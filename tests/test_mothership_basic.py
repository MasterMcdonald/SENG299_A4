
import unittest

from mothership.base import MothershipServer


class TestMothershipBasic(unittest.TestCase):
   
    def test_zelan_test_three(self):
        """
        this test is to test if handle worker contact
        worker not running
        """
        mothership = MothershipServer()
        mothership.run()
        worker = BasicUserParseWorker("https://www.reddit.com/user/Chrikelnel")
		worker.run()
        self.assertRaises(ValueError, worker.send_to_mother(worker, None, mothership))
    