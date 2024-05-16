# ========================================================================
# Copyright (c) Quandri Tech. All Rights Reserved.
#
# This file is proprietary and confidential. Unauthorized copying
# of this file, via any medium, is strictly prohibited.
#
# ========================================================================


from RPA.Browser.Selenium import Selenium
from RPA.FileSystem import FileSystem
from pathlib import Path

browser = Selenium()
filesystem = FileSystem()

def take_screenshot_of_website():
    url = "https://quandri.io"
    output_dir = "output/screenshot.png"
    
    # Ensure the output directory exists
    Path(output_dir).parent.mkdir(parents=True, exist_ok=True)
    
    # Open the browser in headless mode
    browser.open_available_browser(url, headless=True)
    browser.capture_page_screenshot(output_dir)
    browser.close_all_browsers()

if __name__ == "__main__":
    take_screenshot_of_website()