import time
import pyautogui as p
import keyboard
import time
from datetime import datetime


# import pygame
def slidMouse(leftX=0, leftY=0, rightX=0, rightY=0):
    p.moveTo(leftX, leftY)
    p.dragTo(rightX, rightY, 0.5, button="left")

def startTrail():
    time.sleep(1)
    p.click(1051, 289)
    slidMouse(894, 427, 998, 427)
    time.sleep(0.5)
    p.click(894, 736)

def endGameStep():
    for i in range(20):
        breakGame()
        time.sleep(0.3)
        # 確認按鈕位置
        p.click(1335, 748)
    p.click(1262, 297)


def turnOnTheSkill():
    tupleX = (1455, 1414, 1388, 1394, 1410, 1454)
    tupleY = (365, 441, 522, 616, 689, 768)

    for i in range(len(tupleX)):
        p.click(tupleX[i], tupleY[i])
        time.sleep(0.1)

def reloadWhileDie():
    while True:
        time.sleep(0.2)


        imgLocate = p.locateOnScreen("B:/Python/PythonPrac/GUI/giveUp.png", confidence=0.8)

        if imgLocate != None:
            for i in range(10):
                time.sleep(0.1)
                p.click(imgLocate[0] + imgLocate[2] / 2, imgLocate[1] + imgLocate[3] / 2)

            time.sleep(7)
            p.click(1329, 785)
            time.sleep(3)
            turnOnTheSkill()

            break
        else:
            print("Give Up Image Not found!!!")





# while True:
#     p.doubleClick(650, 200)
#     time.sleep(0.5)



# move the mouse to (x, y, duration)
# p.moveTo(600, 600, 1.2)

# 拖曳屬標至(x, y, duration, button)
# p.dragTo(700, 700, 2, button="left")


# p.doubleClick()
# startTrail()

# region=(1204, 540, 1449, 808)
# img = p.screenshot()
# img.save(r"B:\Python\PythonPrac\GUI\image.png")
# p.hotkey("altleft", "tab")

start = datetime.now()
end = datetime.now()

def printUsedTime():
    end = datetime.now()
    print("Used time: %s." % (end - start))
# print(imgLocate)
# endGameStep()
# reloadWhileDie()
def breakGame():
    if keyboard.is_pressed("x"):
        end = datetime.now()
        print("Used time: %s." % (end - start))
        exit()

def startOnThGuaGiFunc(cnt=30):
    # 如果有200樓標示  startTrail()
    # 沒事就按endGameStep()
    # 死掉  reloadWhileDie()

    # 計算使用時間 -> 開始
    start = datetime.now()
    print(start)
    n = 1 #rush
    m = 1 #die
    while True:

        time.sleep(0.1)

        breakGame()

        if p.locateOnScreen("B:/Python/PythonPrac/GUI/giveUp.png", confidence=0.9) != None:
            reloadWhileDie()
            print("im die. --%s" % m)
            printUsedTime()
            m += 1
        elif p.locateOnScreen("B:/Python/PythonPrac/GUI/timeToStartGame.png", confidence=0.9) != None:
            startTrail()
            print("Start Next Game. --%s" % n)
            printUsedTime()
            n += 1
            # if n > 40:
            #     exit()
        elif p.locateOnScreen("B:/Python/PythonPrac/GUI/restart1.png", confidence=0.8) != None or p.locateOnScreen("B:/Python/PythonPrac/GUI/resrart.png", confidence=0.8) != None:
            p.click(915, 651)
            time.sleep(3)
            turnOnTheSkill()

        elif p.locateOnScreen("B:/Python/PythonPrac/GUI/success.png", confidence=0.9) != None:
            endGameStep()
            time.sleep(2)
        else:
            endGameStep()
            time.sleep(3)

        if n < cnt:
            break

def testGUI():
    for i in range(10):
        time.sleep(0.1)
        if p.locateOnScreen("B:/Python/PythonPrac/GUI/restart1.png", confidence=0.8) != None or p.locateOnScreen("B:/Python/PythonPrac/GUI/resrart.png", confidence=0.8) != None:
            print("find it")
        else:
            print("xdont find")

# while True:
#     else:
#         print("sdfsdf")
# testGUI()
# print(p.position())


# startOnThGuaGiFunc(2)
# turnOnTheSkill()

# reloadWhileDie()
# p.click(1329, 785)

# 計算使用時間 -> 結束

# SCREEN POSITION LEFT TOP ->　(x=367, y=203)
# SCREEN POSITION RIGHT BOT ->　(x=1504, y=844)


