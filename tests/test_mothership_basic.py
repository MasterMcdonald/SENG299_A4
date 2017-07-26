
import unittest

from mothership.base import MothershipServer
from workers.basic_worker import BasicUserParseWorker


class TestMothershipBasic(unittest.TestCase):
    pass
    def test_zelan_test_three(self):
        """
        this test is to test if handle worker contact
        worker not running
        """
        mothership = MothershipServer()
        mothership.run()
        worker = BasicUserParseWorker("https://www.reddit.com/user/Chrikelnel")
        worker.run()
        #try:
        #    worker.run()
        #except ConnectionRefusedError:
        #    self.fail("Error")
        self.assertRaises(ValueError, worker.send_to_mother(worker, None, mothership))