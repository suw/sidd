# Copyright (c) 2011-2013, ImageCat Inc.
#
# This program is free software: you can redistribute it and/or modify 
# it under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or 
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License 
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
Widget (Panel) for creating mapping scheme
"""
import functools

from PyQt4.QtGui import QWidget, QMessageBox, QDialog, QAbstractItemView, QFileDialog
from PyQt4.QtCore import QObject, QSize, QPoint, pyqtSlot, QString, Qt, QModelIndex

from utils.system import get_app_dir
from sidd.ms import MappingScheme, MappingSchemeZone, Statistics, StatisticNode
from sidd.exception import SIDDException
from sidd.constants import MSExportTypes

from ui.exception import SIDDUIException
from ui.constants import logUICall, get_ui_string, UI_PADDING
from ui.dlg_ms_branch import DialogEditMS
from ui.dlg_save_ms import DialogSaveMS
from ui.dlg_build_ms import DialogMSOptions 
from ui.dlg_edit_zone import DialogEditZoneName
from ui.dlg_size_input import  DialogSizeInput
from ui.helper.ms_tree import MSTreeModel
from ui.helper.vlabel import VerticalQLabel
from ui.helper.ms_leaves_table import MSLeavesTableModel
from ui.qt.wdg_ms_ui import Ui_widgetMappingSchemes

class WidgetMappingSchemes(Ui_widgetMappingSchemes, QWidget):
    """
    Widget (Panel) for creating mapping scheme
    """
    # internal decorator to perform common checks required
    # for many calls
    #############################
    class UICallChecker(object):        
        def __init__(self):
            pass

        def __call__(self, f):            
            @functools.wraps(f)
            def wrapper(*args, **kw):
                # try requested operation
                try:
                    logUICall.log('function call %s from module %s' % (f.__name__, f.__module__), logUICall.DEBUG)                    
                    retval =  f(*args, **kw)
                    return retval                
                except SIDDUIException as err:
                    logUICall.log(self.errString(get_ui_string("app.error.ui"), err), logUICall.WARNING)
                except SIDDException as err:
                    logUICall.log(self.errString(get_ui_string("app.error.model"), err), logUICall.WARNING)
                except Exception as err:
                    logUICall.log(self.errString(get_ui_string("app.error.unexpected"),err), logUICall.ERROR)
            return wrapper
        
        def errString(self, title, err):
            return '%s\n%s' % (title, err)
            
        
    uiCallChecker = UICallChecker()

    # constructor / destructor
    ###############################    
    def __init__(self, app):
        """
        constructor
        - initialize UI elements
        - connect UI elements to callback            
        """
        super(WidgetMappingSchemes, self).__init__()
        self.ui = Ui_widgetMappingSchemes()
        self.ui.setupUi(self)
        
        self.allow_repeats = app.app_config.get('options', 'allow_repeats', False, bool)

        # vertical label for toggle mapping scheme library 
        # table header
        self.table_ms_headers = []
        self.table_ms_headers.append([get_ui_string('widget.ms.distribution.value'), get_ui_string('widget.ms.distribution.value.desc')])
        self.table_ms_headers.append([get_ui_string('widget.ms.distribution.weight'), get_ui_string('widget.ms.distribution.weight.desc')])
        self.table_ms_headers.append([get_ui_string('widget.ms.distribution.size'), get_ui_string('widget.ms.distribution.size.desc')])
        self.table_ms_headers.append([get_ui_string('widget.ms.distribution.cost'), get_ui_string('widget.ms.distribution.cost.desc')])
        self.table_ms_display_formats = ['%s', '%.2f', '%.2f', '%.2f']

        self.ms_library_vlabel = VerticalQLabel(self)
        self.ms_library_vlabel.setText(get_ui_string('widget.ms.library.title'))
        self.ms_library_vlabel.setFixedSize(40, 200)
        self.ms_library_vlabel.setStyleSheet("Font-size:10pt;Font-weight:Bold")        
        self.ms_library_vlabel.clicked.connect(self.showMSLibrary)

        self.bldg_dist_vlabel = VerticalQLabel(self)
        self.bldg_dist_vlabel.setFixedSize(40, 200)
        self.bldg_dist_vlabel.setStyleSheet("Font-size:10pt;Font-weight:Bold")        
        self.bldg_dist_vlabel.setText(get_ui_string('widget.ms.distribution.title'))
        self.bldg_dist_vlabel.clicked.connect(self.showBuildingDistribution)
        
        # fix selection mode for tree view
        self.ui.tree_ms.setSelectionMode(QAbstractItemView.SingleSelection)        
        
        # fix column size for leaf table
        self.ui.table_ms_leaves.verticalHeader().hide()
        self.ui.table_ms_leaves.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.table_ms_leaves.setSortingEnabled(True)
        self.ui.table_ms_leaves.setSelectionMode(QAbstractItemView.SingleSelection)

        self.app = app
        self.ms = None
        self.ui.tree_ms.animated=True
        
        self.msdb_dao =  app.msdb_dao
        for region in self.msdb_dao.get_regions():
            self.ui.list_ms_library_regions.addItem(QString(region))
        
        self.clearMappingScheme()
        
        self.dlgEditMS = DialogEditMS(self.app)
        self.dlgEditMS.setModal(True)
        self.dlgSaveMS = DialogSaveMS(self.app)
        self.dlgSaveMS.setModal(True)        
        self.dlgMSOptions = DialogMSOptions(self.app, self.app.taxonomy, {})
        self.dlgMSOptions.setModal(True)
        self.dlgEditZone = DialogEditZoneName()
        self.dlgEditZone.setModal(True)

        self.dlgSizeInput = DialogSizeInput(self.app)        
        self.dlgSizeInput.setModal(True)

        # connect slots (ui event)
        self.ui.tree_ms.clicked[QModelIndex].connect(self.treeNodeSelected)

        self.ui.btn_create_ms.clicked.connect(self.createMS)
        self.ui.btn_load_ms.clicked.connect(self.loadMS)
        self.ui.btn_save_ms.clicked.connect(self.saveMS)
        self.ui.btn_save_to_lib.clicked.connect(self.saveMSToLib)
        self.ui.btn_expand_tree.clicked.connect(self.expandTree)
        self.ui.btn_collapse_tree.clicked.connect(self.collapseTree)
        
        self.ui.btn_add_zone.clicked.connect(self.addZone)
        self.ui.btn_add_child.clicked.connect(self.addBranch)
        self.ui.btn_del_child.clicked.connect(self.removeBranch)
        self.ui.btn_edit_level.clicked.connect(self.editBranch)

        self.ui.cb_ms_zones.currentIndexChanged[str].connect(self.refreshLeaves)
        self.ui.btn_save_ms_leaves.clicked.connect(self.saveMSLeaves)
        self.ui.ck_use_modifier.toggled.connect(self.refreshLeaves)        

        self.ui.list_ms_library_regions.clicked.connect(self.regionSelected)
        self.ui.list_ms_library_types.clicked.connect(self.typeSelected)
        self.ui.list_ms_library_msnames.clicked.connect(self.msSelected)
        self.ui.btn_del_lib_ms.clicked.connect(self.deleteLibraryMS)

        self.ui.btn_add_branch.clicked.connect(self.appendBranch)
        
        self.ui.btn_secondary_mod.clicked.connect(self.setModifiers)
        self.ui.btn_build_exposure.clicked.connect(self.applyMS)
        self.ui.table_ms_leaves.doubleClicked.connect(self.editAdditionalAttributes)
        
        self.ms_library_visible = True
        self.setMSLibraryVisible(False)        

        if not app.app_config.get('options', 'parse_modifier', True, bool):
            self.ui.btn_secondary_mod.setVisible(False)
            
    # UI event handling calls
    ###############################
    @pyqtSlot(QObject)
    def resizeEvent(self, event):
        """ handle window resize """ 
        ui = self.ui
        # adjust location of vertical label
        self.bldg_dist_vlabel.move(self.width()-self.bldg_dist_vlabel.width(),
                                      self.ui.widget_ms_library.y())        
        self.ms_library_vlabel.move(self.width()-self.ms_library_vlabel.width(),
                                    self.ui.widget_ms_library.y()+self.bldg_dist_vlabel.height())

        # move buttons to bottom right
        ui.btn_build_exposure.move(self.width()-ui.btn_build_exposure.width()-UI_PADDING,
                                   self.height()-ui.btn_build_exposure.height()-UI_PADDING)
        ui.btn_secondary_mod.move(
            QPoint(ui.btn_build_exposure.x()-ui.btn_secondary_mod.width()-UI_PADDING,
                   ui.btn_build_exposure.y()))
        
        panel_width = (self.width() - self.bldg_dist_vlabel.width()) / 2 - UI_PADDING
        panel_height = ui.btn_build_exposure.y()- ui.widget_ms_library.y()
        # adjust widget_ms_tree
        ui.widget_ms_tree.resize(panel_width, panel_height)       
        ui.tree_ms.resize(QSize(ui.widget_ms_tree.width(), ui.widget_ms_tree.height()-ui.tree_ms.y()))        
        ui.widget_ms_buttons_r.move(
            QPoint(ui.widget_ms_tree.width()-ui.widget_ms_buttons_r.width(), ui.widget_ms_buttons_r.y()))
        
        # right align ms_library and ms_leaves 
        # NOTE: they occupy the same location (same size)
        ui.widget_ms_library.setGeometry(ui.widget_ms_tree.x()+ui.widget_ms_tree.width(),   # x
                                         ui.widget_ms_library.y(),                          # y
                                         panel_width, panel_height)        
        ui.widget_ms_leaves.setGeometry(ui.widget_ms_tree.x()+ui.widget_ms_tree.width(),    # x
                                        ui.widget_ms_library.y(),                          # y
                                        panel_width, panel_height)
        ui.txt_leaves_total.move(ui.widget_ms_leaves.width() - ui.txt_leaves_total.width()-2*UI_PADDING, 
                                 panel_height-ui.txt_leaves_total.height()-2*UI_PADDING)
        ui.lb_leaves_total.move(ui.txt_leaves_total.x() - ui.txt_leaves_total.width(),
                                ui.txt_leaves_total.y())
        ui.table_ms_leaves.resize(panel_width - 6*UI_PADDING, ui.lb_leaves_total.y()-ui.table_ms_leaves.y() - 2*UI_PADDING)
        # logo
        self.ui.lb_gem_logo.move(self.width()-self.ui.lb_gem_logo.width(), self.ui.lb_gem_logo.y())
        
    @uiCallChecker
    @pyqtSlot()
    def createMS(self):
        """ create new mapping scheme """
        # load existing options
        options = self.app.project.operator_options
        self.dlgMSOptions.attribute_ranges.clear()
        for attr in self.dlgMSOptions.attributes:
            if options.has_key(attr.name):
                self.dlgMSOptions.attribute_ranges[attr.name] = options[attr.name]
        if options.has_key('attribute.order'):
            self.dlgMSOptions.attribute_order = options['attribute.order']
        else:
            self.dlgMSOptions.attribute_order = [attr.name for attr in self.dlgMSOptions.attributes]
        
        if options.has_key('stratified.sampling'):
            self.dlgMSOptions.use_sampling = options['stratified.sampling']
        else:
            self.dlgMSOptions.use_sampling = False
        if self.dlgMSOptions.exec_() == QDialog.Accepted:
            # set options
            options['attribute.order'] = self.dlgMSOptions.attribute_order
            for attr, attr_range in self.dlgMSOptions.attribute_ranges.iteritems():
                options[attr] = attr_range
            options['stratified.sampling'] = self.dlgMSOptions.use_sampling 
            # process
            if self.dlgMSOptions.build_option == self.dlgMSOptions.BUILD_EMPTY:
                self.app.createEmptyMS()
            else:
                self.app.buildMappingScheme()
    
    @uiCallChecker
    @pyqtSlot()
    def loadMS(self):
        """ save existing mapping scheme """
        if self.ms is not None and not self.ms.is_empty:
            # alert user
            answer = QMessageBox.warning(self,
                                         get_ui_string("app.confirm.title"),
                                         get_ui_string("widget.ms.warning.replace"),
                                         QMessageBox.Yes | QMessageBox.No)
            if answer == QMessageBox.No:
                return
        self.app.getOpenFileName(self, 
                                 get_ui_string("widget.ms.file.open"),
                                 get_ui_string("app.extension.xml"), 
                                 self.app.loadMS)
        
    @uiCallChecker
    @pyqtSlot()
    def saveMS(self):
        filename = QFileDialog.getSaveFileName(self,
                                               get_ui_string("widget.result.export.folder.open"),
                                               get_app_dir(),
                                               get_ui_string("app.extension.xml"))
        if not filename.isNull():            
            self.app.exportMS(filename, MSExportTypes.XML)

    @uiCallChecker
    @pyqtSlot()
    def saveMSLeaves(self):
        filename = QFileDialog.getSaveFileName(self,
                                               get_ui_string("widget.result.export.folder.open"),
                                               get_app_dir(),
                                               get_ui_string("app.extension.csv"))
        if not filename.isNull():            
            self.app.exportMS(filename, MSExportTypes.CSV)

    @uiCallChecker
    @pyqtSlot()
    def saveMSToLib(self):
        """ save existing mapping scheme """
        if self.ms is not None:
            # show save dialogbox for mapping scheme
            self.dlgSaveMS.setMS(self.ms)
            self.dlgSaveMS.exec_()

    @uiCallChecker
    @pyqtSlot()
    def expandTree(self):
        selectedIndexes = self.ui.tree_ms.selectedIndexes()
        if len(selectedIndexes) == 0:
            self.ui.tree_ms.expandAll()
        else:
            self.recursiveExpand(self.ui.tree_ms, selectedIndexes[0], True)
    
    @uiCallChecker
    @pyqtSlot()
    def collapseTree(self):
        selectedIndexes = self.ui.tree_ms.selectedIndexes()
        if len(selectedIndexes) == 0:
            self.ui.tree_ms.collapseAll()            
        else:
            self.recursiveExpand(self.ui.tree_ms, selectedIndexes[0], False)
    
    @uiCallChecker
    @pyqtSlot()
    def addZone(self):
        ans = self.dlgEditZone.exec_()
        if ans == QDialog.Accepted:
            new_zone_name = self.dlgEditZone.get_zone_name()
            for zone in self.ms.get_zones():
                if zone.name == new_zone_name:
                    raise SIDDException('zone already exists')
            
            statistics = Statistics(self.app.taxonomy)
            zone = MappingSchemeZone(new_zone_name)
            self.ms.assign(zone, statistics)
            self.showMappingScheme(self.ms)        
    
    @uiCallChecker
    @pyqtSlot()
    def addBranch(self):
        """ add branch to mapping scheme """
        node = self.getSelectedNode(self.ui.tree_ms)
        if type(node) == MappingSchemeZone:
            node = node.stats.get_tree()
        
        # show save dialogbox for selected node
        self.dlgEditMS.setNode(node, self.app.project.operator_options, addNew=True)
        ans = self.dlgEditMS.exec_()

        # accepted means apply change        
        if ans == QDialog.Accepted:
            # NOTE: dlgEditMS should already have performed all the checks on 
            #       values/weights pair, we can safely assume that data is clean 
            #       to be used    
                        
            node.update_children(self.dlgEditMS.current_attribute, self.dlgEditMS.values, self.dlgEditMS.weights)
            self.refreshTree()
            self.refreshLeaves(self.ui.cb_ms_zones.currentText())            

    @uiCallChecker
    @pyqtSlot()
    def removeBranch(self):
        """ remove branch from mapping scheme tree """
        node = self.getSelectedNode(self.ui.tree_ms)
        answer = QMessageBox.warning(self,
                                     get_ui_string("app.confirm.title"),
                                     get_ui_string("widget.ms.warning.deletebranch"),
                                     QMessageBox.Yes | QMessageBox.No)
        if answer == QMessageBox.Yes:
            self.app.deleteMSBranch(node)
            self.refreshTree()
            self.refreshLeaves(self.ui.cb_ms_zones.currentText())
        
    @uiCallChecker
    @pyqtSlot()
    def editBranch(self):
        """ edit a branch from mapping scheme tree """
        node = self.getSelectedNode(self.ui.tree_ms)
        if type(node) == MappingSchemeZone:
            # node correspond to zone, edit name
            zone_to_edit = None
            zone_names = []
            for zone in self.ms.get_zones():
                if zone.name == node.name:
                    zone_to_edit = zone
                zone_names.append(zone.name)
            if zone_to_edit is None:
                raise SIDDException('zone not found')
            
            self.dlgEditZone.set_zone_name(node.name)
            ans = self.dlgEditZone.exec_()
            if ans == QDialog.Accepted:
                new_zone_name = self.dlgEditZone.get_zone_name()
                try:
                    zone_names.index(new_zone_name)
                    raise SIDDException('zone already exists')
                    return 
                except:
                    pass
                zone_to_edit.name = new_zone_name
                self.showMappingScheme(self.ms)
        else:
            # node correspond to mapping scheme node, edit tree level
            
            # show save dialogbox for selected node
            self.dlgEditMS.setNode(node, self.app.project.operator_options)
            ans = self.dlgEditMS.exec_()
    
            # accepted means apply change        
            if ans == QDialog.Accepted:
                # NOTE: dlgEditMS should already have performed all the checks on 
                #       values/weights pair, we can safely assume that data is clean 
                #       to be used    
                
                # some children were deleted confirm again
                if len(self.dlgEditMS.values) < len(node.children): 
                    answer = QMessageBox.warning(self,
                                                 get_ui_string("app.confirm.title"),
                                                 get_ui_string("widget.ms.warning.deletebranch"),
                                                 QMessageBox.Yes | QMessageBox.No)
                    if answer == QMessageBox.No:
                        return
                node.parent.update_children(self.dlgEditMS.current_attribute, self.dlgEditMS.values, self.dlgEditMS.weights)            
                self.refreshTree()
                self.refreshLeaves(self.ui.cb_ms_zones.currentText())

    @uiCallChecker
    @pyqtSlot()
    def appendBranch(self):
        """ 
        event handler for btn_add_branch 
        - append branch to mapping scheme tree 
        """
        # get selected node from working mapping scheme tree
        try:
            node = self.getSelectedNode(self.ui.tree_ms)
            branch = self.getSelectedNode(self.ui.tree_ms_library)
        except:
            raise SIDDUIException(get_ui_string("widget.ms.warning.node.branch.required"))
        self.app.appendMSBranch(node, branch)
        
    @uiCallChecker
    @pyqtSlot()
    def setModifiers(self):
        """
        event handler for btn_secondary_mod 
        - switch view to secondary modifier tab
        """        
        self.app.showTab(2)

    @uiCallChecker
    @pyqtSlot()
    def applyMS(self):
        """  
        event handler for btn_build_exposure 
        - apply mapping scheme and generate exposure 
        """        
        self.app.buildExposure()

    @pyqtSlot()
    def showMSLibrary(self):        
        self.setMSLibraryVisible(True)

    @pyqtSlot()
    def showBuildingDistribution(self):
        self.setMSLibraryVisible(False)
            
    @logUICall
    @pyqtSlot(int)
    def regionSelected(self, modelIndex):
        """
        update mapping scheme types and available mapping schemes list
        according to selected region
        """
        # get selected region
        region = str(self.ui.list_ms_library_regions.currentItem().text())
        
        # adjust UI to display results
        self.resetMSLibrary()
        for mstype in self.msdb_dao.get_types_in_region(region):
            self.ui.list_ms_library_types.addItem(QString(mstype))
        
    @logUICall
    @pyqtSlot(int)
    def typeSelected(self, modelIndex):
        """
        update available mapping schemes list according to selected type
        """
        # get selected region/type
        region = str(self.ui.list_ms_library_regions.currentItem ().text())
        mstype = str(self.ui.list_ms_library_types.currentItem ().text())
        
        # adjust UI to display results
        #self.ui.list_ms_library_msnames.clear()
        self.resetMSLibrary(clearTypes=False)               
        for ms_name in self.msdb_dao.get_ms_in_region_type(region, mstype):
            self.ui.list_ms_library_msnames.addItem(QString(ms_name))        

    @logUICall
    @pyqtSlot(int)
    def msSelected(self, modelIndex):
        """ visualize selected mapping scheme from available list """

        # get selected region/type/ms
        region = str(self.ui.list_ms_library_regions.currentItem ().text())
        ms_type = str(self.ui.list_ms_library_types.currentItem ().text())
        ms_name = str(self.ui.list_ms_library_msnames.currentItem().text())       
        
        # deserialize mapping scheme object from XML in DB
        [date_created, data_source, quality, use_notes, ms_xml] = self.msdb_dao.get_ms(region, ms_type, ms_name)
        
        self.ui.txt_ms_library_date.setText(date_created)
        self.ui.txt_ms_library_datasource.setText(data_source)
        self.ui.txt_ms_library_quality.setText(quality)
        self.ui.txt_ms_library_notes.setText(use_notes) 
        lib_ms = MappingScheme(None)
        lib_ms.from_text(ms_xml)
        
        # adjust UI to display results
        self.ui.tree_ms_library.setModel(MSTreeModel(lib_ms))
        self.ui.tree_ms_library.setSelectionMode(QAbstractItemView.SingleSelection)
        
        if (ms_type == get_ui_string('app.mslibrary.user.multilevel') or
            ms_type == get_ui_string('app.mslibrary.user.singlelevel')):
            self.ui.btn_del_lib_ms.setEnabled(True)

    @logUICall
    @pyqtSlot()    
    def deleteLibraryMS(self):
        # get selected region/type/ms
        region = str(self.ui.list_ms_library_regions.currentItem ().text())
        ms_type = str(self.ui.list_ms_library_types.currentItem ().text())
        ms_name = str(self.ui.list_ms_library_msnames.currentItem().text())        
        
        if (ms_type != get_ui_string('app.mslibrary.user.multilevel') and
            ms_type != get_ui_string('app.mslibrary.user.singlelevel')):
            logUICall.log(get_ui_string('widget.ms.library.delete.denied'), logUICall.WARNING)
            return
        # deserialize mapping scheme object from XML in DB
        self.msdb_dao.delete_ms(region, ms_type, ms_name)
        self.resetMSLibrary()        

    @pyqtSlot(QModelIndex)    
    def treeNodeSelected(self, index=None):
        node = index.internalPointer()
        new_zone = None     
        if type(node) == MappingSchemeZone:
            new_zone = node.name
        else:
            stat = self.ms.get_assignment_by_node(node)
            if stat is not None:
                new_zone = stat.root.value
        if new_zone is not None:
            if self.ui.cb_ms_zones.currentText() != new_zone:
                    self.ui.cb_ms_zones.setCurrentIndex(self.ui.cb_ms_zones.findText(new_zone))

    @uiCallChecker
    @pyqtSlot(str)
    def refreshLeaves(self, value): 
        if self.ms is None or self.ui.cb_ms_zones.count() == 0:
            return       
        values = []
        total_weights = 0
        use_modifier = self.ui.ck_use_modifier.isChecked()
        zone_selected = str(self.ui.cb_ms_zones.currentText())
        try:
            stats = self.ms.get_assignment_by_name(zone_selected)
            stats.refresh_leaves(use_modifier)
            for val, wt, node in stats.leaves:
                weight = wt *100.0
                size = node.get_additional_float(StatisticNode.AverageSize)
                cost = node.get_additional_float(StatisticNode.UnitCost)                
                total_weights += weight
                values.append([val, weight, size, cost, node])
        except Exception, err:
            raise SIDDException(str(err))
        try:
            self.ui.table_ms_leaves.setModel(MSLeavesTableModel(values, self.table_ms_headers, self.table_ms_display_formats,
                                                                self.ms.taxonomy, self.ms.taxonomy.codes))
        except Exception, err:
            raise SIDDException(str(err))
        self.ui.table_ms_leaves.horizontalHeader().resizeSection(0, self.ui.table_ms_leaves.width() * 0.60)
        self.ui.table_ms_leaves.horizontalHeader().resizeSection(1, self.ui.table_ms_leaves.width() * 0.14)  
        self.ui.table_ms_leaves.horizontalHeader().resizeSection(2, self.ui.table_ms_leaves.width() * 0.13)
        self.ui.table_ms_leaves.horizontalHeader().resizeSection(3, self.ui.table_ms_leaves.width() * 0.13)
        self.ui.txt_leaves_total.setText('%.1f' % total_weights)

    @logUICall
    @pyqtSlot()
    def editAdditionalAttributes(self):
        selected =self.ui.table_ms_leaves.selectedIndexes()
        if (len(selected) > 0):            
            self.dlgSizeInput.setNode(selected[0].internalPointer(), self.ms)
            if self.dlgSizeInput.exec_() == QDialog.Accepted:
                self.dlgSizeInput.node.set_additional(StatisticNode.AverageSize, self.dlgSizeInput.avg_size)
                self.dlgSizeInput.node.set_additional(StatisticNode.UnitCost, self.dlgSizeInput.unit_cost)
                self.refreshLeaves(self.ui.cb_ms_zones.currentText())                
        return
    
    # public methods
    ###############################
    @logUICall
    def showMappingScheme(self, ms):
        """ display mapping scheme """
        self.ms = ms
        treeUI = self.ui.tree_ms
        self.tree_model = MSTreeModel(ms)        
        treeUI.setModel(self.tree_model)
        self.ui.tree_ms.setEnabled(True)
        
        self.ui.cb_ms_zones.clear()
        for zone in self.ms.get_zones():
            self.ui.cb_ms_zones.addItem(zone.name)
    
    @logUICall
    def refreshTree(self):
        indices = self.tree_model.persistentIndexList()
        for index in indices:
            if self.ui.tree_ms.isExpanded(index):
                self.ui.tree_ms.setExpanded(index, False)             
                self.ui.tree_ms.setExpanded(index, True)
        
    @logUICall
    def clearMappingScheme(self):
        self.ms = None
        self.ui.tree_ms.setModel(None)
        self.ui.tree_ms.setEnabled(False)
        self.ui.table_ms_leaves.setModel(None)
        self.ui.cb_ms_zones.clear()
        
    # internal helper methods
    ###############################
    def setMSLibraryVisible(self, visible):
        self.ms_library_visible = visible        
        self.ui.widget_ms_library.setVisible(visible)
        self.ui.widget_ms_leaves.setVisible(not visible)
        if not visible:
            self.resetMSLibrary()
            self.ms_library_vlabel.setEnabled(True)            
            # set Disable stops event
            self.bldg_dist_vlabel.setEnabled(False)
            # Selected label is black, not selected is gray 
            self.ms_library_vlabel.setSelected(False)
            self.bldg_dist_vlabel.setSelected(True)
        else:
            # set Disable stops event
            self.ms_library_vlabel.setEnabled(False)
            self.bldg_dist_vlabel.setEnabled(True)
            # Selected label is black, not selected is gray 
            self.ms_library_vlabel.setSelected(True)
            self.bldg_dist_vlabel.setSelected(False)

    def getSelectedNode(self, tree):
        """ retrieve currently selected node from given tree """
        selectedIndexes = tree.selectedIndexes()
        if (len(selectedIndexes) <= 0):
            raise SIDDUIException(get_ui_string("widget.ms.warning.node.required"))
            return None
        if not selectedIndexes[0].isValid():
            raise SIDDUIException(get_ui_string("widget.ms.warning.node.invalid"))
            return None
        return selectedIndexes[0].internalPointer()

    def resetMSLibrary(self, clearTypes=True, clearNames=True):
        """ reset mapping scheme library UI elements """
        if clearTypes:
            self.ui.list_ms_library_types.clear()
        if clearNames:
            self.ui.list_ms_library_msnames.clear()
        self.ui.tree_ms_library.setModel(None)
        self.ui.txt_ms_library_date.setText("")
        self.ui.txt_ms_library_datasource.setText("")
        self.ui.txt_ms_library_quality.setText("")
        self.ui.txt_ms_library_notes.setText("")   
        self.ui.btn_del_lib_ms.setEnabled(False)      

    def recursiveExpand(self, tree, index, expand):
        tree.setExpanded(index, expand)
        for i in range(index.model().rowCount(index)):
            child = index.child(i, 0)
            self.recursiveExpand(tree, child, expand)
