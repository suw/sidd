# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt\wdg_ms.ui'
#
# Created: Fri Jun 21 14:28:01 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_widgetMappingSchemes(object):
    def setupUi(self, widgetMappingSchemes):
        widgetMappingSchemes.setObjectName(_fromUtf8("widgetMappingSchemes"))
        widgetMappingSchemes.resize(950, 750)
        self.btn_secondary_mod = QtGui.QPushButton(widgetMappingSchemes)
        self.btn_secondary_mod.setGeometry(QtCore.QRect(630, 620, 131, 31))
        self.btn_secondary_mod.setObjectName(_fromUtf8("btn_secondary_mod"))
        self.btn_build_exposure = QtGui.QPushButton(widgetMappingSchemes)
        self.btn_build_exposure.setGeometry(QtCore.QRect(780, 620, 131, 31))
        self.btn_build_exposure.setObjectName(_fromUtf8("btn_build_exposure"))
        self.lb_panel_title = QtGui.QLabel(widgetMappingSchemes)
        self.lb_panel_title.setGeometry(QtCore.QRect(10, 0, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.lb_panel_title.setFont(font)
        self.lb_panel_title.setObjectName(_fromUtf8("lb_panel_title"))
        self.widget_ms_tree = QtGui.QWidget(widgetMappingSchemes)
        self.widget_ms_tree.setGeometry(QtCore.QRect(10, 40, 331, 571))
        self.widget_ms_tree.setObjectName(_fromUtf8("widget_ms_tree"))
        self.widget_ms_buttons_r = QtGui.QWidget(self.widget_ms_tree)
        self.widget_ms_buttons_r.setGeometry(QtCore.QRect(160, 0, 171, 31))
        self.widget_ms_buttons_r.setObjectName(_fromUtf8("widget_ms_buttons_r"))
        self.btn_edit_level = QtGui.QPushButton(self.widget_ms_buttons_r)
        self.btn_edit_level.setGeometry(QtCore.QRect(140, 0, 31, 23))
        self.btn_edit_level.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/imgs/icons/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_edit_level.setIcon(icon)
        self.btn_edit_level.setObjectName(_fromUtf8("btn_edit_level"))
        self.btn_del_child = QtGui.QPushButton(self.widget_ms_buttons_r)
        self.btn_del_child.setGeometry(QtCore.QRect(110, 0, 31, 23))
        self.btn_del_child.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/imgs/icons/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_del_child.setIcon(icon1)
        self.btn_del_child.setObjectName(_fromUtf8("btn_del_child"))
        self.btn_add_child = QtGui.QPushButton(self.widget_ms_buttons_r)
        self.btn_add_child.setGeometry(QtCore.QRect(80, 0, 31, 23))
        self.btn_add_child.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/imgs/icons/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_child.setIcon(icon2)
        self.btn_add_child.setObjectName(_fromUtf8("btn_add_child"))
        self.btn_add_zone = QtGui.QPushButton(self.widget_ms_buttons_r)
        self.btn_add_zone.setGeometry(QtCore.QRect(50, 0, 31, 23))
        self.btn_add_zone.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/imgs/icons/element_clouds.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_zone.setIcon(icon3)
        self.btn_add_zone.setObjectName(_fromUtf8("btn_add_zone"))
        self.tree_ms = QtGui.QTreeView(self.widget_ms_tree)
        self.tree_ms.setGeometry(QtCore.QRect(0, 30, 331, 541))
        self.tree_ms.setObjectName(_fromUtf8("tree_ms"))
        self.widget_ms_buttons_l = QtGui.QWidget(self.widget_ms_tree)
        self.widget_ms_buttons_l.setGeometry(QtCore.QRect(0, 0, 141, 31))
        self.widget_ms_buttons_l.setObjectName(_fromUtf8("widget_ms_buttons_l"))
        self.btn_save_ms = QtGui.QPushButton(self.widget_ms_buttons_l)
        self.btn_save_ms.setGeometry(QtCore.QRect(30, 0, 31, 23))
        self.btn_save_ms.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/imgs/icons/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save_ms.setIcon(icon4)
        self.btn_save_ms.setObjectName(_fromUtf8("btn_save_ms"))
        self.btn_create_ms = QtGui.QPushButton(self.widget_ms_buttons_l)
        self.btn_create_ms.setGeometry(QtCore.QRect(0, 0, 31, 23))
        self.btn_create_ms.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/imgs/icons/new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_create_ms.setIcon(icon5)
        self.btn_create_ms.setObjectName(_fromUtf8("btn_create_ms"))
        self.btn_expand_tree = QtGui.QPushButton(self.widget_ms_buttons_l)
        self.btn_expand_tree.setGeometry(QtCore.QRect(80, 0, 31, 23))
        self.btn_expand_tree.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/imgs/icons/magnify_plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_expand_tree.setIcon(icon6)
        self.btn_expand_tree.setObjectName(_fromUtf8("btn_expand_tree"))
        self.btn_collapse_tree = QtGui.QPushButton(self.widget_ms_buttons_l)
        self.btn_collapse_tree.setGeometry(QtCore.QRect(110, 0, 31, 23))
        self.btn_collapse_tree.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/imgs/icons/magnify_minus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_collapse_tree.setIcon(icon7)
        self.btn_collapse_tree.setObjectName(_fromUtf8("btn_collapse_tree"))
        self.widget_ms_library = QtGui.QWidget(widgetMappingSchemes)
        self.widget_ms_library.setGeometry(QtCore.QRect(350, 70, 561, 541))
        self.widget_ms_library.setObjectName(_fromUtf8("widget_ms_library"))
        self.btn_add_branch = QtGui.QPushButton(self.widget_ms_library)
        self.btn_add_branch.setGeometry(QtCore.QRect(0, 150, 31, 23))
        self.btn_add_branch.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/imgs/icons/arrow_left.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_branch.setIcon(icon8)
        self.btn_add_branch.setObjectName(_fromUtf8("btn_add_branch"))
        self.box_ms_library = QtGui.QGroupBox(self.widget_ms_library)
        self.box_ms_library.setEnabled(True)
        self.box_ms_library.setGeometry(QtCore.QRect(40, 0, 521, 541))
        self.box_ms_library.setObjectName(_fromUtf8("box_ms_library"))
        self.list_ms_library_regions = QtGui.QListWidget(self.box_ms_library)
        self.list_ms_library_regions.setGeometry(QtCore.QRect(310, 40, 200, 191))
        self.list_ms_library_regions.setObjectName(_fromUtf8("list_ms_library_regions"))
        self.lb_ms_library_regions = QtGui.QLabel(self.box_ms_library)
        self.lb_ms_library_regions.setGeometry(QtCore.QRect(310, 20, 200, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_ms_library_regions.setFont(font)
        self.lb_ms_library_regions.setObjectName(_fromUtf8("lb_ms_library_regions"))
        self.lb_ms_library_types = QtGui.QLabel(self.box_ms_library)
        self.lb_ms_library_types.setGeometry(QtCore.QRect(310, 240, 200, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_ms_library_types.setFont(font)
        self.lb_ms_library_types.setObjectName(_fromUtf8("lb_ms_library_types"))
        self.list_ms_library_types = QtGui.QListWidget(self.box_ms_library)
        self.list_ms_library_types.setGeometry(QtCore.QRect(310, 260, 200, 81))
        self.list_ms_library_types.setObjectName(_fromUtf8("list_ms_library_types"))
        self.list_ms_library_msnames = QtGui.QListWidget(self.box_ms_library)
        self.list_ms_library_msnames.setGeometry(QtCore.QRect(310, 380, 200, 151))
        self.list_ms_library_msnames.setObjectName(_fromUtf8("list_ms_library_msnames"))
        self.lb_ms_library_msnames = QtGui.QLabel(self.box_ms_library)
        self.lb_ms_library_msnames.setGeometry(QtCore.QRect(310, 350, 200, 25))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_ms_library_msnames.setFont(font)
        self.lb_ms_library_msnames.setObjectName(_fromUtf8("lb_ms_library_msnames"))
        self.tree_ms_library = QtGui.QTreeView(self.box_ms_library)
        self.tree_ms_library.setGeometry(QtCore.QRect(10, 40, 280, 321))
        self.tree_ms_library.setObjectName(_fromUtf8("tree_ms_library"))
        self.lb_tree_ms_library = QtGui.QLabel(self.box_ms_library)
        self.lb_tree_ms_library.setGeometry(QtCore.QRect(20, 20, 280, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_tree_ms_library.setFont(font)
        self.lb_tree_ms_library.setObjectName(_fromUtf8("lb_tree_ms_library"))
        self.lb_ms_library_date = QtGui.QLabel(self.box_ms_library)
        self.lb_ms_library_date.setGeometry(QtCore.QRect(10, 370, 100, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_ms_library_date.setFont(font)
        self.lb_ms_library_date.setObjectName(_fromUtf8("lb_ms_library_date"))
        self.lb_ms_library_notes = QtGui.QLabel(self.box_ms_library)
        self.lb_ms_library_notes.setGeometry(QtCore.QRect(10, 460, 100, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_ms_library_notes.setFont(font)
        self.lb_ms_library_notes.setObjectName(_fromUtf8("lb_ms_library_notes"))
        self.txt_ms_library_date = QtGui.QLineEdit(self.box_ms_library)
        self.txt_ms_library_date.setGeometry(QtCore.QRect(120, 370, 171, 20))
        self.txt_ms_library_date.setReadOnly(True)
        self.txt_ms_library_date.setObjectName(_fromUtf8("txt_ms_library_date"))
        self.txt_ms_library_notes = QtGui.QTextEdit(self.box_ms_library)
        self.txt_ms_library_notes.setGeometry(QtCore.QRect(120, 460, 171, 71))
        self.txt_ms_library_notes.setReadOnly(True)
        self.txt_ms_library_notes.setObjectName(_fromUtf8("txt_ms_library_notes"))
        self.txt_ms_library_datasource = QtGui.QLineEdit(self.box_ms_library)
        self.txt_ms_library_datasource.setGeometry(QtCore.QRect(120, 400, 171, 20))
        self.txt_ms_library_datasource.setReadOnly(True)
        self.txt_ms_library_datasource.setObjectName(_fromUtf8("txt_ms_library_datasource"))
        self.lb_ms_library_datasource = QtGui.QLabel(self.box_ms_library)
        self.lb_ms_library_datasource.setGeometry(QtCore.QRect(10, 400, 100, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_ms_library_datasource.setFont(font)
        self.lb_ms_library_datasource.setObjectName(_fromUtf8("lb_ms_library_datasource"))
        self.lb_ms_library_quality = QtGui.QLabel(self.box_ms_library)
        self.lb_ms_library_quality.setGeometry(QtCore.QRect(10, 430, 100, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_ms_library_quality.setFont(font)
        self.lb_ms_library_quality.setObjectName(_fromUtf8("lb_ms_library_quality"))
        self.txt_ms_library_quality = QtGui.QLineEdit(self.box_ms_library)
        self.txt_ms_library_quality.setGeometry(QtCore.QRect(120, 430, 171, 21))
        self.txt_ms_library_quality.setReadOnly(True)
        self.txt_ms_library_quality.setObjectName(_fromUtf8("txt_ms_library_quality"))
        self.lb_ms_library_ms = QtGui.QLabel(self.box_ms_library)
        self.lb_ms_library_ms.setGeometry(QtCore.QRect(10, 20, 100, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_ms_library_ms.setFont(font)
        self.lb_ms_library_ms.setObjectName(_fromUtf8("lb_ms_library_ms"))
        self.btn_del_lib_ms = QtGui.QPushButton(self.box_ms_library)
        self.btn_del_lib_ms.setGeometry(QtCore.QRect(480, 350, 31, 25))
        self.btn_del_lib_ms.setText(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/imgs/icons/minus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_del_lib_ms.setIcon(icon9)
        self.btn_del_lib_ms.setObjectName(_fromUtf8("btn_del_lib_ms"))
        self.widget_ms_leaves = QtGui.QWidget(widgetMappingSchemes)
        self.widget_ms_leaves.setGeometry(QtCore.QRect(220, 640, 561, 531))
        self.widget_ms_leaves.setObjectName(_fromUtf8("widget_ms_leaves"))
        self.table_ms_leaves = QtGui.QTableView(self.widget_ms_leaves)
        self.table_ms_leaves.setGeometry(QtCore.QRect(40, 50, 521, 441))
        self.table_ms_leaves.setObjectName(_fromUtf8("table_ms_leaves"))
        self.cb_ms_zones = QtGui.QComboBox(self.widget_ms_leaves)
        self.cb_ms_zones.setGeometry(QtCore.QRect(110, 0, 151, 22))
        self.cb_ms_zones.setObjectName(_fromUtf8("cb_ms_zones"))
        self.lb_ms_zones = QtGui.QLabel(self.widget_ms_leaves)
        self.lb_ms_zones.setGeometry(QtCore.QRect(40, 0, 91, 16))
        self.lb_ms_zones.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lb_ms_zones.setObjectName(_fromUtf8("lb_ms_zones"))
        self.txt_leaves_total = QtGui.QLineEdit(self.widget_ms_leaves)
        self.txt_leaves_total.setGeometry(QtCore.QRect(410, 500, 151, 20))
        self.txt_leaves_total.setReadOnly(True)
        self.txt_leaves_total.setObjectName(_fromUtf8("txt_leaves_total"))
        self.lb_leaves_total = QtGui.QLabel(self.widget_ms_leaves)
        self.lb_leaves_total.setGeometry(QtCore.QRect(300, 500, 91, 20))
        self.lb_leaves_total.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_leaves_total.setObjectName(_fromUtf8("lb_leaves_total"))
        self.lb_ms_leaves = QtGui.QLabel(self.widget_ms_leaves)
        self.lb_ms_leaves.setGeometry(QtCore.QRect(40, 30, 111, 16))
        self.lb_ms_leaves.setObjectName(_fromUtf8("lb_ms_leaves"))
        self.btn_save_bldg_distribution = QtGui.QPushButton(self.widget_ms_leaves)
        self.btn_save_bldg_distribution.setGeometry(QtCore.QRect(530, 20, 31, 23))
        self.btn_save_bldg_distribution.setText(_fromUtf8(""))
        self.btn_save_bldg_distribution.setIcon(icon4)
        self.btn_save_bldg_distribution.setObjectName(_fromUtf8("btn_save_bldg_distribution"))
        self.ck_use_modifier = QtGui.QCheckBox(self.widget_ms_leaves)
        self.ck_use_modifier.setGeometry(QtCore.QRect(300, 0, 131, 17))
        self.ck_use_modifier.setObjectName(_fromUtf8("ck_use_modifier"))
        self.lb_gem_logo = QtGui.QLabel(widgetMappingSchemes)
        self.lb_gem_logo.setGeometry(QtCore.QRect(830, 0, 121, 61))
        self.lb_gem_logo.setText(_fromUtf8(""))
        self.lb_gem_logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/imgs/gem_logo_120X60.png")))
        self.lb_gem_logo.setScaledContents(False)
        self.lb_gem_logo.setObjectName(_fromUtf8("lb_gem_logo"))

        self.retranslateUi(widgetMappingSchemes)
        QtCore.QMetaObject.connectSlotsByName(widgetMappingSchemes)

    def retranslateUi(self, widgetMappingSchemes):
        widgetMappingSchemes.setWindowTitle(QtGui.QApplication.translate("widgetMappingSchemes", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_secondary_mod.setText(QtGui.QApplication.translate("widgetMappingSchemes", "Modifiers", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_build_exposure.setText(QtGui.QApplication.translate("widgetMappingSchemes", "Build Exposure", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_panel_title.setText(QtGui.QApplication.translate("widgetMappingSchemes", "Manage Mapping Schemes", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_edit_level.setToolTip(QtGui.QApplication.translate("widgetMappingSchemes", "Edit Level", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_del_child.setToolTip(QtGui.QApplication.translate("widgetMappingSchemes", "Delete Selected Node ", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_add_child.setToolTip(QtGui.QApplication.translate("widgetMappingSchemes", "Add/Edit Child Nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_add_zone.setToolTip(QtGui.QApplication.translate("widgetMappingSchemes", "Add New Zone", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_save_ms.setToolTip(QtGui.QApplication.translate("widgetMappingSchemes", "Save Mapping Scheme", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_create_ms.setToolTip(QtGui.QApplication.translate("widgetMappingSchemes", "Create New Mapping Scheme", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_expand_tree.setToolTip(QtGui.QApplication.translate("widgetMappingSchemes", "Expand Mapping Scheme Tree", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_collapse_tree.setToolTip(QtGui.QApplication.translate("widgetMappingSchemes", "Collapse Mapping Scheme Tree", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_add_branch.setToolTip(QtGui.QApplication.translate("widgetMappingSchemes", "Append Selected Mapping Scheme from Library to Zone", None, QtGui.QApplication.UnicodeUTF8))
        self.box_ms_library.setTitle(QtGui.QApplication.translate("widgetMappingSchemes", "Mapping Scheme Library", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_ms_library_regions.setText(QtGui.QApplication.translate("widgetMappingSchemes", "Regions", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_ms_library_types.setText(QtGui.QApplication.translate("widgetMappingSchemes", "Types", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_ms_library_msnames.setText(QtGui.QApplication.translate("widgetMappingSchemes", "Available Mapping Schemes", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_ms_library_date.setText(QtGui.QApplication.translate("widgetMappingSchemes", "Date Created", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_ms_library_notes.setText(QtGui.QApplication.translate("widgetMappingSchemes", "Use Notes", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_ms_library_datasource.setText(QtGui.QApplication.translate("widgetMappingSchemes", "Data Source", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_ms_library_quality.setText(QtGui.QApplication.translate("widgetMappingSchemes", "Data Measured", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_ms_library_ms.setText(QtGui.QApplication.translate("widgetMappingSchemes", "Mapping Scheme", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_del_lib_ms.setToolTip(QtGui.QApplication.translate("widgetMappingSchemes", "Delete Selected Mapping Scheme", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_ms_zones.setText(QtGui.QApplication.translate("widgetMappingSchemes", "Select zone", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_leaves_total.setText(QtGui.QApplication.translate("widgetMappingSchemes", "Total", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_ms_leaves.setText(QtGui.QApplication.translate("widgetMappingSchemes", "Building Distribution", None, QtGui.QApplication.UnicodeUTF8))
        self.ck_use_modifier.setText(QtGui.QApplication.translate("widgetMappingSchemes", "Include Modifiers", None, QtGui.QApplication.UnicodeUTF8))

import SIDDResource_rc
