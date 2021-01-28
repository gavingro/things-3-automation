# things-3-study-automation
A repo for automating the creation of a series of spaced-repetition to-do's to intelligently schedule your studying.



# Usage
*To Come*


## Thoughts
At the time of creation, the only coding foundation I had was a little bit of python.
This is a little bit clunky, especially compared to how CulturedCode has a nice guide for manipulating [Things 3 with Applescript](https://culturedcode.com/things/download/Things3AppleScriptGuide.pdf).
*In the future, I'll probably learn some applescript and "re-do" this project with that in mind.*

Anyways, we're using the [Things URL Scheme](https://culturedcode.com/things/support/articles/2803573/).
The plan is to use python to interact with Things 3 using this scheme so we can automate things.
Then we can even use Alfred workflows to pass in details.

### Goal :
Can we automate the creation of "spaced repetition" tasks in our Retention projects?

### Problem (Why I started this):
I wanted to have good study habits, and I wanted to use my Things 3 environment that I rely on to help me out. I've found a lot of success using spaced repetition in the past, and I excel when I use Things to handle the scheduling of these "check in's".

The catch is, it was a bit of labour up front to manually make these todo's. I had been able to overcome that and do the front-loaded admin work by copying and filling in templates, but that's still a lot of needless toil.
I anticipated that the friction of the monotonous copy-pasting of tasks was going to stop me from studying in an optimal, organized way as I went back to school.

## Known Frustrations
1. Currently the URL schemes do well in "writing" to Things, and opening it up with different searches or views, but very poor in reading information back to my script. It looks like I'll be unable to get the script to "check" if there's already a project made.
    * Since it's a lot quicker to make a quick project than drag a bunch of notes around, I'll have to seperate that task (or do it manually)

2. Currently the URL schemes do not support the creation of headings in a project. I use these headings extensively for organization, and so I'm not ready to give them up.
    * In the meantime I will manually add one in before making my study reminders.

*Perhaps the applescript or JSON solutions will have some answers for in solving these two problems.*

3. Currently, I prefer to set the dates as "Sometime", then schedule the next session at the end of the current session. As such, I've been using this for some weeks without realizing the dates were not cumulative in their spaces. This will be fixed in the next build.

# Filetree

* main.py
  * *The program to be run in order to schedule the to-do's for information you fill in with an editor.*


# Requirements
  * None (Just Python 3). The only imports are from the Python Standard Library.
