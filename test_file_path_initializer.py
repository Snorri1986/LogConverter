import unittest
import prep


class MyTestCase(unittest.TestCase):
    def test_prep(self):
        prep.init_path_variables()
        self.assertIsNotNone(prep.deposit_task_log_path)
        self.assertIsNotNone(prep.loan_task_log_path)


if __name__ == '__main__':
    unittest.main()
