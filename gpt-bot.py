from selenium import webdriver
from PIL import Image
import time

# initialize the Chrome webdriver
driver = webdriver.Chrome()

# navigate to the Dev.to website
driver.get("https://dev.to")

# set a timer to take a screenshot every 1 minute
# while True:
#     # take a screenshot of the website
#     screenshot_name = "devto_screenshot.png"
#     driver.save_screenshot(screenshot_name)

#     # open the screenshot and save the image locally
#     with Image.open(screenshot_name) as img:
#         img.save("devto_screenshot_local.png")

#     # pause the script for 60 seconds
#     time.sleep(60)

# take a screenshot of the website
screenshot_name = "devto_screenshot.png"
driver.save_screenshot(screenshot_name)
# open the screenshot and save the image locally
with Image.open(screenshot_name) as img:
    img.save("devto_screenshot.png")
# pause the script for 60 seconds
# time.sleep(60)

# close the web driver
driver.quit()