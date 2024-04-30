import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_online_status():
    numara = "Numarayı buraya yazın" 
    online_start_time = None

    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")

    while True:
        driver.refresh()
        try:
            online_status = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//span[@title='Çevrimiçi ({numara})']")))
            if online_status:
                if online_start_time is None:
                    online_start_time = datetime.now()
        except:
            if online_start_time is not None:
                online_end_time = datetime.now()
                online_duration = online_end_time - online_start_time
                with open('kayit.txt', 'a') as file:
                    file.write(f"Çevrimiçi kaldığı süre: {online_duration}\n")
                online_start_time = None

        time.sleep(2)
check_online_status()
