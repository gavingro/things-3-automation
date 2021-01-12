# Use this program in your text editor to create spaced repetition to-do's.
# Fill in your Lecture Notes Title (Header), Class (Things Project) Name, and
#       description to add to each to-do.

# Then, when you're ready, run the script.

from things_study_scheduler import ThingsStudyScheduler

# Input the name of the lecture notes here:
reminder_title = """TESTINGTHINGSTODO"""

# Input the name of the class or project area here:
project_area = """Review: MATH 152 - Linear Algebra"""

# Input the description or link you want to attach on the to-do here:
desc = (
    """https://www.notion.so/L1-Working-with-Vectors-8a06aa5ef5074ea7ab4bd3992ca7dfff"""
)
if "www.notion.so" in desc:
    desc = desc.replace("https:", "notion:")

review_scheduler = ThingsStudyScheduler(reminder_title, project_area, desc)

if __name__ == "__main__":
    review_scheduler.schedule_study_reminders()
