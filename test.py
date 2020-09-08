import unittest
from things_classes import ThingsMaker, ThingsStudyScheduler


class TestThingsMaker(unittest.TestCase):
    def setUp(self):
        self.things_maker = ThingsMaker()

    def test_things_maker_traits(self):
        self.assertEqual(str, type(self.things_maker.addlink))


class TestStudyScheduler(unittest.TestCase):
    def setUp(self):
        title = "This is a test to do"
        project = "Testing Project"
        link = "https:\\fakelinkstring"
        self.study_scheduler = ThingsStudyScheduler(title, project, link)

    def test_things_study_scheduler_init(self):
        self.assertNotEqual(len(self.study_scheduler.addlink), 0)
        self.assertEqual(str, type(self.study_scheduler.title))
        self.assertEqual(str, type(self.study_scheduler.project))
        self.assertIn("Do Quick", self.study_scheduler.tags)
        self.assertEqual(len(self.study_scheduler.spaced_repetition_gaps), 16)
        self.assertTrue(self.study_scheduler.gap_title_dict["1 day"])


if __name__ == "__main__":
    unittest.main()
