import webbrowser


class ThingsMaker:
    """
    A class to centralize the automation of things tasks.
    Currently only used with the ThingsStudyModule() subclass.

    Left an open framework for future automations
    """

    addlink = "things:///add?title="


class ThingsStudyScheduler(ThingsMaker):
    """
    A class to setup spaced repition reminders in Things for studying.


    Parameters
    **********
    title = The title of the lecture you want to review
    project = The things Project that the reminders will populate in.
    link = An optional link to your page of notes in Notion or Bear.


    Methods
    *******
    make_spaced_repition_reminders()
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

    def __init__(self, title, project, link=None):
        self.title = title
        self.project = project
        if link:
            self.link = link
        else:
            self.link = ""
        self.tags = "%F0%9F%A4%A9 Do Quick %F0%9F%9A%80"

        # Making the gap-title Dictionary for the reminders function.
        # Placing this here rather than in the next function so I can unit test.
        day1 = "Review: Make {} into Notion Categories - {} later.".format(
            self.title, self.spaced_repetition_gaps[0]
        )
        day2 = "Review: Make {} into Notion Quiz Questions - {} later.".format(
            self.title, self.spaced_repetition_gaps[1]
        )
        title_list = [day1, day2]
        for gap in self.spaced_repetition_gaps[2:]:
            title_list.append("Review: {} - {} later".format(self.title, gap))
        self.gap_title_dict = {
            gap: title for gap, title in zip(self.spaced_repetition_gaps, title_list)
        }

    def schedule_study_reminders(self):
        """
        Generates a series of ToDo's in Things 3 with the given title,
        project, and description (link) at the Heading equal to the title, all
        spaced out according to spaced repition.
        """
        for gap, title in self.gap_title_dict.items():
            webbrowser.open(
                self.addlink
                + title.replace(" ", "%20").replace(":", "%3A")
                + "&notes="
                + self.link.replace(":", "%3A")
                + "&when="
                + "someday"  # gap.replace(" ", "%20").replace(":", "%3A")
                + "&tags="
                + self.tags.replace(" ", "%20")
                + "&list="
                + self.project.replace(" ", "%20").replace(":", "%3A")
                + "&heading="
                + self.title.replace(" ", "%20").replace(":", "%3A")
            )
