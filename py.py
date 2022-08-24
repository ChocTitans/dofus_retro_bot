from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import cv2



def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def click2():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.02)

# ougi (125, 115,  81)
# ougi2 (237, 156,  22)
# ougi 3 (249, 235, 213)
# corbac ( 82,  77,  98)
# corbac lumineux 221, 211, 185)


def ig():
    ig = pyautogui.locateCenterOnScreen('ig.png', confidence=0.60)
    if ig is not None:
        return True
    else:
        return False

def ready():
    ready = pyautogui.locateCenterOnScreen('ready.png', confidence=0.60)

    if ready is not None:
        pyautogui.moveTo(ready)
        click2()
        return True
    else:
        return False

def bug_pass():
    bug = pyautogui.locateCenterOnScreen('bugpass.png', confidence=0.60)
    if bug is not None:
        pyautogui.moveTo(250,45)
        return

def big_function():
    time.sleep(0.5)
    research=0 
    while keyboard.is_pressed('q') == False:
                
        if ready() == True:
            return
        elif ig() == True:
            return
        
        pic = pyautogui.screenshot(region=(250,45,1100,640))

        width, height = pic.size
    
        for x in range(0, width, 5):
            for y in range(0, height, 5):

                r, g, b = pic.getpixel((x, y))

                if b == 81 and r == 125 and g == 115:
                    pyautogui.keyDown("shift")
                    click(x+250, y+45)
                    click(x+250, y+45)
                    pyautogui.keyUp("shift")
                    ready()
                    bug_pass()                        
                    return
                elif b == 98 and r == 82 and g == 77:
                    pyautogui.keyDown("shift")
                    click(x+250, y+45)
                    click(x+250, y+45)
                    pyautogui.keyUp("shift")
                    ready()
                    bug_pass()                        
                    return
                elif b == 98 and r == 237 and g == 156:
                    pyautogui.keyDown("shift")
                    click(x+250, y+45)
                    click(x+250, y+45)
                    pyautogui.keyUp("shift")
                    ready()
                    bug_pass()                        
                    return
                elif b == 213 and r == 249 and g == 235:
                    pyautogui.keyDown("shift")
                    click(x+250, y+45)
                    click(x+250, y+45)
                    pyautogui.keyUp("shift")
                    ready()
                    bug_pass()                        
                    return
                elif b == 185 and r == 221 and g == 211:
                    pyautogui.keyDown("shift")
                    click(x+250, y+45)
                    click(x+250, y+45)
                    pyautogui.keyUp("shift")
                    ready()
                    bug_pass()                        
                    return
                elif b == 66 and r == 193 and g == 145: # (193, 145,  66) ougibotte
                    pyautogui.keyDown("shift")
                    click(x+250, y+45)
                    click(x+250, y+45)
                    pyautogui.keyUp("shift")
                    ready()
                    bug_pass()                        
                    return
            research+=1
        print(research)
        if research >= 2200:
            time.sleep(2)
            chat = pyautogui.locateCenterOnScreen('chat.png', confidence=0.70)
            if chat is not None:
                click(x+250, y+45)
                pyautogui.write('.movemobs')
                time.sleep(0.3)
                pyautogui.keyDown("enter")
                time.sleep(0.3)
                pyautogui.keyUp("enter")







def combat():
    flesh = pyautogui.locateCenterOnScreen('flesh.png', confidence=0.70)
    eye = pyautogui.locateCenterOnScreen('eye.png', confidence=0.70)
    #echec = pyautogui.locateCenterOnScreen('echec.png', confidence=0.70)

    for i in range(2):
        time.sleep(1.3)
        if ig() == False:
            return
        else:
            if flesh is not None:
                pyautogui.moveTo(flesh)
                click2()
                time.sleep(0.3)

                pyautogui.moveTo(690,437)
                click2()
                time.sleep(0.3)

    bug_pass()


    if ig() == False:
        return
    else:
        if eye is not None:
            pyautogui.moveTo(eye)
            click2()
            time.sleep(0.3)

            pyautogui.moveTo(690,437)
            click2()
            time.sleep(0.3)

    bug_pass()


def checklevelup():
    levelup = pyautogui.locateCenterOnScreen('ok.png', confidence=0.70)
    if levelup is not None:
        pyautogui.moveTo(levelup)
        click2()
        return





while True:
    big_function()
    combat()
    checklevelup()
