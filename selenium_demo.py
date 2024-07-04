from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Khởi tạo WebDriver
driver = webdriver.Chrome()

# # Điều hướng đến URL
# driver.get("https://fullstack.edu.vn/")

# # Chờ cho trang tải hoàn tất trong vòng 10 giây
# driver.implicitly_wait(10)
# driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]").click()
# driver.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/button[1]").click()
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div/main/div/button[1]").click()


# # Tìm và điền vào trường email
# email_field = driver.find_element(By.ID, 'email')
# email_field.send_keys("ngochuyenn0503@gmail.com")

# # Tìm và điền vào trường mật khẩ
# password_field = driver.find_element(By.ID, 'password')
# password_field.send_keys("Huyen2905")

# # Nhấp vào nút đăng nhập
# login_button = driver.find_element(By.CLASS_NAME, 'btn-login')
# login_button.click()
 

 # Điều hướng đến URL
driver.get("https://www.facebook.com/")

# chờ cho trang tải trong vòng 10 giây
driver.implicitly_wait(10)

# tìm và điền vào trừng email
email_field = driver.find_element(By.ID, 'email')
email_field.send_keys("0346671107")

#tìm và điền vào trường mật Khẩu
password_field = driver.find_element(By.ID, 'pass')
password_field.send_keys("Kimoanh123")

#  nhấp và nút đăng nhập
login_button = driver.find_element(By.XPATH, '//button[@name="login"]') 
login_button.click()

# Chờ cho trang đăng nhập hoàn thành
WebDriverWait(driver, 10).until(EC.url_contains("facebook.com"))

# tìm và điền trường tìm kiếm 
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//input[@type="search"]'))
)
search_button.send_keys("Ngọc Huyền")

search_button.submit()

