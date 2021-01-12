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

    spaced_repetition_gaps = [
        "1 day",
        "1 days",
        "2 days",
        "3 days",
        "5 days",
        "7 days",
        "10 days",
        "2 weeks",
        "3 weeks",
        "5 weeks",
        "2 months",
        "3 months",
        "5 months",
        "7 months",
        "10 months",
        "1 year",
    ]

    def __init__(self, title, project, desc=None):
        self.title = title
        self.project = project
        if desc:
            self.desc = desc
        else:
            self.desc = ""
        self.tags = "%F0%9F%A4%A9 Do Quick %F0%9F%9A%80"

        # Making the gap-title Dictionary for the reminders function.
        # Placing this here rather than in the next function so I can unit test.
        day1 = "Review: Make {} into Notion Questions - {} later.".format(
            self.title, self.spaced_repetition_gaps[0]
        )
        day2 = "Review: Answer {} questions and categorize Notion page - {} later.".format(
            self.title, self.spaced_repetition_gaps[1]
        )
        title_list = [day1, day2]
        for gap in self.spaced_repetition_gaps[2:]:
            title_list.append("Review: {} - {} later".format(self.title, gap))
        self.gap_title_dict = {
            gap: title for gap, title in zip(self.spaced_repetition_gaps, title_list)
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
