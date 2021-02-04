import pytest
from appium import webdriver

# Constants

APPIUM_HOME = 'http://localhost:4723/wd/hub'


# Hooks
def pytest_bdd_step_error(step):
    print(f'Step failed: {step}')


@pytest.fixture
def android_up_drive():
    desired_cap = dict(
        automationName='UiAutomator2',
        platformName='Android',
        deviceName='GCAZB6010134RCH',
        appPackage='br.com.petz',
        appActivity='br.com.hanzo.petz.view.MainActivity',
        autoGrantPermissions=True
        # noReset=True,
        # fullReset=False
    )

    driver = webdriver.Remote(APPIUM_HOME, desired_cap)
    yield driver.execute()
    driver.quit()