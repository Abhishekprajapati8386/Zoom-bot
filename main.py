print('Loading...')
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
from os import system
from keyboard import is_pressed
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
system('cls')
print('Loaded Zoom Bot')

meetingID =  input("Enter Meeting ID: ")    
if len(meetingID) == 0:
    meetingID = defualt[0]
meetingPasscode = input("Enter Meeting Passcode: ")
if len(meetingPasscode) == 0:
    meetingPasscode = defualt[1]
numberOfBots = int(input('Bot(s) Number: '))
customName = input('Name(Leave a blank for Random name): ')
system('cls')
f = []
f = open('names.txt', 'r').read()
f = f.split('\n')
baseName = random.choice(f)
drivers = []
options = Options()
options.add_argument('--log-level=3') #Disable Log
options.add_argument("--disable-infobars") #Disable anoying info
options.add_argument("start-maximized") #Maximize when opened
options.add_argument("--disable-extensions") #Disable antivirus to make it broken

options.add_experimental_option("prefs", {
   \
   "profile.default_content_setting_values.media_stream_mic": 2,
   "profile.default_content_setting_values.media_stream_camera": 2
})
options.add_argument("--mute-audio") #Mute all tabs(Else if you had 2 bots or more, It will broke your pc :o)
options.add_argument("--headless") 
for i in range(numberOfBots):
    baseName = random.choice(f)
    print('Please ignore the warning!')
    drivers.append(webdriver.Chrome(executable_path='chromedriver.exe', options=options))
    drivers[i].get(f'https://us05web.zoom.us/join')
    system('cls')
    print('Please ignore the warning!\nMay take long time to complete.\n')
    try:
        drivers[i].find_element(by="id", value="mic-icon").click()
        sleep(1.25)
        drivers[i].find_element(by="id", value="video-icon").click()
    except:
        pass
    drivers[i].find_element(by="name", value="join-confno").send_keys(meetingID)
    drivers[i].find_element(by="id", value="btnSubmit").click()
    drivers[i].execute_script("window.scrollBy(0, 100);")
    sleep(3)
    drivers[i].find_element(By.XPATH, "//*[contains(text(), '{}')]".format("Join from Your Browser")).click()
    sleep(3)
    drivers[i].find_element(by="id", value="input-for-pwd").send_keys(meetingPasscode)
    drivers[i].find_element(by="id", value="input-for-name").send_keys(baseName)
    button = drivers[i].find_element(By.CLASS_NAME, "preview-join-button")
    sleep(3)
    drivers[i].find_element(by="id", value="preview-audio-control-button").click()
    sleep(4)
    drivers[i].find_elements(by=By.CLASS_NAME, value="preview-join-button")[0].click()
print('All bot(s) is joined!\nPress Alt+Ctrl+Shift+E to Exit all bots')

#Waiting for user to quit bot(s)

while True:
    if is_pressed('alt') and is_pressed('ctrl') and is_pressed('shift') and is_pressed('e') or is_pressed('E'):
        system('cls')
        for i in range(numberOfBots):
            print(f'Exiting Bot Number {i+1}')
            sleep(0.075)
            drivers[i].close()
        system('pause')
        print('If Auto Exit not working,\nPlease Exit by your self!')
        quit() 