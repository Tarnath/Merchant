import unittest
from merchant.rendering import scene


class MyTestCase(unittest.TestCase):
    def test_object_cant_be_instantiated(self):
        with self.assertRaises(NotImplementedError):
            scene.Object()


if __name__ == '__main__':
    unittest.main()
