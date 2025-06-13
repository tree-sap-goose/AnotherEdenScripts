import win32api, win32gui, win32con, time
import functionScripts2 as scripts
import _user_console_ as uc

def cashPoints(fn):
    
    while True:
        noExclamation, exclamationCoords = fn.waitFor(fn.EXCLAMATION[4], doClick=True, timeout=5, errorLogging=True)
        if noExclamation == True:
            raise Exception("Random Pathing Error")
        fn.waitFor(fn.vspath + "stop.png", clickUntil=True)
        time.sleep(1)
        fn.click(1242, 859)
        fn.waitFor(fn.vspath + "stop.png")
        time.sleep(1)
        fn.click(639, 565)
        enough, enoughCoords = fn.waitFor(fn.vspath + "notEnough.png", clickUntil=True, timeout=5)
        if enough == False:
            fn.waitFor(fn.path + "menu.png", clickUntil=True)
            break
        fn.waitFor(fn.vspath + "yes.png", doClick=True, clickUntil=True)
        fn.waitFor(fn.path + "menu.png", clickUntil=True)

def main(mapNameList, mapIndex, phaseNum=0):

    fn = scripts.AEWindow("LDPlayer", "RenderWindow", uc.script_path + "img\\", "gl")

    mapName = "lua"
    mapEra = "past"
    continent = "zerberiya" 
    difficulty = "veryHard" 
    innerMapName = None

    runs = 0
    start = time.time()
    times = []
    
    errorCounter = 0

    phase = phaseNum  #   0,         1,         2,         3---       4,         5,         6,         7,         8,         9---      10,        11,        12,        13,        14,        15,        16,        17,        18,        19,        20,        21,        22,        23,        24,        25,        26,        27,        28,        29,        30,        31,        32,        33,        34,        35,        36,        37,        38**       39,        40**       41,        42,        43,        44,        45,        46,        47,        48,        49,        50---       51,       52,        53,        54,        55,        56,        57,        58,         59,        60,        61,        62,         63,        64,        65,        66,        67,        68,        69***       70,        71,        72,        73,        74,        75,        76---      77,        78,        79,
    duration  = [   1.75857,       1.5, 1.1686368,       1.5,     2.591,       1.5,     1.184,       1.5,     0.576,     1.965,     1.008,       1.5,     2.753,       1.5,     0.368,     3.497,     1.048,       1.5,     1.208,       1.5,     0.855,     2.000,       1.5,     0.919,       1.5,     1.552,     2.723,       1.5,     0.728,     3.295,      5.16,     0.864,       1.5,      1.68,       1.5,     0.792,     3.048,       1.5,     0.952,       1.5,     1.072,     1.865,       1.5,     1.111,       1.5,     1.008,     0.896,       1.5,     1.159,       1.5,     0.233,     0.887,      0.72,       1.5,     2.247,       1.5,     0.688,     2.312,     0.407,     1.895,]
    direction = [   "right",      "up",   "right",      "up",    "left",      "up",   "right",      "up",   "right",    "left",    "left",    "down",    "left",    "down",   "right",    "left",   "right",      "up",   "right",      "up",   "right",    "left",      "up",    "left",      "up",   "right",    "left",      "up",    "left",   "right",   "right",    "left",    "down",    "left",    "down",    "left",   "right",      "up",    "left",      "up",   "right",    "left",      "up",    "left",      "up",   "right",    "left",    "down",    "left",    "down",   "right",    "left",   "right",      "up",    "left",    "down",   "right",    "left",    "left",    "left",]

    loop = True
    #'''
    if phase == 0:
        fn.validateParty("RedKey")
        
        if mapIndex == 0:
            loop, phase = fn.returnToDungeonGates(mapName, mapEra, continent, mapNameList, mapIndex, innerMapName, True, difficulty)
            
        else:
            loop, phase = fn.changeDungeon(mapName, mapEra, continent, mapNameList, mapIndex, innerMapName, True, difficulty)
            
        
    #'''
    
    while loop == True:
        #print("---------------------phase", end=' ')
        #print(phase, end="---------------------\n")
        
        if phase >= 0:
            if direction[phase] == "right" or direction[phase] == "left":
                fn.drag(direction[phase], duration[phase])
            else:
                fn.drag(direction[phase], 0.1)
                time.sleep(1)
        
        if phase == 0:

            if runs == 0:
                fn.drag("right", 4)
                fn.drag("left", 0.741)
                fn.drag("up", 1)
                fn.waitFor(fn.path + "menu.png")
                fn.drag("right", 0.8)
                time.sleep(1)

                cashPoints(fn)

                fn.waitFor(fn.path + "menu.png")
                fn.drag("left", 0.8)
                fn.drag("down", 1)
                fn.waitFor(fn.path + "menu.png")
                fn.drag("left", 1.096)
       
        if phase == 3:
            fn.waitFor(fn.path + "menu.png", timeout=10)
            
            #JP is no longer supported; keeping in case its picked up again.
            '''
            if fn.version == "jp":
                fn.battle("pause", 'a', 'g', 'v', 's', 'r', 'f', 'e', 'g')
            else:
                fn.battle("pause", 'a', 'e', 's', 'e', 'd', 'e', 'f', 'r', 'g')
            '''
            
            fn.battle("pause", 'a', 'e', 's', 'e', 'd', 'e', 'f', 'r', 'g')

        elif phase == 8 or phase == 15 or phase == 25 or phase == 30 or phase == 51 or phase == 58:
            time.sleep(0.5)
            fn.waitFor(fn.EXCLAMATION[2], doClick=True, errorLogging=True, confidence=0.8)
            fn.waitFor(fn.path + "menu.png", clickUntil=True)
            
        elif phase == 9:
            time.sleep(0.5)
            fn.clickBomb()
            fn.waitFor(fn.path + "menu.png", clickUntil=True)
            
        elif phase == 14:
            time.sleep(0.5)
            fn.clickBomb()
            fn.waitFor(fn.path + "menu.png", clickUntil=True)

        elif phase == 20:
            time.sleep(0.5)
            fn.clickBomb()
            fn.waitFor(fn.path + "menu.png", clickUntil=True)
        
        elif phase == 22:
        
            fn.waitFor(fn.path + "menu.png")
            
            #JP is no longer supported; keeping in case its picked up again.
            '''
            if fn.version == "jp":
                fn.battle("pause", 'a', 'g', 'v', 's', 'r', 'f', 'e', 'g')
            else:
                fn.battle("pause", 'a', 'e', 's', 'e', 'd', 'e', 'f', 'r', 'g')
            '''
            
            fn.battle("pause", 'a', 'e', 's', 'e', 'd', 'e', 'f', 'r', 'g')
            
            time.sleep(0.5)
            fn.clickBomb()
            fn.waitFor(fn.path + "menu.png", clickUntil=True)
        
        elif phase == 26:
            time.sleep(0.5)
            fn.clickBomb()
            fn.waitFor(fn.path + "menu.png", clickUntil=True)
            
        elif phase == 28:
            time.sleep(0.5)
            fn.clickBomb()
            fn.waitFor(fn.path + "menu.png", clickUntil=True)
        
        elif phase == 29:
            time.sleep(0.5)
            fn.clickBomb()
            fn.waitFor(fn.path + "menu.png", clickUntil=True)
        
        elif phase == 35:
            time.sleep(0.5)
            fn.clickBomb()
            fn.waitFor(fn.path + "menu.png", clickUntil=True)
        
        elif phase == 37:

            fn.waitFor(fn.path + "menu.png")
            
            #JP is no longer supported; keeping in case its picked up again.
            '''
            if fn.version == "jp":
                fn.battle("pause", 'a', 'g', 'v', 's', 'r', 'f', 'e', 'g')
            else:
                fn.battle("pause", 'a', 'e', 's', 'e', 'd', 'e', 'f', 'r', 'g')
            '''
                
            fn.battle("pause", 'a', 'e', 's', 'e', 'd', 'e', 'f', 'r', 'g')
            
            time.sleep(0.5)
            fn.clickBomb()
            fn.waitFor(fn.path + "menu.png", clickUntil=True)
        
        elif phase == 40:
            time.sleep(0.5)
            fn.clickBomb()
            fn.waitFor(fn.path + "menu.png", clickUntil=True)
        
        elif phase == 42:
            fn.horror("pause", 'a', 'e', 's', 'e', 'd', 'e', 'f', 'r', 'g', "done")
        
        elif phase == 45:
            time.sleep(0.5)
            fn.clickBomb()
            fn.waitFor(fn.path + "menu.png", clickUntil=True)
        
        elif phase == 50:
        
            time.sleep(0.5)
            fn.clickBomb()
            fn.waitFor(fn.path + "menu.png", clickUntil=True)
        
        elif phase == 56:
            time.sleep(0.5)
            fn.clickBomb()
            fn.waitFor(fn.path + "menu.png", clickUntil=True)
            
        elif phase == 57:
            time.sleep(0.5)
            fn.waitFor(fn.LEAVE_DOOR[0], doClick=True)
            fn.waitFor(fn.path + "menu.png", clickUntil=True)
        
        elif phase == 59:
            fn.waitFor(fn.vspath + "yes.png", doClick=True)
            
            #JP is no longer supported; keeping in case its picked up again.
            '''
            if fn.version == "jp":
                fn.horror("pause", 'a', 'r', 's', 'q', 'd', 'g', 'v', 'f', 'r', 'g', "pause", 's', 'r', 'd', 'w', 'g', "done")
            else:
                fn.horror("pause", 'a', 'e', 's', 'e', 'd', 'e', 'f', 'r', 'g', "done")
            fn.waitFor(fn.path + "menu.png", clickUntil=True) 
            '''
            
            fn.horror("pause", 'a', 'e', 's', 'e', 'd', 'e', 'f', 'r', 'g', "done")
            
            runs = fn.countRuns(start, times, runs)  
            loop, phase = fn.goAgain(mapName, difficulty, mapNameList, mapIndex, innerMap=innerMapName)
            
        
        phase += 1
        
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
if __name__ == "__main__":
    phase = input("What phase? ")
    main(["City of Lost Paradise"], 0, phaseNum=int(phase))