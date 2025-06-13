import win32api, win32gui, win32con, win32ui, win32process
import time, smtplib, ssl, os, signal, sys, traceback
import pyscreeze as gui, numpy as np, pytesseract as ocr, cv2, pyautogui
from ctypes import windll
from contextlib import contextmanager

gui.USE_IMAGE_NOT_FOUND_EXCEPTION = False
                    
class Window:
    
    def __init__(self, windowName, enabledClassName, imgLibPath, version, partial = False, cycle=0):
        self.wn = windowName
        self.ecn = enabledClassName
        self.path = imgLibPath
        self.vspath = ''
        self.version = version
        self.cycle = cycle
        
        def findHwndWithPartialWindowName(partialName):
            top_windows = []
            win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd), top_windows)
            for hwnd in top_windows:
                if partialName in win32gui.GetWindowText(hwnd):
                    return hwnd
            return 0
        
        if partial == False:
            self.hwnd = win32gui.FindWindow(None, self.wn)
        elif partial == True:
            self.hwnd = findHwndWithPartialWindowName(self.wn)
        
        self.threadID, self.PID = win32process.GetWindowThreadProcessId(self.hwnd)
        
        self.EXCLAMATION = [self.path + "exclamation0.png", self.path + "exclamation1(small).png", self.path + "exclamation2.png", self.path + "exclamation3.png", self.path + "exclamation4.png", 
               self.path + "exclamation5(small).png", self.path + "exclamation6(small).png", self.path + "exclamation7(verySmall).png", self.path + "exclamation8.png", self.path + "exclamation9.png", self.path + "exclamation10.png"]
        self.LEAVE_DOOR = [self.path + "leaveDoor0.png", self.path + "leaveDoor1.png"]

        #Take monitor resolution into account-- Another Eden is at 1920x1080. Current set for 1920x1200
        self.MONITOR_Y = 0
        
        self.VK_CODE = {'0':0x30,
                        '1':0x31,
                        '2':0x32,
                        '3':0x33,
                        '4':0x34,
                        '5':0x35,
                        '6':0x36,
                        '7':0x37,
                        '8':0x38,
                        '9':0x39,
                        'a':0x41,
                        'b':0x42,
                        'c':0x43,
                        'd':0x44,
                        'e':0x45,
                        'f':0x46,
                        'g':0x47,
                        'h':0x48,
                        'i':0x49,
                        'j':0x4A,
                        'k':0x4B,
                        'l':0x4C,
                        'm':0x4D,
                        'n':0x4E,
                        'o':0x4F,
                        'p':0x50,
                        'q':0x51,
                        'r':0x52,
                        's':0x53,
                        't':0x54,
                        'u':0x55,
                        'v':0x56,
                        'w':0x57,
                        'x':0x58,
                        'y':0x59,
                        'z':0x5A,
                        'f11':0x7A,
                        'f2':0x71,
                        'enter':0x0D}
        
        print(self.hwnd, end=' ')
        print("parent")
        print(self.PID)
        
        if self.version == "gl":
            self.vspath = self.path + "gl\\"
        elif self.version == "jp":
            self.vspath = self.path + "jp\\"
        elif self.version is None:
            pass
        else:
            raise Exception("Invalid version")
        
        if self.hwnd != 0:
            win32gui.EnumChildWindows(self.hwnd, Window.findChildren, self)
            #win32gui.EnableWindow(self.hwnd, False)
            #win32gui.SetForegroundWindow(self.hwnd)
            #win32gui.EnableWindow(self.hwnd, True)

    def findChildren(hwnd, self):

        className = win32gui.GetClassName(hwnd)
        hwnds = []

        self.hwnd = hwnd
            
        try: 
            dlgID = win32gui.GetDlgCtrlID(hwnd) 
        except: 
            dlgID = "None"
        try: 
            dlgText = win32gui.GetDlgItemText(hwnd, dlgID) 
        except: 
            dlgText = "None"
        try: 
            winText = win32gui.GetWindowText(hwnd) 
        except: 
            winText = "None"
        
        print(f"{hwnd:10} {className:20} {dlgID:5} {dlgText:20} {winText:20}")

        if className == self.ecn:
            
            if self.cycle == 0:
                print(str(self.hwnd) + " THIS IS ITTT")
                return False 
            else:
                self.cycle -= 1
                print("Right name, wrong level....")
            
    @contextmanager
    def gdi_resource_management(self, hwnd):
        # Acquire resources
        hwnd_dc = win32gui.GetWindowDC(hwnd)
        mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
        save_dc = mfc_dc.CreateCompatibleDC()
        bitmap = win32ui.CreateBitmap()
        
        try:
            yield hwnd_dc, mfc_dc, save_dc, bitmap
        finally:
            # Ensure resources are released
            win32gui.DeleteObject(bitmap.GetHandle())
            save_dc.DeleteDC()
            mfc_dc.DeleteDC()
            win32gui.ReleaseDC(hwnd, hwnd_dc)
    
    def screenshot(self, imageFilename=None, region=None):
        
        windll.user32.SetProcessDPIAware()
        
        if imageFilename == None:
            imageFilename = self.vspath+"out.bmp"
        
        left, top, right, bottom = win32gui.GetClientRect(self.hwnd)
        w = right - left
        h = bottom - top
        x = 0
        y = 0
        
        if region is not None:
            assert len(region) == 4, 'region argument must be a tuple of four ints'
            x = region[0]
            y = region[1]
            w = region[2]
            h = region[3]
    
        im = imageFilename
    
        with self.gdi_resource_management(self.hwnd) as (hwnd_dc, mfc_dc, save_dc, bitmap):
            bitmap.CreateCompatibleBitmap(mfc_dc, w, h)
            save_dc.SelectObject(bitmap)

            result = windll.user32.PrintWindow(self.hwnd, save_dc.GetSafeHdc(), 3)

            if not result:
                raise RuntimeError(f"Unable to acquire screenshot! Result: {result}")
            
            bmpinfo = bitmap.GetInfo()
            bmpstr = bitmap.GetBitmapBits(True)

        img = np.frombuffer(bmpstr, dtype=np.uint8).reshape((bmpinfo["bmHeight"], bmpinfo["bmWidth"], 4))
        img = np.ascontiguousarray(img)[..., :-1]  # make image C_CONTIGUOUS and drop alpha channel

        cv2.imwrite(im, img)
        
        return im
        
    def locateOnScreen(self, image, **kwargs):
        gui.screenshot = self.screenshot
        retVal = gui.locateOnScreen(image, **kwargs)
        #print(retVal)
        return retVal 
        
    def click(self, x, y, times=1, delay=0.5, post=False, errorLogging=False):
       
        lParam = win32api.MAKELONG(x, y)

        for _ in range(times):
            
            if post == False:
                win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, 0, lParam)
                win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, lParam)
            elif post == True:
                win32api.PostMessage(self.hwnd, win32con.WM_LBUTTONDOWN, 0, lParam)
                win32api.PostMessage(self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, lParam)
                
            time.sleep(delay)
            
            if errorLogging == True:
                print("clicked at (", end='')
                print(x, end=", ")
                print(y, end=") ")
                print(times, end=' ')
                print("times with a delay of", end=' ')
                print(delay, end=' ')
                print("secounds!")
                
        #pyautogui.click(x, y, times, delay) 
        
    def clickBomb(self, x1=300, x2=1620, endPic=None, errorLogging=False):
        
        if endPic == None:
            endPic = self.path + "menu.png"
        
        time.sleep(0.5)
        print("CLIIIIIIIIIIIIIIIIIIIIIICK BOOOOOOOOOOOOOOOOOOOOOOOMMMMMMMMB!")
        for x in range(x1, x2, 80):
            for y in range(400, 680, 80):
                if errorLogging == True:
                    print(str(x) + ', ' + str(y))
                self.click(x, y, delay=0.1)
        self.waitFor(endPic, clickUntil=True)
        
    def press(self, key, times=1, delay=0.3, post=False, errorLogging=False):
    
        for _ in range(times):
            
            if post == False:
                win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, self.VK_CODE[key], 0)
                win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, self.VK_CODE[key], 0)
            elif post == True:
                win32api.PostMessage(self.hwnd, win32con.WM_KEYDOWN, self.VK_CODE[key], 0)
                win32api.PostMessage(self.hwnd, win32con.WM_KEYUP, self.VK_CODE[key], 0)
                
            time.sleep(delay)
            
            if errorLogging == True:
                print("Pressed the ", end='')
                print(key, end=" key ")
                print(times, end=" times with a delay of ")
                print(delay, end=" secounds.\n")
                    
    def drag(self, direction, duration, battleStrat=None, errorLogging=False, lag=True, battleMode=False, timeFactor=10, sx=500, sy=400, dx=500, dy=500):
    
        if errorLogging == True:
            print("Dragging", end=' ')
            print(direction, end=" for ")
            print(duration, end=" secounds.\n")
            
        x = sx
        y = sy
        
        lParam = win32api.MAKELONG(x, y)
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, 0, lParam)
        
        if direction == "left":
            x -= dx
        elif direction == "right":
            x += dx
        elif direction == "up":
            y -= dy
        elif direction == "down":
            y += dy
        
        lParam = win32api.MAKELONG(x, y)
        win32api.SendMessage(self.hwnd, win32con.WM_MOUSEMOVE, win32con.MK_LBUTTON, lParam)
        
        if battleMode == True:
            encounter = False
            start = time.time()
            times = []
            
            while (time.time() - start) < (duration):
            
                currentTime = time.time() - start
                currentSecond = round(currentTime, 0)
                times.append(currentSecond)
                
                if len(times) == 0:
                    print("0")
                
                elif times[len(times)-1] != times[len(times)-2]:
                    print(currentSecond)    
                    
                fight = self.locateOnScreen(self.vspath + "attackButton.png", confidence=0.8)
                
                if fight:
                    currentTime = time.time()-start
                    encounter = True
                    win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, 0, lParam)
                    battleStrat()
                    
                    if lag == False:
                        if currentTime < timeFactor:
                            if errorLogging == True:
                                print("No correction needed.")
                        elif currentTime >= timeFactor:
                            
                            self.drag(direction, (duration+timeFactor)-currentTime, battleStrat=battleStrat, timeFactor=timeFactor, errorLogging=True, battleMode=True) 
                                
            win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, 0, lParam)
            
            while (time.time() - start) > duration and (time.time() - start) < (duration + timeFactor):
            
                currentTime = time.time() - start
                currentSecond = round(currentTime, 0)
                times.append(currentSecond)
                
                if len(times) == 0:
                    print("0")
                
                elif times[len(times)-1] != times[len(times)-2]:
                    print(currentSecond)
                    
                fight = self.locateOnScreen(self.vspath + "attackButton.png", confidence=0.8)
                
                if fight:
                   encounter = True
                   battleStrat()
                   
                   if lag == False:
                        if currentTime >= duration+timeFactor:
                            if errorLogging == True:
                                print("No correction needed.")
                        else:
                            self.drag(direction, (duration+timeFactor)-currentTime, battleStrat=battleStrat, timeFactor=timeFactor, errorLogging=errorLogging, battleMode=True)
                            
            return encounter
            
        else:
        
            time.sleep(duration)
            win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, 0, lParam)
            
            return False
            
    def waitFor(self, image, timeout=-1, confidence=0.8, grayscale=True, clickUntil=False, doClick=False, errorLogging=False, clickx = 500, clicky = 500, delay=0.5, region=None, timeConst=120):
        
        TIMEOUT = False
        start = time.time()
        times = []
        
        if errorLogging == True:
            print("Waiting for ", end='')
            print(image)
        
        while True:
        
            if errorLogging == True:
            
                currentTime = time.time() - start
                currentSecond = round(currentTime, 0)
                times.append(currentSecond)
                
                if len(times) == 0:
                    print("0")
                
                elif times[len(times)-1] != times[len(times)-2]:
                    print(currentSecond)
                
            if clickUntil == True:
                self.click(clickx, clicky, delay=delay, errorLogging=errorLogging)
            
            event = self.locateOnScreen(image, confidence=confidence, grayscale=grayscale, region=region)
            
            if event: 
                TIMEOUT = False
                if errorLogging == True:
                    print("Done.")
                
                eventCoords = gui.center(event)
                
                if doClick == True:
                    self.click(eventCoords.x, eventCoords.y, delay=1, errorLogging=errorLogging)
                    
                return TIMEOUT, eventCoords
            if timeConst >= 100:    
                if (time.time() - start) > timeConst:
                    self.notify("Subject: Something, " + image.replace(self.path, '') + ", Went Wrong-- Taking way too long")
                    quit()
            
                
            if timeout == -1:
                continue
            
            elif time.time()-start > timeout:
                if errorLogging == True:
                    print("Times up for " + image.replace(self.path, '') + "!!!")
                TIMEOUT = True
                eventCoords = None
                
                return TIMEOUT, eventCoords            
    
    def img2text(self, language, config, region=None):

        img = self.screenshot(region=region)
        text = ocr.image_to_string(img, language, config=config)
        numText = ''
        for i in text:
            if i.isdigit():
                numText = numText + i
        if numText == '':
            numText = '0'
        number = int(numText)
        return number
        
    def compareImages(self, img1, img2, simThreshold=0.90):
        
        simPercent = 0
        simList = []
        
        im1 = cv2.imread(img1)
        im2 = cv2.imread(img2)
        
        im1 = np.linalg.norm(im1)
        im2 = np.linalg.norm(im2)
        
        if im1 < im2:
            simPercent = im1/im2
        elif im2 < im1:
            simPercent = im2/im1

        #print(simPercent)

        if simPercent >= simThreshold:
            #print("images are simular")
            return True
        else:
            #print("images are not simular!")
            return False
            
    def wlog(self, message):
        print(message)

