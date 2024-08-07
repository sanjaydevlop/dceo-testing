import pytest
import os
from selenium import webdriver
import time, shutil
import inspect, sys
import logging
import uuid


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
grandparent_dir=os.path.abspath(os.path.join(parent_dir, os.pardir))
sys.path.append(grandparent_dir)
print(grandparent_dir)
driver = None

@pytest.fixture(scope="function")
def setup(request):
    global driver
    driver = webdriver.Chrome()
    driver.get("https://testnhm.nslhub.com/login")
    driver.maximize_window()
    time.sleep(5)
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # file_name = report.nodeid.replace("::", "_") + ".png"
            # timestamp = time.strftime("%Y%m%d-%H%M%S")
            unique_id = str(uuid.uuid4())[:8]  # Limiting to 8 characters for brevity
            file_name = f"{unique_id}.png"
            # file_name = file_name.replace("/", f"_{timestamp}_")
            _capture_screenshot(file_name)
            if file_name:
                screenshot_path = f"{grandparent_dir}/Leave_management_System/screenshots/{file_name}"
                screenshot_path_without_screenshot = f"{grandparent_dir}/Leave_management_System"
                _save_screenshot(screenshot_path_without_screenshot, file_name)
                html = f'<div><img src="{screenshot_path}" alt="screenshot" style="width:304px;height:228px;" ' \
                       f'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

def _save_screenshot(path, name):
    screenshots_dir = os.path.join(path, "screenshots")
    shutil.move(name, os.path.join(screenshots_dir, os.path.basename(name)))
