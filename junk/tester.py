import argparse
import os
import sys
import unittest
from testcases import test

class TestLoader:
    @staticmethod
    def __load_test(path, file_name, suite):
        sys.path.append(path)
        import_modula = __import__(file_name)
        loaded_suite = unittest.TestLoader().loadTestsFromModule(import_modula)
        suite.addTest(loaded_suite)
        sys.path.pop()

    def load_test_from(self, directory, suite):
        for file in os.listdir(directory):
            if os.path.isdir(os.path.join(directory,file)):
                self.load_test_from(os.path.join(directory, file), suite)
            if not (file.endswith('test.py') or file.endswith('tests.py')):
                continue
            self.__load_test(directory, file[:-3], suite)

if __name__ == "__main__":
    argparse = argparse.ArgumentParser()
    argparse.add_argument('--XMl', help='XML kimenet', action="store_true")
    args = argparse.parse_args()

    print('Loadin test modules', file=sys.stderr)
    main_suite = unittest.TestSuite()
    Loader = TestLoader()
    Loader.load_test_from('testcases', main_suite)
    print('running test', file=sys.stderr)
    unittest.TextTestRunner(verbosity=2).run(main_suite)