class AEWindow(Window):
    
    def battle(self, *args, finalDirection="right", errorLogging=False, battleLimit=5,):
        
        battleNum = 0
        
        start = time.time()
        
        while True:
            
            self.drag("left", 3)
            self.drag("right", 3)
            
            battle = self.locateOnScreen(self.vspath + "attackButton.png", confidence=0.9, grayscale=True)
            
            if (time.time() - start) > 60:
                #notify("Subject: Something Went wrong: we are still looking for a battle!")
                self.wlog("Something Went wrong: we are still looking for a battle!")
            
            if battle:
                
                self.horror(*args)
                while True:
                    alive, coords = self.waitFor(self.vspath+"killConfirmed.png", timeout = 30, errorLogging=errorLogging)
                    if alive == True:
                        self.horror('g')
                    elif alive == False:
                        self.waitFor(self.path + "menu.png", clickUntil=True,  errorLogging=errorLogging)
                        start = time.time()
                        break
                        
                    
                battleNum += 1
                
                if errorLogging == True:
                    print("Battled ", end='')
                    print(battleNum, end=" times!\n")
                
            if battleNum == battleLimit:
                if errorLogging == True:
                    print("Job done!")
                break
        
        self.drag(finalDirection, 15)

    def horror(self, *args, timeConst=120):

        for key in args:
            if key == "pause":
                self.waitFor(self.vspath+"attackButton.png", timeConst=timeConst)
                continue
            elif key == "done":
                while True:
                    alive, deathCoords = self.waitFor(self.vspath+"killConfirmed.png", doClick=True, timeout = 25)
                    if alive == True:
                        self.press('g')
                    elif alive == False:
                        break
                time.sleep(1)
                self.waitFor(self.path+"menu.png", clickUntil=True) 
                continue
            self.press(key)        

    def goAgain(self, mapName, diff, mapNameList, mapIndex, innerMap=None):

        
        print("------------------------------------------LEGGO AGAIN!!!!------------------------------------------")
        
        time.sleep(3)
        noExclamation, exclamationCoords = self.waitFor(self.EXCLAMATION[0], doClick=True)
        
        mapa = self.vspath + "maps\\map_" + mapName + ".png"
        noMap, mapCoords = self.waitFor(mapa) 
        noTimeStop, timeStopCoords = self.waitFor(self.path + "timeStop.png", timeout=5)
        if noTimeStop == True:
            print("------------------------------------------UH-o!!!!!!------------------------------------------")
            loop, phase = self.whiteCard(mapName, innerMap, diff, mapNameList, mapIndex)
            return loop, phase
            
        self.waitFor(mapa, doClick=True)
        if innerMap is not None:
            self.waitFor(self.vspath + "maps\\map_" + innerMap + ".png", doClick=True)
            print("BOOYEAH")
            
        loop, phase = self.startDungeon(diff, mapNameList, mapIndex)
        return loop, phase
        
    def startDungeon(self, diff, mapNameList, mapIndex):
        
        if diff == "veryHard":
            self.waitFor(self.vspath + "veryHard.png", doClick=True, timeout=3)
        elif diff == "hard":
            self.waitFor(self.vspath + "hard.png", doClick=True)
            
        noButton, buttonCoords = self.waitFor(self.vspath + "letsgo.png", doClick=True, timeout=5)
        if noButton == True:
            print("No more red keys!")
            self.waitFor(self.vspath + "cancel.png", doClick=True)
            time.sleep(1)
            self.click(500, 500)
            time.sleep(1)
            self.click(1764, 105)
            time.sleep(1)
            self.waitFor(self.path + "xButton.png", doClick=True)
            self.waitFor(self.path + "menu.png")
            loop = False
            
            if mapIndex == len(mapNameList) - 1:
                self.terminate()
                print("Chesus")
                
            return loop, 0
        
        else:
            self.waitFor(self.path + "menu.png")
            phase = -1
            loop = True
            print(str(phase) + " >>>> time to start over!!!! >>>>")
            
            return loop, phase
            
    def terminate(self):
        
        if self.version == "jp":
            self.waitFor(self.path + "menu.png", doClick=True)
            self.waitFor(self.vspath + "settings.png", doClick=True)
            self.waitFor(self.vspath + "inGameDataTransfer.png", doClick=True)
            self.waitFor(self.vspath + "saveTransferData.png", doClick=True)
            self.waitFor(self.vspath + "go.png", doClick=True)
            self.waitFor(self.path + "ok.png", doClick=True)
            self.notify("Subject: JP Red Keys Gone!")
            os.kill(PID, signal.SIGTERM)
        elif self.version == "gl":
            self.notify("Subject: GL Red Key Runs Completed!")
            os.kill(self.PID, signal.SIGTERM)
        
    def notify(self, message):     
        
        print(message)

    def identifyRoomPCD(self, mapName, innerMapName, diff, mapNameList, mapIndex):
        
        def moveDungeon(mapName, innerMapName, diff, mapNameList, mapIndex):

            #phase = 0   #         0,         1,         2,         3,         4,         5,         6,         7,
            #duration  = [      1118,      1400,     0.822,       583,       962,     0.201,     1.165,       736,]
            #direction = [       304,       282,   "right",       308,       322,   "right",   "right",       258,]
            #isClick   = [   "click",   "click",     "n/a",   "click",   "click",     "n/a",     "n/a",   "click",]

            for _ in range(2):
                self.waitFor(self.EXCLAMATION[0], doClick=True)
                self.waitFor(self.path + "menu.png", clickUntil=True, clickx=1910, clicky=197)
            
            self.drag("right", 0.822)
            time.sleep(1)
            
            for _ in range(2):
                self.waitFor(self.EXCLAMATION[0], doClick=True)
                self.waitFor(self.path + "menu.png", clickUntil=True, clickx=1910, clicky=197)
            
            self.drag("right", 0.201)
            time.sleep(1)

            noExclamation, exclamationCoords = self.waitFor(self.EXCLAMATION[0], doClick=True, timeout=3)
                
            if noExclamation == False:
                self.notify("Subject: ChantBarddddd!!!!!!")
                self.wlog("CHANT BARD")
                
            self.waitFor(self.path + "menu.png", clickUntil=True, clickx=1910, clicky=197)

            
            self.drag("right", 1.165)
            self.drag("up", 1.5)
            self.waitFor(self.path + "menu.png", clickUntil=True)
            
            loop, phase = self.goAgain(mapName, diff, mapNameList, mapIndex, innerMap=innerMapName)
            
            return loop, phase
                
        def movePcdII():

            for _ in range(3):
                self.waitFor(self.EXCLAMATION[2], doClick=True)
                self.waitFor(self.path + "menu.png", clickUntil=True, clickx=1910, clicky=197)
                
            self.drag("left", 0.479)
            time.sleep(1)

            self.waitFor(self.EXCLAMATION[2], doClick=True)
            self.waitFor(self.path + "menu.png", clickUntil=True, clickx=1910, clicky=197)
            
            self.drag("left", 0.681)
            time.sleep(1)
            
            self.waitFor(self.EXCLAMATION[2], doClick=True)
            self.waitFor(self.path + "menu.png", clickUntil=True, clickx=1910, clicky=197)
            return True

        def movePcdIII():

            phase = 0   #         0,         1,         2,
            duration  = [     0.957,     0.408,     0.584,]
            direction = [    "left",    "left",    "left",]

            while True:
            
                self.drag(direction[phase], duration[phase])
                self.waitFor(self.path + "menu.png")
                
                if phase == 0:
                    self.waitFor(self.EXCLAMATION[4], doClick=True)
                    self.waitFor(self.path + "menu.png", clickUntil=True)
                    self.waitFor(self.EXCLAMATION[4], doClick=True)
                    self.waitFor(self.path + "menu.png", clickUntil=True)
                    self.waitFor(self.EXCLAMATION[4], doClick=True)
                    self.waitFor(self.path + "menu.png", clickUntil=True)
                elif phase == 1:
                    self.waitFor(self.EXCLAMATION[4], doClick=True, region=(960, 0, 960, 1910))
                    self.waitFor(self.path + "menu.png", clickUntil=True)
                elif phase == 2:
                    self.waitFor(self.EXCLAMATION[4], doClick=True)
                    self.waitFor(self.path + "menu.png")
                    return True
                    break
                phase += 1
                
        def movePcdIV():
            
            self.waitFor(self.EXCLAMATION[0], doClick=True)
            self.waitFor(self.path + "menu.png", clickUntil=True, clickx=1910, clicky=197)
            
            self.drag("right", 1)
            time.sleep(1)
            
            for _ in range(3):
                self.waitFor(self.EXCLAMATION[3], doClick=True)
                self.waitFor(self.path + "menu.png", clickUntil=True, clickx=1910, clicky=197)
                
            self.drag("right", 0.5)
            time.sleep(1)
            
            self.waitFor(self.EXCLAMATION[0], doClick=True)
            self.waitFor(self.path + "menu.png", clickUntil=True, clickx=1910, clicky=97)

            return True

        def movePcdV():
            
            for _ in range(3):
                self.waitFor(self.EXCLAMATION[3], doClick=True)
                self.waitFor(self.path + "menu.png", clickUntil=True, clickx=1910, clicky=197)
                
            self.drag("right", 0.5)
            time.sleep(1)
            
            self.waitFor(self.EXCLAMATION[3], doClick=True)
            self.waitFor(self.path + "menu.png", clickUntil=True, clickx=1910, clicky=197)

            return True
        
        def moveDummyTraining():

            phase = 0   #         0,         1,         2,         3,         4,
            duration  = [      0.56,       805,       463,     0.398,       492,]
            direction = [    "left",        67,        87,    "left",       152,]
            isClick   = [     "n/a",   "click",   "click",     "n/a",   "click",]


            while True:
            
                if isClick[phase] == "click":
                    time.sleep(1)
                    self.waitFor(self.EXCLAMATION[0], doClick=True)
                    self.waitFor(self.path + "menu.png", clickUntil=True)
                    
                else:
                    self.drag(direction[phase], duration[phase])
                    
                if phase == 4:
                    return True
                    break
                phase += 1

        def moveCatParadise():

            self.waitFor(self.EXCLAMATION[0], doClick=True)
            self.waitFor(self.path + "menu.png", clickUntil=True, clickx=1910, clicky=197)
            
            self.waitFor(self.EXCLAMATION[2], doClick=True)
            self.waitFor(self.path + "menu.png", clickUntil=True, clickx=1910, clicky=197)
            
            self.drag("right", 1.027)
            time.sleep(1)
            
            self.waitFor(self.EXCLAMATION[4], doClick=True)
            self.waitFor(self.path + "menu.png", clickUntil=True, clickx=1910, clicky=197)
            
            return True
            
        def moveGrastaTrove(self):

            phase = 0   #         0,         3,
            duration  = [ 0.7999873]
            direction = [    "left"]
            
            while True:
                
                if phase == 0:
                    self.waitFor(self.EXCLAMATION[3], doClick=True)
                    self.waitFor(self.path + "menu.png", clickUntil=True)
                    self.waitFor(self.EXCLAMATION[3], doClick=True)
                    self.waitFor(self.path + "menu.png", clickUntil=True)
                
                self.drag(direction[phase], duration[phase])
                
                if phase == 0:
                    time.sleep(1)
                    self.waitFor(self.EXCLAMATION[3], doClick=True)
                    self.waitFor(self.path + "menu.png", clickUntil=True)
                    return True
                    break
                phase += 1
        
        self.waitFor(self.path + "menu.png")
        
        while True:
        
            start = time.time()
            
            while (time.time() - start) < 10:
                pcdII         = self.locateOnScreen(self.path + "pcd_II.png", confidence=0.95)
                pcdIII        = self.locateOnScreen(self.path + "pcd_III.png", confidence=0.90)
                pcdIV         = self.locateOnScreen(self.path + "pcd_IV.png", confidence=0.95)
                pcdV          = self.locateOnScreen(self.path + "pcd_V.png", confidence=0.95)
                pcdVI         = self.locateOnScreen(self.path + "pcd_VI.png", confidence=0.95)
                dungeon       = self.locateOnScreen(self.path + "dungeon.png", confidence=0.95)
                dummyTraining = self.locateOnScreen(self.path + "pcd_dummyTraining.png", confidence=0.95)
                grastaTrove   = self.locateOnScreen(self.path + "pcd_grastaTrove.png", confidence=0.95)
                catParadise   = self.locateOnScreen(self.path + "pcd_catParadise.png", confidence=0.95)
                
                if pcdII:
                    print("ZOL PLAINS!!!")
                    movePcdII()
                    time.sleep(1)
                    
                elif pcdIII:
                    print("INDUMSTRIAL RUINS!!!")
                    movePcdIII() 
                    time.sleep(1)
                    
                elif dungeon:
                    print("DONEgeonnnnn")
                    loop, phase = moveDungeon(mapName, innerMapName, diff, mapNameList, mapIndex)
                    return loop, phase
                    
                elif pcdIV:
                    print("ACUTEL!!!")
                    movePcdIV()
                    time.sleep(1)
                    
                elif pcdV:
                    print("BARUOKIIII!!!")
                    movePcdV()
                    time.sleep(1)
                    
                elif pcdV:
                    print("ELLLIZIIIOOOOOOON LEGGGGGOOOO THE END!!!")
                    self.wlog("CHANTTTT BARRRRD!!!!")
                    
                elif dummyTraining:
                    print("DUMMY TRAINIG!!!")
                    moveDummyTraining()
                    time.sleep(1)
                    
                elif grastaTrove:
                    print("GARASTAAA!!!")
                    moveGrastaTrove()
                    time.sleep(1)
                    
                elif catParadise:
                    print("KITTTYYYY!!!")
                    moveCatParadise()
                    time.sleep(1)
                                
                else:
                    print("NO ROOM FOUND")        
                    self.notify("Subject: Uncharted Territory! Requesting User Assistanece!")
                    quit()

    def whiteCard(self, mapName, innerMapName, diff, mapNameList, mapIndex):
        
        self.findMap("phantomCrystal", "timeStop", "illusionWorld", mapNameList, mapIndex, dungeon=True, diff="hard")

        self.waitFor(self.EXCLAMATION[0], doClick=True, region=(0, 0, 600, 1080))
        self.waitFor(self.path + "menu.png", clickUntil=True, clickx=1910, clicky=197)
        
        self.waitFor(self.EXCLAMATION[0], doClick=True, region=(900, 0, 1020, 1080))
        self.waitFor(self.path + "menu.png", clickUntil=True, clickx=1910, clicky=197)
            
        self.waitFor(self.path + "menu.png")
        loop, phase = self.identifyRoomPCD(mapName, innerMapName, diff, mapNameList, mapIndex)
        return loop, phase
                   
    def abilityChooser(self, first, second):

        prefered = self.vspath + "ability\\" + first +".png"
        secondary = self.vspath + "ability\\" + second +".png"
        
        noPrefered, preferedCoords = self.waitFor(prefered, grayscale=False, timeout=2, doClick=True, confidence=0.9)
        if noPrefered == True:
            print("trying secoundary!!")
            self.waitFor(secondary, grayscale=False, doClick=True)

    def exist(self, ability):

        image = self.vspath + "ability\\exist\\" + ability + ".png"
        
        noImage, imageCoords = self.waitFor(image, timeout=3, confidence = 0.9)
        if noImage == True:
            return False
        else:
            return True

    def validateParty(self, partyName):
        
        if partyName == "":
            return False
        
        self.waitFor(self.path + "menu.png", doClick=True)
        self.waitFor(self.vspath + "party.png", doClick=True)
        
        for _ in range(10):
            
            noParty, partyCoords = self.waitFor(self.vspath + "partys\\" + partyName + ".png", timeout=2)
            if noParty == True:
                self.drag("left", 1)
                continue
            elif noParty == False:
                break
            
            print("party not Found")
            
            self.wlog("Party Not found!")
        
        self.waitFor(self.path + "menu.png", clickUntil=True, clickx=1900, clicky=30)

    def findMap(self, mapName, era, continent, mapNameList, mapIndex, innerMapName=None, dungeon=False, diff="veryHard", errorLogging=False, multiDestination= False, option = 1):
        
        print(f"Finding {mapName}.....")
        
        if dungeon == False:
            self.waitFor(self.path + "map.png", doClick=True, clickx=941, clicky=28, errorLogging=errorLogging)
            
        self.waitFor(self.path + "future.png", errorLogging=errorLogging)
        
        if era == "past":
            self.click(120, 173, errorLogging=errorLogging)
            print("Into the past")
        elif era == "present":
            self.click(311, 164, errorLogging=errorLogging)
            print("Into the present")
        elif era == "future":
            self.click(481, 157, errorLogging=errorLogging)
            print("Into the future")
        elif era == "timeStop":
            self.click(663, 160, errorLogging=errorLogging)
            print("A little rest?")
        elif era == "hollow":
            self.click(853, 160, errorLogging=errorLogging)
            print("Into the hollow")
        
        self.waitFor(self.vspath + "no.png", timeout=2, doClick=True, errorLogging=errorLogging) 
            
        self.click(1801, 977)
        
        if dungeon == True:
            if continent != "underworld":
                self.waitFor(self.vspath + "maps\\continent_" + continent + ".png", doClick=True)
        else:
            self.waitFor(self.vspath + "maps\\continent_" + continent + ".png", doClick=True)
            
        if era == "past":
            self.click(120, 173, errorLogging=errorLogging)
            print("Into the past, once again")
        elif era == "present":
            self.click(311, 164, errorLogging=errorLogging)
            print("Into the present, once again")
        elif era == "future":
            self.click(481, 157, errorLogging=errorLogging)
            print("Into the future, once again")
        elif era == "timeStop":
            self.click(663, 160, errorLogging=errorLogging)
            print("Resting a little more...")
        elif era == "hollow":
            self.click(853, 160, errorLogging=errorLogging)
            print("Into the hollow, once again")
        
        self.waitFor(self.vspath + "no.png", timeout=2, doClick=True, errorLogging=errorLogging)    
        
        starty = 400
        counter = 0
        foundOut = False
        foundIn = False
        
        while True:
        
            time.sleep(1)
            if foundOut == False:
                noMap, mapCoords = self.waitFor(self.vspath + "maps\\map_" + mapName + ".png", timeout=2, doClick=True, errorLogging=errorLogging, region=(0, 303, 1920, (1080-303)))
            elif foundOut == True:
                noMap, mapCoords = self.waitFor(self.vspath + "maps\\map_" + innerMapName + ".png", timeout=2, doClick=True, errorLogging=errorLogging)
            
            if noMap == True:
                counter += 1
            
                if counter == 1:
                    for _ in range(4):
                        self.drag("right", 0, sy=starty, errorLogging=errorLogging)
                        time.sleep(0.05)
                    for _ in range(2):
                        self.drag("down", 0, sy=starty, errorLogging=errorLogging)
                        time.sleep(0.05)
                elif counter == 2:
                    for _ in range(1):
                        self.drag("left", 0, sy=starty, errorLogging=errorLogging)
                        time.sleep(0.05)
                elif counter == 3:
                    for _ in range(1):
                        self.drag("left", 0, sy=starty, errorLogging=errorLogging)
                        time.sleep(0.05)
                elif counter == 4:
                    for _ in range(1):
                        self.drag("up", 0, sy=starty, errorLogging=errorLogging)
                        time.sleep(0.05)
                elif counter == 5:
                    for _ in range(1):
                        self.drag("right", 0, sy=starty, errorLogging=errorLogging)
                        time.sleep(0.05)
                elif counter == 6:
                    for _ in range(1):
                        self.drag("right", 0, sy=starty, errorLogging=errorLogging)
                        time.sleep(0.05)
                elif counter == 7:
                    for _ in range(1):
                        self.drag("up", 0, sy=starty, errorLogging=errorLogging)
                        time.sleep(0.05)
                elif counter == 8:
                    for _ in range(1):
                        self.drag("left", 0, sy=starty, errorLogging=errorLogging)
                        time.sleep(0.05)
                elif counter == 9:
                    for _ in range(1):
                        self.drag("left", 0, sy=starty, errorLogging=errorLogging)
                        time.sleep(0.05)
                else:
                    counter = 0
                    print("Trying Once More!")
                    starty += 50
                    if starty > 1000:
                        starty = 400
                    
            elif noMap == False:

                if innerMapName is not None:
                    counter = 0
                    print("inner map time")
                    if foundOut == True:
                        foundIn = True
                        
                elif innerMapName is None:
                    foundIn = True
                
                foundOut = True
                
                if foundOut == True and foundIn == True:
                    break
                    
        if dungeon == False:
            if multiDestination == True:
                if option == 1:
                    self.click(1097, 394)
                elif option == 2:
                    self.click(1100, 522)
                elif option == 3:
                    self.click(1095, 673)
                elif option == 4:
                    self.click(1083, 821)
            self.waitFor(self.vspath + "yes.png", doClick=True)
            self.waitFor(self.path + "menu.png")
            return None, None
        elif dungeon == True:
            loop, phase = self.startDungeon(diff, mapNameList, mapIndex)
            return loop, phase
            
    def testMarks(self, marks, region=None, confidence=0.8, errorLogging=False):
        
        counter = 0
        
        for i in marks:
        
            noMark, markCoords = self.waitFor(i, timeout=2, region=region, confidence=confidence, errorLogging=errorLogging)
            if noMark == False:
                if errorLogging == True:
                    print("DA WINNER IS......... EXCLMATION " + str(counter))
                return markCoords, counter
                
            counter += 1
        
        return None, None
            
    def AF_control(self, status, mapNameList, mapIndex):
        self.findMap("nagsham", "present", "garulea", "outer", mapNameList, mapIndex)
        self.drag("right", 1.271)
        self.drag("up", 1)
        self.drag("right", 6.357)
        time.sleep(1)
        self.waitFor(self.EXCLAMATION[2], doClick=True)
        self.waitFor(self.vspath + "attackButton.png", clickUntil=True, clickx=966, clicky=492)
        self.horror('a', 'q', 's', 'q', 'd', 'q', 'f', 'q', 'g')
        for i in range(3):
            self.waitFor(self.vspath + "attackButton.png", clickUntil=True, doClick=True)
        if status == "deplete":
            self.waitFor(self.vspath + "attackButton.png", clickUntil=True)
            self.press('m')
        elif status == "refill":
            self.waitFor(self.vspath + "attackButton.png", clickUntil=True, doClick=True)
            self.waitFor(self.path + "menu.png", clickUntil=True)
            self.waitFor(self.EXCLAMATION[2], doClick=True)
            self.waitFor(self.vspath + "attackButton.png", clickUntil=True, clickx=966, clicky=492)
            for i in range(5):
                self.waitFor(self.vspath + "attackButton.png", clickUntil=True, doClick=True)
        self.waitFor(self.path + "menu.png", clickUntil=True)

    def countRuns(self, start, times, runs):
        
        assert type(times) == list
        
        end = time.time() - start
        times.append(end)
        runs += 1
        if len(times) > 1:
            print("\n\n\nThis is run ", end='')
            print(runs, end="!\n----------------------------------------------------------------------------\n")
            print("This run took", end=' ')
            print((times[len(times)-1] - times[len(times)-2])/60, end=" minutes!\nThe total time taken is ")
            print(times[len(times)-1]/60, end=" minutes!\n----------------------------------------------------------------------------\n\n\n")
        else:
            print("This is run ", end='')
            print(runs, end="!\n----------------------------------------------------------------------------\n")
            print("This run took", end=' ')
            print((times[len(times)-1])/60, end=" minutes!\nThe total time taken is ")
            print(times[len(times)-1]/60, end=" minutes!\n----------------------------------------------------------------------------\n\n\n")
        return runs

    def returnToDungeonGates(self, mapName, mapEra, mapContinent, mapNameList, mapIndex, innerMapName, dungeon, difficulty, errorLogging=False):

        self.findMap("spacetimeRift", "timeStop", "illusionWorld", mapNameList, mapIndex, dungeon=False)
        self.drag("left", 0.694)
        time.sleep(0.5)
        self.waitFor(self.path+"keyCardExclamation.png", doClick=True, timeout=3, grayscale=False, confidence=0.95)
        self.waitFor(self.path + "menu.png", clickUntil=True)
        loop, phase = self.changeDungeon(mapName, mapEra, mapContinent, mapNameList, mapIndex, innerMapName, dungeon, difficulty, errorLogging)
        return loop, phase

    def changeDungeon(self, *args):
        
        self.waitFor(self.EXCLAMATION[0], doClick=True, region=(0, 0, 1450, 1080))
        loop, phase = self.findMap(*args)
        return loop, phase


