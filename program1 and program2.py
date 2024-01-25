# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jUipz9U7eiely17tU4nPo-lbFOPowmGd
"""

n=4
for i in range(0,n):
  for j in range(0,i+1):
    print("*", end="")
  print()
cnt=1
for k in range(0,n):
    print(cnt*" "+"*" * (n-cnt), end="")
    cnt+=1
    print()

# Commented out IPython magic to ensure Python compatibility.
# %%shell
# cat > /etc/apt/sources.list.d/debian.list <<'EOF'
# deb [arch=amd64 signed-by=/usr/share/keyrings/debian-buster.gpg] http://deb.debian.org/debian buster main
# deb [arch=amd64 signed-by=/usr/share/keyrings/debian-buster-updates.gpg] http://deb.debian.org/debian buster-updates main
# deb [arch=amd64 signed-by=/usr/share/keyrings/debian-security-buster.gpg] http://deb.debian.org/debian-security buster/updates main
# EOF
# 
# # Add keys
# apt-key adv --keyserver keyserver.ubuntu.com --recv-keys DCC9EFBF77E11517
# apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 648ACFD622F3D138
# apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 112695A0E562B32A
# 
# apt-key export 77E11517 | gpg --dearmour -o /usr/share/keyrings/debian-buster.gpg
# apt-key export 22F3D138 | gpg --dearmour -o /usr/share/keyrings/debian-buster-updates.gpg
# apt-key export E562B32A | gpg --dearmour -o /usr/share/keyrings/debian-security-buster.gpg
# 
# # Prefer debian repo for chromium* packages only
# # Note the double-blank lines between entries
# cat > /etc/apt/preferences.d/chromium.pref << 'EOF'
# Package: *
# Pin: release a=eoan
# Pin-Priority: 500
# 
# 
# Package: *
# Pin: origin "deb.debian.org"
# Pin-Priority: 300
# 
# 
# Package: chromium*
# Pin: origin "deb.debian.org"
# Pin-Priority: 700
# EOF
# 
# # Install chromium and chromium-driver
# apt-get update
# apt-get install chromium chromium-driver
# 
# # Install selenium
# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.headless = True

driver.page_source

driver

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.flightradar24.com/data/pnq/")
elist = driver.find_elements(By.XPATH("//a[@href='https://www.flightradar24.com/data/airports/pnq/arrivals']"))
elist[0].click()
driver.implicitly_wait(120)
places=['Bangalore','Delhi','Goa','Chandigarh','Dubai','Hyderabad','Nagpur','Dubai']
tablerows = driver.find_elements(By.XPATH("//table[@class='table table-condensed']/tbody/tr"))
if len(tablerows)==0:
  print("There is no data present in UI. please find screenshot for more details")
  driver.save_screenshot("error.png")
  exit
for row in tablerows:
  output = row.text.split(',')
  if output[2] in str(places):
    print(output[2]+":"+output[5])
  else:
    pass