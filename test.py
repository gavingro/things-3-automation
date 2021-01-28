import unittest
from things_maker import ThingsMaker
from things_study_scheduler import ThingsStudyScheduler


class TestThingsMaker(unittest.TestCase):
    def setUp(self):
        self.things_maker = ThingsMaker()

    def test_things_maker_traits(self):
        self.assertEqual(str, type(self.things_maker.things_url))


class TestStudyScheduler(unittest.TestCase):
    def setUp(self):
        title = "This is a test to do"
        project = "Testing Project"
        desc = "https:\\fakelinkstring for studying"
        self.study_scheduler = ThingsStudyScheduler(title, project, desc)

    def test_things_study_scheduler_init(self):
        self.assertNotEqual(len(self.study_scheduler.things_url), 0)
        self.assertEqual(str, type(self.study_scheduler.title))
        self.assertEqual(str, type(self.study_scheduler.project))
        self.assertIn("Do Quick", self.study_scheduler.tags)
        self.assertEqual(len(self.study_scheduler.spaced_repetition_gaps), 12)
        self.assertEqual(len(self.study_scheduler.gap_title_dict), 14)
        self.assertTrue(self.study_scheduler.gap_title_dict["in 1 days"])

    def test_things_study_scheduler_clean_attributes(self):
        self.study_scheduler.clean_attributes()
        self.assertNotIn(" ", self.study_scheduler.title)
        self.assertNotIn(":", self.study_scheduler.desc)
        self.assertNotIn(" ", self.study_scheduler.project)

    def test_things_generate_link(self):
        self.study_scheduler.clean_attributes()
        url = self.study_scheduler.get_generator_link()
        self.assertTrue(url)
        self.assertNotIn(" ", url)
        self.assertIn("things:///add?", url)


if __name__ == "__main__":
    unittest.main()
