# Use this program in your text editor to create spaced repetition to-do's.
# Fill in your reminder title (Header), area (Things Project) Name, and
#       description to add to each to-do.

# Then, when you're ready, run the script.

from things_study_scheduler import ThingsStudyScheduler

# Input the name of the lecture notes here:
reminder_title = """Topic 2: Electric Boogaloo"""

# Input the name of the class or project area here:
project_area = """BLAT 9000"""

# Input the description or link you want to attach on the to-do here:
desc = """You love blat class, just remember to check in on topic 2. https://www.notion.so/BLAT9000"""
if "www.notion.so" in desc:
    desc = desc.replace("https:", "notion:")

review_scheduler = ThingsStudyScheduler(reminder_title, project_area, desc)

if __name__ == "__main__":
    review_scheduler.schedule_study_reminders()
