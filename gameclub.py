from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import soundfile
import speech_recognition as sr
import os
import urllib
import pandas as pd


username = "i-hirose@k-andi.co.jp"
password = "Ez9ubrcG"

# Go to site
driver = webdriver.Chrome()
driver.get('https://gameclub.jp')

# Press the sell button
sell_button = driver.find_element("xpath", "//i[@class='fas fa-camera']")
sell_button.click()

# Input email and password
email_input = driver.find_element(By.NAME, "email")
email_input.send_keys(username)
time.sleep(2)
pwd_input = driver.find_element(By.NAME, "password")
pwd_input.send_keys(password)
time.sleep(2)

# Click the captcha button
recaptcha = driver.find_element(By.XPATH, "//div[@class = 'g-recaptcha']")
recaptcha.click()
time.sleep(2)

#Judge the status of check
driver.switch_to.default_content()
check_status = driver.find_element(By.XPATH, "//div[5]")
status = check_status.value_of_css_property("visibility")
print(status)

if status != "hidden":
    # Get audio challenge
    driver.switch_to.default_content()
    frames=driver.find_element(By.XPATH, "//div[5]").find_elements(By.TAG_NAME, "iframe")
    driver.switch_to.frame(frames[0])
    driver.find_element(By.ID, "recaptcha-audio-button").click()

    # Click the play button
    driver.switch_to.default_content()   
    frames= driver.find_elements(By.TAG_NAME, "iframe")
    driver.switch_to.frame(frames[-1])
    time.sleep(2)
    driver.find_element(By.XPATH, "//div/div//div[3]/div/button").click()

    #get the mp3 audio file
    src = driver.find_element(By.ID, "audio-source").get_attribute("src")
    print("[INFO] Audio src: %s"%src)   

    #download the mp3 audio file from the source
    urllib.request.urlretrieve(src, os.getcwd()+"\\sample.wav")

    data,samplerate=soundfile.read('sample.wav')
    soundfile.write('new.wav',data,samplerate, subtype='PCM_16')
    r=sr.Recognizer()
    with sr.AudioFile("new.wav") as source:
        audio_data=r.record(source)
        text=r.recognize_google(audio_data)
        print(text)

    # Click the verify button
    driver.find_element(By.ID, "audio-response").send_keys(text)
    driver.find_element(By.ID, "recaptcha-verify-button").click()

time.sleep(3) 

driver.switch_to.default_content()
login_click = driver.find_element(By.XPATH,"//button[@class='btn btn-danger btn-registration']")
login_click.click()

time.sleep(3)
# upload_image = driver.find_element(By.ID, "image-upload-label")
# upload_image.click()
while True:
    driver.find_element(By.XPATH, "//input[@type='file']").send_keys(r"F:\Portfolio\8.png")

    search = driver.find_element(By.ID, "btn-search-title")
    search.click()

    time.sleep(10)
    googlesheetid='1uXXG0LjOf6xIr3mqimVH6Kcwkj-tYZ_oLOpgYlQJAnA'
    sheetname='Gameclub.jp'
    url=f"https://docs.google.com/spreadsheets/d/{googlesheetid}/gviz/tq?tqx=out:csv&sheet={sheetname}"
    content=pd.read_csv(url)

    search_title = driver.find_element(By.ID, "search-title-input")
    search_title.send_keys(content.iloc[0,2])

    time.sleep(2)
    item = driver.find_element(By.XPATH, "//div[@class='item']")
    item.click()

    time.sleep(2)

    radio = driver.find_element(By.ID, "account-type-id-40")
    radio.click()

    name = driver.find_element(By.NAME, "name")
    name.send_keys(content.iloc[0,4])

    detail = driver.find_element(By.NAME, "detail")
    detail.send_keys(content.iloc[0,5])

    retry_time = int(content.iloc[0, 8])
    value = driver.find_element(By.NAME, "subcategory_unique_property_3_value")
    value.send_keys(retry_time)

    notice = driver.find_element(By.NAME, "notice_information")
    notice.send_keys(content.iloc[0,10])

    price_budget = int(content.iloc[0, 11])
    price = driver.find_element(By.NAME, "price")
    price.send_keys(price_budget)

    confirm_button = driver.find_element(By.ID, "btn-confirm")
    confirm_button.click()

    time.sleep(1)
    add_button = driver.find_element(By.ID, "btn-add")
    add_button.click()
    time.sleep(3)
    close_button = driver.find_element(By.XPATH, "//*[@id='content-wrapper']/div/div[2]/div[8]/div/div[1]/i")
    close_button.click()

    time.sleep(10)
    
    return_button = driver.find_element(By.XPATH, "//*[@id='content-wrapper']/header/div/div[2]/div[2]/a[2]")
    return_button.click()
