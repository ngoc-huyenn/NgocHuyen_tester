from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#khởi tạo Webdriver 
driver = webdriver.Chrome()

driver.get('https://tuoitre.vn/')

driver.implicitly_wait(10)

# Nút đnhap/đki
login_form= driver.find_element(By.ID, "head_login")
login_form.click()

# #tìm và điền trường đki
# botton = driver.find_element(By.ID, "profile-tab").click()
# email_field = driver.find_element(By.ID, "input-username-register")
# email_field.send_keys('Ngochuyexu2905@gmail.com')
# pass_field = driver.find_element(By.ID, "password-field-login")
# pass_field.send_keys('Huyen2905')
# checkbox = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[1]/div/div/span").click()

# submit = driver.find_element(By.ID, "submit-register-form").click()


# Tìm và điền trường vào đăng nhập
text_field = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/div/div[1]/form/label[1]/input")
text_field.send_keys('ngochuyenn0503@gmail.com')

password_field = driver.find_element(By.ID, "password-field-register")
password_field.send_keys('Huyen2905')

submitlogin = driver.find_element(By.ID, "button-login")
submitlogin.click()

btn = driver.find_element(By.XPATH, '//*[@id="box-login-success"]/div/div/div/div/div[4]/button').click()

# Search
search_header = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div[1]/a[1]').click()

text_box = driver.find_element(By.XPATH, '//*[@id="admWrapsite"]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div[1]/input')
text_box.send_keys('Đà Nẵng')

search_box = driver.find_element(By.XPATH, '//*[@id="admWrapsite"]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div[1]/a[2]').click()
