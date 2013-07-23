import glob
import unittest
import logging

logging.disable(logging.CRITICAL)

test_file_paths = glob.glob('Test*.py')
test_names = [path[:-3] for path in test_file_paths]
test_suites = [unittest.defaultTestLoader.loadTestsFromName(name) for name in test_names]
suite = unittest.TestSuite(test_suites)
unittest.TextTestRunner(verbosity=2).run(suite)