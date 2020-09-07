import unittest
from things_trials import *


class TestThingsMaker(unittest.TestCase):
    def setUp(self):
        self.things_maker_object = ThingsMaker()

    def test_things_maker_traits(self):
        self.assertEqual(str, type(self.things_maker_object.addlink))


if __name__ == "__main__":
    unittest.main()
