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
    A class of objects that when created (planned in alfred), will be able
    to use make_spaced_repition_reminders() function to auto - populate
    my Things 3.
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
        self.title = title.replace(" ", "%20")
        self.project = project.replace(" ", "%20")
        if link:
            self.link = link
        else:
            self.link = ""
        self.tags = "testing"

    def make_spaced_repition_reminders(self):
        """
        Uses the spaced repition list and makes a series of ToDo's in Things 3
        with the title, spaced out according to the spaced repition.

        In the future, this will make it in a certain project as well
        """
        day1 = "Review: Make {self.title} into Notion Categories - {self.spaced_repetition_gaps[0]} later.".replace(
            " ", "%20"
        )
        day2 = f"Review: Make {self.title} into Notion Quiz Questions - {self.spaced_repetition_gaps[1]} later.".replace(
            " ", "%20"
        )
        title_list = [day1, day2]
        for gap in self.spaced_repetition_gaps[2:]:
            title_list.append(f"Review: {self.title} - {gap} later".replace(" ", "%20"))
        gap_title_dict = {
            gap: title for gap, title in zip(self.spaced_repetition_gaps, title_list)
        }

        for gap, title in gap_title_dict:
            webbrowser.open(
                self.addlink
                + title
                + "&notes="
                + self.link
                + "&tags="
                + self.tags
                + "&when="
                + "in%20{}%20days".format(gap)
            )
