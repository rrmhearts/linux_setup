import a_setup

from sikuli import *
from flex_regions import *
from test_helper import TestHelper

"""
Click through all of the buttons in the left sidebar
on the Lexicon screen.
Make sure the middle part of the screen changes
within 5 seconds.
If an information box pops up, close it.
Return to first option when done.
"""

# Setup
helper = TestHelper("try_all_side_bar_buttons")
set_flex_helper(helper)

def stop_observer(event):
    global changed
    changed = True
    event.region.stopObserver()
    if Region(148,139,544,545).exists("information_popup.png"):
        helper.Type(Key.ENTER, time=5)
    
# Opening
###############
helper.Click("Lexicon.png", "Couldn't find 'Lexicon' button")
first_region = Region(21,127,115,15)
click(first_region.getCenter())

# Set initial region to click
region = first_region.offset(Location(0, 18))
count = 0

# Goal
###############

# keep clicking while the list still has items 
while not region.exists(Pattern("blank_space.png").similar(0.99)):
    
    global changed
    changed = False

    # keep count and make sure we don't go too far
    count += 1
    if count > 9:
        helper.write_fail("Script malfunction: went too far down the left column")
        break;

    # Click in the middle of the region and react to change
    MID_TOOLBAR.onChange(stop_observer)
    click(region.getCenter())
    MID_TOOLBAR.observe(5)
    # Check if the observer stopped as intended
    if not changed:
        helper.write_fail("No change when clicking item " + str(count))

    # Move region down by 18 pixels
    region = region.offset(Location(0, 18))

# Closing
###############

# go back to first screen
click(first_region.getCenter())

helper.write_success()
