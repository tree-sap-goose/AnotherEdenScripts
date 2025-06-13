import win32con, win32api, win32gui, win32ui
import time, cv2, traceback, os, subprocess
import webbrowser
import pyautogui as gui
import functionScripts2 as scripts
import _user_console_ as uc

def press(fn, key, times=1, delay=0.3, errorLogging=False):
    
    hwnd=fn.hwnd
    
    for _ in range(times):
        
        for k in key:
            
            win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, fn.VK_CODE[k], 0)
            #win32gui.SendMessage(hwnd, win32con.WM_KEYUP, fn.VK_CODE[k], 0)
            time.sleep(delay)
            
            if errorLogging == True:
                print("Pressed the ", end='')
                print(k, end=" key ")
                print(times, end=" times with a delay of ")
                print(delay, end=" secounds.\n")

#Discontinued due to unpredictibility
'''
def qooUpdate():
    fn.press('f2')
    fn.waitFor(fn.path + "androidClearAll.png", doClick=True)
    fn.waitFor(fn.path + "qooAppLogo.png", doClick=True)
    
    count = 0
    for i in range(20):
        time.sleep(1)
        count += 1
        #print(count)
    
    noController, controllerCoords = fn.waitFor(fn.path + "qooAppController.png", confidence=0.9, doClick=True, timeout=60)
    if noController:
        fn.waitFor(fn.path + "qooAppBackArrow.png", doClick=True, timeout=10)
        fn.waitFor(fn.path + "qooAppUpdate.png", doClick=True)
        fn.waitFor(fn.path + "qooAppInstall.png", doClick=True)
        fn.waitFor(fn.path + "androidInstall.png", doClick=True, timeout=-1)
        fn.waitFor(fn.path + "androidOpen.png", doClick=True, timeout=-1)
        fn.waitFor(fn.path + "qooAppController.png", confidence=0.9, doClick=True, timeout=200)
    fn.waitFor(fn.path + "QooAppUpdateAll.png", doClick=True)
    fn.waitFor(fn.path + "androidInstall.png", doClick=True)
    fn.press('f2')
    fn.waitFor(fn.path + "androidClearAll.png", doClick=True)
'''

def apkPureUpdate():

    updateDownloadPath = "https://d.apkpure.com/b/XAPK/games.wfs.anothereden?version=latest"
    webbrowser.open(updateDownloadPath)
    
    #WIP
    '''
    ############################################
    # Set xapk files to be saved automatically #
    ############################################
    
    time.sleep(5)
    downloadDialogue = scripts.Window("Opening ANOTHER EDEN", None, "C:\\Users\\Twilight_Moon\\Documents\\Code\\Python\\AnotherEdenScripts\\img\\", "gl", partial=True)
    
    try:
        win32gui.SetForegroundWindow(downloadDialogue.hwnd)
    except:
        print("Set forground window failed.")
    try:
        win32gui.SetFocus(downloadDialogue.hwnd)
    except:
        print("Set focus failed.")
    
    time.sleep(2)
    downloadDialogue.waitFor(downloadDialogue.path + "windowDialogues\okBTN.png", doClick=True, confidence=0.95, errorLogging=True)
    downloadDialogue.press('enter')
    
    time.sleep(2)
    saveDialogue = scripts.Window("Enter name of file to save to", "Button", "C:\\Users\\Twilight_Moon\\Documents\\Code\\Python\\AnotherEdenScripts\\img\\", "gl", partial=True, cycle=1)
    time.sleep(0.5)
    saveDialogue.waitFor(saveDialogue.path + "windowDialogues\saveBTN.png", doClick=True, confidence=0.95, timeout=5, errorLogging=True)
    saveDialogue.press('enter')
    
    #give it 10 mins to download
    time.sleep(600)
    
    #Get Apks from Downloads
    downloadsDir = "C:\\Users\\Twilight_Moon\\downloads\\AnotherEdenAPK"
    apks = []
    
    for i in os.listdir(downloadsDir):
        if ".xapk" in i:
            apks.append(i)
            
    #get most updated version
    
    versionNums = []
    
    for a in apks:
        v = ''
        for i in a:
            if i.isdigit():
                v += i
            elif i == '.':
                v += i
        versionNums.append(v)
        
    versionNums.sort(key=lambda s: [int(u) for u in s.split('.')])
    file = [a for a in apks if versionNums[len(versionNums)-1] in a]
    
    #launch apk
    subprocess.run(downloadsDir+file[0])
    '''
        
    

