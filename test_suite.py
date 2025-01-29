import unittest

from HTMLTestRunner import HTMLTestRunner

from alerts import TestAlerts
from keys import TestKeys


class TestSuite(unittest.TestCase):

    def test_suite(self):
        test_runs = unittest.TestSuite()

        test_runs.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestKeys))

        test_runs.addTests(
            [
                unittest.defaultTestLoader.loadTestsFromTestCase(TestKeys),
                unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts)
            ]
        )

        runner =  HTMLTestRunner(
            report_name="raport name",
            title="Report tile",
            description="Report description"
        )
        runner.run(test_runs)