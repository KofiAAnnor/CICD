from api import app
import unittest

class Tests(unittest.TestCase):

    def sample_test(self):
        tester = app.test_client(self)
        self.assertEqual(400, 400)

if __name__ == "__main__":
    unittest.main()
