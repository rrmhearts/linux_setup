import sys
sys.path.insert(0, '/home/vagrant/linux_setup/sikuli/examples')
from test_helper import TestHelper

helper = TestHelper("open_flex")

helper.Click("Createanewpr.png", "Cannot find `Create a new project`")
type("hello")
helper.Click("OK.png", "Cannot find `OK`")
if exists(Pattern("OK-2.png").similar(0.88)):
    helper.Click(Pattern("OK-1.png").similar(0.86), "Cannot find `OK`")
else:
    helper.Click(Pattern("Qpen.png").similar(0.80), "Cannot find `Open`")
    
def open_handler(event):
    helper.write("Successfully opened flex.")
    event.region.stopObserver()

def green_handler(event):
    helper.write_fail("An error has occurred (green)")
    event.region.stopObserver()
    
onAppear("1435347136957.png", open_handler)
onAppear("Anerrorhasoc.png", green_handler)
observe(40)

if helper.has_fail():
    helper.write_fail("Failed to open")


