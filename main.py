import pyautogui
import cv2
import numpy as np
import time

who = "ENTER EMAIL ADRESS"
subject = "ENTER TITLE"
text = "ENTER TEXT"
repeat = 10

w, h = pyautogui.size()
x, y = pyautogui.position()

def findImage(path):
    template = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

    mx = cv2.minMaxLoc(result)[3][0]
    my = cv2.minMaxLoc(result)[3][1]
    return mx, my, cv2.minMaxLoc(result)[0]

for i in range(repeat):
    print()
    compose = findImage("compose.png")
    pyautogui.moveTo(compose[0]+50, compose[1]+50)
    pyautogui.click()
    print("composed email")

    time.sleep(0.1)

    email = findImage("email.png")
    pyautogui.moveTo(email[0]+40, email[1]+60)
    pyautogui.click()
    pyautogui.click()
    pyautogui.typewrite(list(who), 0)
    print("typed WHO")

    pyautogui.moveTo(email[0]+20, email[1]+100)
    pyautogui.click()
    pyautogui.click()
    pyautogui.typewrite(list(subject), 0)
    print("typed SUBJECT")

    pyautogui.moveTo(email[0]+20, email[1]+150)
    pyautogui.click()
    pyautogui.click()
    pyautogui.typewrite(list(text), 0)
    print("typed TEXT")

    send = findImage("send.png")
    pyautogui.moveTo(send[0]+20, send[1]+20)
    pyautogui.click()
    print("sent")