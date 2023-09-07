from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import soundfile
import speech_recognition as sr
import os
import urllib
import pandas as pd

username = "company@k-andi.co.jp"
password = "FKrAd7kQk7sLPb"

# Go to site
driver = webdriver.Chrome()
driver.get('https://rmt.club/')

# Press the sell button
sell_button = driver.find_element("xpath", "//img[@class= 'top_slide_pc']")
sell_button.click()
# Input email and password
email_input = driver.find_element(By.NAME, "data[User][mail]")
email_input.send_keys(username)
time.sleep(1)
pwd_input = driver.find_element(By.NAME, "data[User][password]")
pwd_input.send_keys(password)
time.sleep(3)

# Click the captcha button
recaptcha = driver.find_element(By.XPATH, "//div[@class = 'g-recaptcha']")
recaptcha.click()
time.sleep(1)

#Judge the status of check
check_status = driver.find_element(By.XPATH, "//div[3]")
status = check_status.value_of_css_property("visibility")
print(status)

if status != "hidden":
    # Get audio challenge
    driver.switch_to.default_content()
    frames = driver.find_element(By.XPATH, "//div[3]/div[4]/iframe")
    driver.switch_to.frame(frames)
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
    soundfile.write('rmt.wav',data,samplerate, subtype='PCM_16')
    r=sr.Recognizer()
    with sr.AudioFile("rmt.wav") as source:
        audio_data=r.record(source)
        text=r.recognize_google(audio_data)
        print(text)
    time.sleep(5)

    # Click the verify button
    driver.find_element(By.ID, "audio-response").send_keys(text)
    time.sleep(2)
    driver.find_element(By.ID, "recaptcha-verify-button").click()

time.sleep(2)
driver.switch_to.default_content()

login_click = driver.find_element("xpath", "//input[@class='btn_type1 fade']")
login_click.click()

display_button = driver.find_element("xpath", "//img[@class= 'top_slide_pc']")
display_button.click()

time.sleep(2)
sale_button = driver.find_element("xpath", "//label[@for='DealRequest0']")
sale_button.click()

googlesheetid='1uXXG0LjOf6xIr3mqimVH6Kcwkj-tYZ_oLOpgYlQJAnA'
sheetname='RMT.club'
url=f"https://docs.google.com/spreadsheets/d/{googlesheetid}/gviz/tq?tqx=out:csv&sheet={sheetname}"
content=pd.read_csv(url)

game_name = driver.find_element(By.NAME, "data[Deal][game_title]")
game_name.send_keys(content.iloc[0,1])

publication_title = driver.find_element(By.NAME, "data[Deal][deal_title]")
publication_title.send_keys(content.iloc[0,2])

tag = driver.find_element(By.NAME, "data[Deal][tag]")
tag.send_keys(content.iloc[0,3])

detail = driver.find_element(By.NAME, "data[Deal][info]")
detail.send_keys(content.iloc[0,4])

# upload_button = driver.find_element("xpath", "//label[@id='add_upload_file' and @class='btn_up file_upload_wrapper']")
# upload_button.click()
driver.find_element(By.XPATH, "//input[@type='file']").send_keys(r"F:\Portfolio\8.png")

price_budget = int(content.iloc[0,6])
price = driver.find_element(By.NAME, "data[Deal][deal_price]")
price.send_keys(price_budget)

confirm_button = driver.find_element(By.NAME, "smt_confirm")
confirm_button.click()

agree_button = driver.find_element(By.NAME, "data[Deal][agreement]")
agree_button.click()

finish_button = driver.find_element(By.NAME, "smt_finish")
finish_button.click()
time.sleep(50)