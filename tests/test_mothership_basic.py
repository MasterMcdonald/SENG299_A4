
import unittest

from mothership.base import MothershipServer


class TestMothershipBasic(unittest.TestCase):

    def test_zelan_test_two(self):
        """
        this test is to test if handle worker contact
		worker not running
        """
        mothership = MothershipServer()
       
        self.assertRaises(ValueError, mothership.run)