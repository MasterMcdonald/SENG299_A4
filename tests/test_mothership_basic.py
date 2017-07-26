
import unittest

from mothership.base import MothershipServer


class TestMothershipBasic(unittest.TestCase):
    pass
    '''@unittest.expectedFailure
    def test_zelan_test_two(self):
        """
        this test is to test if handle worker contact
        worker not running
        """
        mothership = MothershipServer()
        mothership.run()
        worker = BasicUserParseWorker("https://www.reddit.com/user/Chrikelnel")
        self.assertRaises(ConnectionRefusedError, worker.run)
    '''