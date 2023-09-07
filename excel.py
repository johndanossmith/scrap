from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import xlwt
from xlwt import Workbook

driver=webdriver.Chrome()
driver.get("https://yogmaratha.com/")

profile_button = driver.find_element(By.XPATH, "//a[@class='primary-btn cta-btn' and @href='details.php?id=BR4827' and @tabindex='0']")
profile_button.click()

sur = driver.find_element(By.XPATH, "//*[@id='product-tab']/div/div[1]/div/div")
surname=sur.text

age = driver.find_element(By.XPATH, "//*[@id='product-tab']/div/div[2]/div/div")
agenum=age.text

cast = driver.find_element(By.XPATH, "//*[@id='product-tab']/div/div[3]/div/div")
casttext=cast.text

marital = driver.find_element(By.XPATH, "//*[@id='product-tab']/div/div[4]/div/div")
maritaltext=marital.text

hei = driver.find_element(By.XPATH, "//*[@id='product-tab']/div/div[5]/div/div")
height=hei.text

wei = driver.find_element(By.XPATH, "//*[@id='product-tab']/div/div[6]/div/div")
weight=wei.text

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
  
sheet1.write(1, 0, surname)
sheet1.write(2, 0, agenum)
sheet1.write(3, 0, casttext)
sheet1.write(4, 0, maritaltext)
sheet1.write(5, 0, height)
sheet1.write(6, 0, weight)
  
wb.save('xlwt example.xls')

time.sleep(100)