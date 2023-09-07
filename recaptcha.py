import os
from python3_anticaptcha import NoCaptchaTaskProxyless
from anticaptchaofficial.recaptchav2proxyless import *
from selenium import webdriver

ANTICAPTCHA_KEY = "b7566ed9ddedea93b852bb09f856c76d"

def solveCaptcha():
    result = NoCaptchaTaskProxyless.NoCaptchaTaskProxyless(
        anticaptcha_key=ANTICAPTCHA_KEY
    ).captcha_handler(
        websiteURL="https://www.google.com/recaptcha/api2/demo",
        websiteKey="6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-",
    )
    return result.get("solution").get("gRecaptchaResponse")

driver=webdriver.Chrome()
driver.get("https://www.google.com/recaptcha/api2/demo")
captcha_response = solveCaptcha()

driver.execute_script(
    "arguments[0].style.display='inline'",
    driver.find_element("xpath",
        '//*[@id="g-recaptcha-response"]'
    ),
)
driver.execute_script(
'document.getElementById("g-recaptcha-response").innerHTML = "%s"'
            % captcha_response
)
print("Sfdf")
submit = driver.find_element("xpath", "//input[@id='recaptcha-demo-submit']")
submit.click()
time.sleep(120)