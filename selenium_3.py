from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import imaplib 
import email
from email.header import decode_header
import webbrowser 
import os
import re
from imap_tools import MailBox, AND

email_name = 'ngochuyenxu2905@gmail.com'
email_password = 'acdeydciopkdrqnw'

def get_code(email_name, email_password):
  verification_code = ""
  def extract_verification_code(text):
    match = re.search(r'\b\d{6}\b', text)
    return match.group() if match else None
  with MailBox("imap.gmail.com").login(email_name, email_password, "INBOX") as mailbox:
    # Search for emails from Facebook
    emails = mailbox.fetch(criteria=AND(from_="no-reply@zoom.us"), limit=2, reverse=True, mark_seen=False)
    
    for msg in emails:
        
        # Extract the verification code from the email body
        verification_code = extract_verification_code(msg.subject)
        if verification_code:
            print(f"Verification code: {verification_code}")
            return verification_code
        else:
            print("Not found.")
  return verification_code

# Get the verification code
verification_code = get_code(email_name, email_password)

# Khởi tạo webdriver
driver = webdriver.Chrome()
driver.get('https://zoom.us/join')

driver.implicitly_wait(10)

# Registration
btn_signup = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/nav/div[2]/div/ul[2]/li[3]/a')
btn_signup.click()

btn_click = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[3]/button').click()

# Your Birth 
year = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div/div/div/div/input')
year.send_keys('2003')

bnt_continue = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div/div/button').click()

email = driver.find_element(By.ID, 'email')
email.send_keys('ngochuyenxu2905@gmail.com')

botton = driver.find_element(By.CLASS_NAME, 'zm-button__slot').click()

text = driver.find_element(By.CLASS_NAME, 'zm-pin-code__input')
text.send_keys('get_code(email_name,email_password)')

btn_accuracy = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div/div[4]/button').click()






