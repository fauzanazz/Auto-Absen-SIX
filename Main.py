from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from datetime import *

def opentab():
    newlink = link.get_attribute('data-url')
    driver.switch_to.new_window('tab')
    driver.get(f'https://akademik.itb.ac.id/{newlink}')
    

# Mengetahui hari apa dan batasan waktu
HariIni = date.today()
found = False
while found == False:
    if HariIni >= date(2022, 11, 28):
        date = '2022-11-27'
        x = datetime.strptime(date, '%Y-%m-%d').date()
        found = True
    else:
        datetime.now() - timedelta(days=7)

# Open Chrome
driver = webdriver.Chrome()

# Login
driver.get('https://akademik.itb.ac.id/app/K/mahasiswa:19622236+2022-1/kelas/jadwal/mahasiswa')

title = driver.title

# If Login or not
if title == "Login | SIX":
    login = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/a")
    driver.execute_script("arguments[0].click();", login)

    Username = driver.find_element(By.NAME, "username")
    Username.send_keys('Username SIX')
    
    Password = driver.find_element(By.NAME, "password")
    Password.send_keys('Password SIX')

    submit_button = driver.find_element(By.NAME, "submit")
    submit_button.click()
    driver.implicitly_wait(10)
    
# Absen
selisih = HariIni - x
# column = (selisih.days // 7) + 1
# row = selisih.days % 7

# Debug karena belum ada absensi
# ---------------------
column = 1
row = 1
# ---------------------

available = len(driver.find_elements(By.XPATH,f"/html/body/div/div[2]/div/table/tbody/tr[{column}]/td[{row}]/div[2]"))
if available != 1:
    for i in range (available):
        link = driver.find_element(By.XPATH, f"/html/body/div/div[2]/div/table/tbody/tr[{column}]/td[{row}]/div[2]/div[{i+1}]/a")
        opentab()
        #Tandai Hadir
        #Belum diketahui harus ada absensinya terlebih dahulu
    
else:
    link = driver.find_element(By.XPATH, f"/html/body/div/div[2]/div/table/tbody/tr[{column}]/td[{row}]/div[2]/div/a")
    opentab()

#Tandai Hadir
#Belum diketahui harus ada absensinya terlebih dahulu (Tandai Hadir dapat dimasukkan pada fungsi opentab!)

#Delay
driver.implicitly_wait(10)

#Quit

driver.quit()
