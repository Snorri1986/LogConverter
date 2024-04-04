import unittest
import file_path_initializer


class MyTestCase(unittest.TestCase):
    def test_init_path_variables(self):
        file_path_initializer.init_path_variables()
        self.assertIsNotNone(file_path_initializer.deposit_task_log_path)
        self.assertIsNotNone(file_path_initializer.loan_task_log_path)


if __name__ == '__main__':
    unittest.main()