def timeLoop(): 
    
    fn = scripts.Window("LDPlayer", "RenderWindow", uc.script_path + "img\\", "gl")
    
    start = time.time()
    
    alreadySeen = not uc.ads
    status = True
    
    while status == True and ((time.time() - start) < (3*3600)):

        events  = [fn.locateOnScreen(fn.vspath + "yes.png", confidence=0.8),                                   #0
                   fn.locateOnScreen(fn.path + "ok.png", confidence=0.8),                                    #1
                   fn.locateOnScreen(fn.vspath + "continue.png", confidence=0.8),                              #2
                   fn.locateOnScreen(fn.path + "menu.png", confidence=0.8),                                  #3
                   fn.locateOnScreen(fn.vspath + "takeOver.png", confidence=0.8),               #4
                   fn.locateOnScreen(fn.vspath + "startUsingTransfer.png", confidence=0.8),     #5
                   fn.locateOnScreen(fn.vspath + "watchVideo.png", confidence=0.8),             #6
                   fn.locateOnScreen(fn.vspath + "close.png", confidence=0.8),                  #7
                   fn.locateOnScreen(fn.path + "AElogo.png", confidence=0.75),                  #8
                   fn.locateOnScreen(fn.vspath + "agree.png", confidence=0.8),                  #9
                   fn.locateOnScreen(fn.vspath + "standardDownload.png", confidence=0.8)]       #10
        
        for event in events:
            
            if event == events[1] and events[1] is not None:
                
                eventCoords = gui.center(event)
                fn.click(eventCoords.x, eventCoords.y)
                
                noUpdate, updateCoords = fn.waitFor(fn.path + "googlePlay.png", timeout=60)
                if noUpdate == False:
                    print("\n\nInitiating Update procedures...")
                    apkPureUpdate()
                    
            elif event == events[3] and events[3] is not None:
                
                ads = uc.ads
                
                if alreadySeen == False:
                    noButton, buttonCoords = fn.waitFor(fn.vspath + "watchVideo.png", confidence=0.8, timeout=60, doClick=True, errorLogging=True)
                    if noButton == False:
                        fn.waitFor(fn.vspath + "close.png", doClick=True)
                        fn.waitFor(fn.path + "ok.png", doClick=True)
                        
                while ads == True:
                    fn.waitFor(fn.path + "menu.png", doClick=True)
                        
                    for i in range(5):
                        noButton, buttonCoords = fn.waitFor(fn.vspath+"watchVideo_1.png", clickUntil=True, doClick=True, clickx=80, clicky=55, timeout=5)
                        if noButton == True:
                            ads = False
                            break
                        fn.waitFor(fn.path + "ok.png", doClick=True)
                        fn.waitFor(fn.path + "menu.png", doClick=True)
                        fn.waitFor(fn.vspath+"watchVideo_1.png", clickUntil=True, doClick=True, clickx=80, clicky=55)
                        fn.waitFor(fn.path + "ok.png", clickUntil=True, doClick=True)
                    
                    if ads == False:
                        break
                    else:
                        fn.waitFor(fn.path + "ok.png", doClick=True)
                        
                fn.waitFor(fn.path + "menu.png")
                
                status = False
                
                return True
                
            elif event == events[4] and events[4] is not None:
            
                if fn.locateOnScreen(fn.vspath + "prep.png", confidence=0.8):
                    eventCoords = gui.center(event)
                    fn.click(eventCoords.x, eventCoords.y)
                else:
                    fn.notify("Subject:Data not transfered properly from iphone. Try Again?")
                    wlog("Data not transfered properly from iphone. Try Again?")
            
            elif event == events[5] and events[5] is not None:
                
                transfer = True
                
                #click event 5
                eventCoords = gui.center(event)
                fn.click(eventCoords.x, eventCoords.y)
                
                #click buttons till transfer ID textbox
                fn.waitFor(fn.vspath + "transferViaIssuedId.png", doClick=True)
                fn.waitFor(fn.vspath + "enterTransferId.png", doClick=True)
                
                #make sure app takes all keyboard input (loop version ensures that program does not stop on account of win32 error)
                '''win32gui.SetForegroundWindow(fn.HWND)'''
                    
                #based on version, input ID    
                if fn.version == 'gl':
                    print("Entering Username....")
                    press(fn, uc.username)
                    time.sleep(1)
                    
                #JP is no longer supported, keeping in case its picked up again
                '''
                elif fn.version == "jp":
                    gui.write(jp_username)
                '''
                
                #enter password in textbox
                fn.waitFor(fn.vspath + "enterPassword.png", doClick=True)
                print("Entering Password....")
                press(fn, uc.password)
                
                #added becuase set sometimes was clicked but not registered.
                time.sleep(3)
                
                #click the rest of the buttons needed to return to main loop
                fn.waitFor(fn.vspath + "set.png", doClick=True)
                
                noTransfer, transferCoords = fn.waitFor(fn.vspath + "transfer.png", timeout=10)
                if noTransfer:
                    fn.waitFor(fn.vspath + "toTheStore.png", confidence=0.8)
                    qooUpdate()
                else:
                    fn.waitFor(fn.vspath + "transfer.png", doClick=True)
                
            elif event == events[6] and events[6] is not None:
                
                eventCoords = gui.center(event)
                
                if uc.ads == True:
                    fn.click(eventCoords.x, eventCoords.y)
                    fn.waitFor(fn.vspath + "close.png", doClick=True)
                    fn.waitFor(fn.path + "ok.png", doClick=True)
                    alreadySeen = True
                else:
                    #fn.click(eventCoords.x, eventCoords.y)
                    print("do not have enough data for this point; Please get rid or it yourself.")
                    fn.waitFor(fn.path + "menu.png")
                
            elif event == events[8] and events[8] is not None:
                eventCoords = gui.center(event)
                fn.click(eventCoords.x, eventCoords.y+50)
                '''cmd = fn.Window("C:\\Windows\\system32\\cmd.exe", None)
                try:
                    win32gui.SetForegroundWindow(cmd.hwnd)
                except:
                    pass'''
                
            elif event is not None:
                eventCoords = gui.center(event)
                fn.click(eventCoords.x, eventCoords.y)


if __name__ == "__main__":
    timeLoop()