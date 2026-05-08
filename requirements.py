import io
from PIL import Image
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options import XCUITestOptions

options = XCUITestOptions()
options.platform_name = "iOS"
options.automation_name = "XCUITest"
options.device_name = "iPhone"          # TODO: fill in
options.udid = ""                        # TODO: fill in (idevice_id -l)
options.bundle_id = ""                   # TODO: fill in

driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(10)

driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Edit').click()

driver.quit()
