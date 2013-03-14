# SeismiCat: an on-line seismic risk assessment tool for 
# building property owners, lenders, insurers and municipal analysts. 
# @copyright  (c)2012 ImageCat inc, All rights reserved
# @link       http://www.seismicat.com
# @since      SeismiCat v1.0
# @license    
# @version    $Id: ms_unittest.py 19 2012-10-25 01:06:59Z zh $
#

import os

# import sidd packages for testing
from sidd.ms import MappingScheme, MappingSchemeZone, \
                    Statistics, StatisticNode, StatisticError

from common import SIDDTestCase
 
class MSTestCase(SIDDTestCase):

    # run for every test
    ##################################    
    def setUp(self):
        super(MSTestCase, self).setUp()
        self.survey_file = self.test_data_dir + "survey.csv"
        self.ms_file = self.test_data_dir + "ms.xml"
        self.ms_file2 = self.test_data_dir + "ms2.xml"

    # tests
    ##################################
    
    def test_BuildMS(self, skipTest=False):
        import csv
        survey = csv.reader(open(self.survey_file , 'r'), delimiter=',', quotechar='"')
        # skip header, there is probably a better way to do this
        survey.next()

        stats = Statistics(self.taxonomy)
        stats.set_attribute_skip(3, True)
        stats.set_attribute_skip(4, True)
        stats.set_attribute_skip(5, True)
        stats.set_attribute_skip(6, True)
        _count=0

        for row in survey:
            tax_string = row[2]
            stats.add_case(tax_string)
        stats.finalize()
        
        ms = MappingScheme(self.taxonomy)
        ms_zone = MappingSchemeZone('ALL')
        ms.assign(ms_zone, stats)

        if skipTest:
            return ms
        
        ms2 = MappingScheme(self.taxonomy)
        ms2.read(self.ms_file2)
        
        self.assertEqual(
            ms.get_assignment_by_name("ALL").to_xml().strip().__len__(),
            ms2.get_assignment_by_name("ALL").to_xml().strip().__len__()
        )
  
    def test_SaveMS(self):
        tmp_ms_file = self.test_tmp_dir + "tmp_ms.xml"
        ms = self.test_BuildMS(skipTest=True)        
        ms.save(tmp_ms_file)
        
        self.assertTrue(os.path.exists(tmp_ms_file))
        os.remove(tmp_ms_file)

    def test_LoadMS(self, skipTest=False, statsOnly=True):
        ms = MappingScheme(self.taxonomy)
        ms.read(self.ms_file)
        
        if skipTest:
            if statsOnly:
                return ms.get_assignment_by_name("ALL")
            else:
                return ms
        
        stats = ms.get_assignment_by_name("ALL")
        attributes = stats.get_attributes(stats.get_tree())
        expected = ['Material', 'Lateral Load-Resisting System', 'Roof', 'Occupancy']
        self.assertEqual(attributes, expected)
        
    def test_StatsAddBranch(self):
        stats = self.test_LoadMS(skipTest=True, statsOnly=True)
        
        # cannot add tree to self because of conflicting attributes
        with self.assertRaises(StatisticError):
            stats.add_branch(stats.get_tree().children[0], stats.get_tree())

        # sure be able to add new node
        node = stats.get_tree().children[0]
        new_node = StatisticNode(None, "nothing", "val", 0)
        stats.add_branch(node, new_node)
        
        self.assertEquals(len(node.children), 2)
    
    def test_StatsRandomWalk(self):
        self.test_LoadMS(skipTest=True, statsOnly=True)
        
                
    def test_StatsLeaves(self):
        stats = self.test_LoadMS(skipTest=True, statsOnly=True)
        leaves =  stats.get_leaves(refresh=True, with_modifier=True)
        total = 0
        for l in leaves:
            total += l[1]
        self.assertAlmostEqual(total, 1)

        leaves =  stats.get_leaves(refresh=True, with_modifier=False)
        total = 0
        for l in leaves:
            total += l[1]
        self.assertAlmostEqual(total, 1)
        