import webbrowser
from things_maker import ThingsMaker


class ThingsStudyScheduler(ThingsMaker):
    """
    A class to setup spaced repition reminders in Things for studying.


    Parameters
    **********
    title = The title of the thing that you want to review.
    project = The things Project that the reminders will populate in.
    desc = An optional desc to your page of notes in Notion or Bear.


    Methods
    *******
    schedule_study_reminders()
        =   Uses a spaced repetition series of dates and things 3's natural
            language parsing, and generates a series of 16 reminder todo's
            into the future with increasingly larger gaps between them.

    """

    spaced_repetition_gaps = {
        # "1 day": 0,     Included by hand to say today and tomorrow
        # "1 days": 1,
        "2 days": 3,
        "3 days": 6,
        "5 days": 11,
        "8 days": 19,
        "2 weeks": 33,
        "3 weeks": 54,
        "5 weeks": 89,
        "2 months": 121,
        "3 months": 181,
        "5 months": 320,
        "8 months": 561,
        "1 year": 926,
    }

    def __init__(self, title, project, desc=None):
        self.title = title
        self.project = project
        if desc:
            self.desc = desc
        else:
            self.desc = ""
        self.tags = "%F0%9F%A4%A9 Do Quick %F0%9F%9A%80"

        # Making the gap-title Dictionary for the reminders function.

        title_gap_dict = {
            f"Review: {self.title} - {gap} later.": days
            for gap, days in self.spaced_repetition_gaps.items()
        }

        title_gap_dict[f"Review: Make {self.title} into Review Questions - today"] = 0
        title_gap_dict[f"Review: Answer {self.title} Review Questions - tomorrow"] = 1

        self.gap_title_dict = {
            f"in {gap} days": title for title, gap in title_gap_dict.items()
        }

    def clean_attributes(self):
        """
        Replaces characters that could cause errors when opening the things url
        link in all the class attributes needed to create the to-do's.
        """
        bad_characters = {
            " ": "%20",
            ":": "%3A",
        }
        for character, replacement in bad_characters.items():
            self.title = self.title.replace(character, replacement)
            self.desc = self.desc.replace(character, replacement)
            self.tags = self.tags.replace(character, replacement)
            self.project = self.project.replace(character, replacement)
            # TODO: How can we replace this with a list? Pass by reference?

    def get_generator_link(self, title="Untitled", gap="in 1 day"):
        """
        Uses the cleaned attributes, the things url scheme link, and the
        passed in to-do title to return a url link that when opened, will
        generate the necessary todo.
        """
        generator_url = (
            self.things_url
            + title.replace(" ", "%20").replace(":", "%3A")
            + "&notes="
            + self.desc
            + "&when="
            + gap.replace(" ", "%20").replace(":", "%3A")
            + "&tags="
            + self.tags
            + "&list="
            + self.project
            + "&heading="
            + self.title
        )
        return generator_url

    def schedule_study_reminders(self):
        """
        Generates a series of ToDo's in Things 3 with the given title,
        project, and description (desc) at the Heading equal to the title, all
        spaced out according to spaced repition.
        """
        self.clean_attributes()
        for gap, title in self.gap_title_dict.items():
            webbrowser.open(self.get_generator_link(title, gap))
