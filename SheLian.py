from PIL import Image
import pytesseract
import pyautogui as p
import time as t
import keyboard

pytesseract.pytesseract.tesseract_cmd = r"B:\OCR\tesseract.exe"

refreshCount = 0

def breakGame():
    if keyboard.is_pressed("x"):
        exit()

def slidMouse(leftX=0, leftY=0, rightX=0, rightY=0):
    p.moveTo(leftX, leftY)
    p.dragTo(rightX, rightY, 0.5, button="left")

def changeMode():
    slidMouse(775, 433, 667, 426)

def changeEnv():
    slidMouse(775, 586, 667, 586)

def changeMod():
    slidMouse(775, 726, 667, 726)

def refresh():
    for i in range(2):
        t.sleep(0.1)
        p.click(1055, 251)
        t.sleep(0.2)
        p.click(1128, 576)
        t.sleep(0.1)
    print("Its time to refresh.")
    # global refreshCount
    # refreshCount += 1

img = Image.open("./SheLianImg/1.PNG")
test = pytesseract.image_to_string(img, lang='chi_tra')

def test():
    global refreshCount
    while 1:
        if refreshCount > 2:
            break
        # 如果找到T1 不打 -> T1 往右移動一次 如果>9 refresh
        if p.locateOnScreen("B:/Python/PythonPrac/GUI/SheLianImg/defence.PNG", confidence=0.8) != None or p.locateOnScreen("B:/Python/PythonPrac/GUI/SheLianImg/deliver.PNG", confidence=0.8) != None:
            count = 0
            while 1:
                print("更改試煉模式! %d" % count)
                changeMode()
                count += 1
                if p.locateOnScreen("B:/Python/PythonPrac/GUI/SheLianImg/defence.PNG", confidence=0.8) == None and p.locateOnScreen("B:/Python/PythonPrac/GUI/SheLianImg/deliver.PNG", confidence=0.8) == None:
                    break
                if count > 8:
                    refresh()
                    break
        elif p.locateOnScreen("B:/Python/PythonPrac/GUI/SheLianImg/dawu.PNG", confidence=0.8) != None:
            while 1:
                print("更改試煉環境!")
                changeEnv()
                if p.locateOnScreen("B:/Python/PythonPrac/GUI/SheLianImg/dawu.PNG", confidence=0.8) == None:
                    break
        elif p.locateOnScreen("B:/Python/PythonPrac/GUI/SheLianImg/dodgeIncreased.PNG", confidence=1) != None or p.locateOnScreen("B:/Python/PythonPrac/GUI/SheLianImg/cantHitGainLife.PNG", confidence=1) != None:
            count = 0
            while 1:
                print("更改試煉詞綴!")
                changeMod()
                count += 1
                if p.locateOnScreen("B:/Python/PythonPrac/GUI/SheLianImg/dodgeIncreased.PNG", confidence=0.8) == None and p.locateOnScreen("B:/Python/PythonPrac/GUI/SheLianImg/cantHitGainLife.PNG", confidence=0.8) == None:
                    break
                if count > 5:
                    refresh()
                    break
        elif p.locateOnScreen("B:/Python/PythonPrac/GUI/SheLianImg/go.PNG", confidence=0.8) != None:
                x, y = p.locateCenterOnScreen("B:/Python/PythonPrac/GUI/SheLianImg/go.PNG", confidence=0.8)
                p.click(x, y)
                print("GOGOGO")
        elif p.locateOnScreen("B:/Python/PythonPrac/GUI/SheLianImg/V.PNG", confidence=0.8) != None or p.locateOnScreen("B:/Python/PythonPrac/GUI/SheLianImg/question.PNG", confidence=0.8) != None:
            for i in range(5):
                t.sleep(0.1)
                p.click(1335, 748)
            while 1:
                if p.locateOnScreen("B:/Python/PythonPrac/GUI/SheLianImg/ok.PNG", confidence=0.8) != None:
                    x, y = p.locateCenterOnScreen("B:/Python/PythonPrac/GUI/SheLianImg/ok.PNG", confidence=0.8)
                    p.click(x, y)
                    print("OK")
                    break
            while 1:
                if p.locateOnScreen("B:/Python/PythonPrac/GUI/SheLianImg/EndGameGo.PNG", confidence=0.8) != None:
                    x, y = p.locateCenterOnScreen("B:/Python/PythonPrac/GUI/SheLianImg/EndGameGo.PNG", confidence=0.8)
                    p.click(x, y)
                    print("GOGOGO")
                    break
            refreshCount = 0
            print("end step.")
            t.sleep(8)

        t.sleep(0.2)


def testGUI():
    while 1:
        t.sleep(0.1)
        if p.locateOnScreen("B:/Python/PythonPrac/GUI/SheLianImg/EndGameGo.PNG", confidence=0.8) != None:
            print("find it")
        else:
            print("xdont find")
# testGUI()
test()
# print(p.position())
# p.moveTo(1335, 748)
# refresh()
