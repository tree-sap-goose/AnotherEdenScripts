import win32api, win32gui, win32con, time
import functionScripts2 as scripts
import _user_console_ as uc

fn = scripts.AEWindow("LDPlayer", "RenderWindow", uc.script_path + "img\\", "gl")

def addPhase(data, currentPhase, lastPhase, phaseData, preliminaryData1, duration, correctionFactor):
    
    #print("from addPhase(): current phase: " + str(currentPhase) + "/nlast Phase: " + str(lastPhase))
    
    
    if currentPhase == -1:
        if currentPhase <= lastPhase:
                pass
        else:
            preliminaryData1 += "\t\tif phase == 0:\n"
        preliminaryData1 += data
        
    elif phaseData == '':
        if currentPhase <= lastPhase:
                pass
        else:
            phaseData += "\t\tif phase == " + str(len(duration)+correctionFactor-1) + ":\n"
        phaseData += data
    else:
        if currentPhase <= lastPhase:
                pass
        else:
            phaseData += "\t\telif phase == " + str(len(duration)+correctionFactor-1) + ":\n"
        phaseData += data

    
    return phaseData, preliminaryData1

def main():

    correctionFactor = int(input("What phase are we starting on? "))
    userClick = input("Would you like to gauge clicks? (y/n) ")
    style = input("do u want phases? (y/n)")

    duration = []
    direction = []
    isClick = []

    #deviation from 1920x1080
    monitorDiff = -60

    currentPhase = -1 + correctionFactor
    lastPhase = currentPhase - 1 

    phaseData = ''
    phaseTables = ''

    preliminaryData0 = "import win32api, win32gui, win32con, time\nimport functionScripts2 as scripts\nimport _user_console_ as uc\n\ndef main(mapNameList, mapIndex, phaseNum=0):\n\n\tfn = scripts.AEWindow(\"LDPlayer\", \"RenderWindow\", uc.script_path + \"img\\\\\", \"gl\")\n\n\tmapName = \"lua\"\n\tmapEra = \"past\"\n\tcontinent = \"zerberiya\" \n\tdifficulty = \"veryHard\" \n\tinnerMapName = None\n\n\truns = 0\n\tstart = time.time()\n\ttimes = []\n\n"
    preliminaryData1 = "\n\tloop = True\n\t#'''\n\tif phase == 0:\n\t\tfn.validateParty(\"\")\n\t\t\n\t\tif mapIndex == 0:\n\t\t\tloop, phase = fn.returnToDungeonGates(mapName, mapEra, continent, mapNameList, mapIndex, innerMapName, True, difficulty)\n\t\t\t\n\t\telse:\n\t\t\tloop, phase = fn.changeDungeon(mapName, mapEra, continent, mapNameList, mapIndex, innerMapName, True, difficulty)\n\t\t\t\n\t\t\n\t#'''\n\t\n\twhile loop == True:\n\t\t#print(\"---------------------phase\", end=' ')\n\t\t#print(phase, end=\"---------------------\\n\")\n\t\t\n"
    preliminaryData2 = "\t\tif phase >= 0:\n\t\t\tif direction[phase] == \"right\" or direction[phase] == \"left\":\n\t\t\t\tfn.drag(direction[phase], duration[phase])\n\t\t\telse:\n\t\t\t\tfn.drag(direction[phase], 0.1)\n\t\t\t\ttime.sleep(1)\n\t\t\n"
        

    #record click data
    if userClick == "y":
        gaugeClicks = True
    elif userClick == "n":
        gaugeClicks = False
    else:
        print("Come Again?")

    #put in list style
    if style == "y":
        phases = True
    elif style == "n":
        phases = False
    else:
        print("Come Again?")

    programState = True

    while programState == True:
        
        #eliminates unwanted keypresses
        mouseDown = 0
        addAction = 0
        
        #gets key presses
        mouseDown = win32api.GetKeyState(win32con.VK_LBUTTON)
        addAction = win32api.GetKeyState(fn.VK_CODE['z'])
        
        #if mouse button is clicked
        if mouseDown == -127 or mouseDown == -128:
            
            #get start time and cursor position
            start = time.time()
            x1, y1 = win32api.GetCursorPos()
            y1 += monitorDiff
            
            while True:
                
                mouseUp = win32api.GetKeyState(win32con.VK_LBUTTON)
                
                #wait For mouse button to be released
                if mouseUp == 0 or mouseUp == 1:
                    
                    #get cursor position
                    x2, y2 = win32api.GetCursorPos()
                    y2 += monitorDiff
                    
                    #get duration to three decimal places
                    end = time.time() - start
                    end = round(end, 3)
                    
                    #figure out direction using differences
                    if abs(x2-x1) > abs(y2-y1):
                        
                        duration.append(end)
                        
                        if gaugeClicks == True:
                            isClick.append("\"n/a\"")
                        
                        if x2-x1 > 0:
                            direction.append("\"right\"")
                            
                        elif x2-x1 < 0:
                            direction.append("\"left\"")
                            
                    elif abs(x2-x1) < abs(y2-y1):
                    
                        duration.append(1.3)
                        if gaugeClicks == True:
                            isClick.append("\"n/a\"")
                        
                        if y2-y1 > 0:
                            direction.append("\"down\"")
                            
                        elif y2-y1 < 0:
                            direction.append("\"up\"")
                            
                    else:
                        if gaugeClicks == True:
                            duration.append(x1)
                            direction.append(y1)
                            isClick.append("\"click\"")
                            
                    if phases == True:
                    
                        lastPhase = (len(duration) + correctionFactor)
                        currentPhase = lastPhase + 1
                        
                        #print("from phases == True: current phase: " + str(currentPhase) + "/nlast Phase: " + str(lastPhase))
                        
                        phaseTables = "\tphase = 0   #"
                        for i in range(0 + correctionFactor, currentPhase):
                            phaseTables += ('{:>10}'.format(i))
                            phaseTables += ','
                        phaseTables += '\n'

                        phaseTables += ("\tduration  = [")
                        for i in duration:
                            phaseTables += ('{:>10}'.format(i))
                            phaseTables += ','
                        phaseTables += ("]\n")

                        phaseTables += "\tdirection = ["
                        for i in direction:
                            phaseTables += ('{:>10}'.format(i))
                            phaseTables += ','
                        phaseTables += ("]\n")

                        if gaugeClicks == True:
                            phaseTables += "isClick   = ["
                            for i in isClick:
                               phaseTables += ('{:>10}'.format(i))
                               phaseTables += ','
                            phaseTables += "]\n"

                        #print(preliminaryData0)
                        #print(phaseTables)
                        #print(preliminaryData1)
                        #print(preliminaryData2)
                        #print(phaseData)
                        
                    else:
                        for i in range(len(duration)):
                            if gaugeClicks == True:
                                if isClick[i] == "\"click\"":
                                    print("fn.click(" + str(duration[i]) + ", " + str(direction[i]) + ")")
                                else:
                                    print("fn.drag(" + str(direction[i]) + ", " + str(duration[i]) + ")")
                            else:
                                print("fn.drag(" + str(direction[i]) + ", " + str(duration[i]) + ")")
                        print("\n\n\n\n\n")
                    break
        
        elif addAction == -127 or addAction == -128:
            
            execution = True
            
            actions =  [fn.VK_CODE['1'],     #open chest   0
                        fn.VK_CODE['2'],     #horror       1
                        fn.VK_CODE['3'],     #battle       2
                        fn.VK_CODE['8'],     #save & exit  3
                        fn.VK_CODE['4'],     #clickbomb    4
                        fn.VK_CODE['5'],     #boss battle  5
                        fn.VK_CODE['6'],     #pause        6
                        fn.VK_CODE['7']]     #waitFor menu 7
            
            print("Please choose the desired action and press the correspoding number to execute:\n\n\t1- click on mark\n\t2- horror\n\t3- battle\n\t4- clickBomb")
            print("\t5- boss battle\n\t6- pause\n\t7- Enter new room\n\t8- save & exit")
            
            # while loop to ensure that only one action is pressed
            while execution == True:
                
                for i in actions:
                    
                    #removing unwanted key presses
                    action = 0
                    
                    action = win32api.GetKeyState(i)
                    
                    if i == actions[0] and (action == -127 or action == -128):
                        
                        print ("adding chest")
                        
                        while True:
                            keyUp = win32api.GetKeyState(i)
                            if keyUp == 0 or keyUp == 1:
                                break

                        strategizing = True
                        
                        print("1-LeaveDoor, 2-Exclamation")
                        while strategizing == True:
                            keyList = ['1', '2']
                            
                            for key in keyList:
                                pressed = win32api.GetKeyState(fn.VK_CODE[key])
                                if pressed == -127 or pressed == -128:
                                    
                                    print("analyzing....")
                                    
                                    while True:
                                        released = win32api.GetKeyState(fn.VK_CODE[key])
                                        if released == 0 or released == 1:
                                            break
                                            
                                    if key == '1':
                                        exclaimCoords, counter = fn.testMarks(fn.LEAVE_DOOR)
                                        if exclaimCoords is not None:
                                            fn.click(exclaimCoords.x, exclaimCoords.y)
                                            fn.waitFor(fn.path + "menu.png", clickUntil=True)
                                        data = "\t\t\ttime.sleep(1)\n\t\t\tfn.waitFor(fn.LEAVE_DOOR["
                                        strategizing = False
                                        break
                                    
                                    elif key == '2':
                                        exclaimCoords, counter = fn.testMarks(fn.EXCLAMATION)
                                        if exclaimCoords is not None:
                                            fn.click(exclaimCoords.x, exclaimCoords.y)
                                            fn.waitFor(fn.path + "menu.png", clickUntil=True)
                                        data = "\t\t\ttime.sleep(1)\n\t\t\tfn.waitFor(fn.EXCLAMATION["
                                        strategizing = False
                                        break

                                    
                        data += str(counter) + "], doClick=True)\n\t\t\tfn.waitFor(fn.path + \"menu.png\", clickUntil=True)\n\n"
                        phaseData, preliminaryData1 = addPhase(data, currentPhase, lastPhase, phaseData, preliminaryData1, duration, correctionFactor)
                        
                        print("finished adding chest")
                        lastPhase += 1
                        execution = False
                        break
                        
                    elif i == actions[1] and (action == -127 or action == -128):
                        print ("adding horror")
                        print("Press \"k\" to end recording")
                        
                        strategizing = True
                        battleList = []
                        
                        while strategizing == True:
                            keyList = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'c', 'v', 'm', 'g', 'k', 'p']
                            
                            for key in keyList:
                                pressed = win32api.GetKeyState(fn.VK_CODE[key])
                                #print(pressed)
                                if pressed == -127 or pressed == -128:
                                
                                    if key == 'k':
                                        strategizing = False
                                        break
                                    
                                    if key == 'p':
                                        print("pause")
                                        battleList.append("pause")
                                    else:
                                        print(key)
                                        battleList.append(key)
                                    
                                    while True:
                                        released = win32api.GetKeyState(fn.VK_CODE[key])
                                        if released == 0 or released == 1:
                                            break
                                            
                                    
                                            
                        old = str(battleList)
                        new = ''
                        
                        for letter in old:
                            if letter == ']' or letter == '[':
                                continue
                            new += letter
                        
                        data = "\t\t\tfn.horror(\"pause\", "  + new + ", \"done\")\n\n"
                        phaseData, preliminaryData1 = addPhase(data, currentPhase, lastPhase, phaseData, preliminaryData1, duration, correctionFactor)
                        
                        print("finished adding horror")
                        lastPhase += 1
                        execution = False
                        break
                        
                    elif i == actions[2] and (action == -127 or action == -128):
                        print("adding battle")
                        print("Type in your strategy. Then press \"k\" to start fighting!")
                                
                        strategizing = True
                        battleList = []
                        while strategizing == True:
                            keyList = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'c', 'v', 'm', 'g', 'k', 'p']
                            
                            for key in keyList:
                                pressed = win32api.GetKeyState(fn.VK_CODE[key])
                                if pressed == -127 or pressed == -128:
                                
                                    if key == 'k':
                                        strategizing = False
                                        break
                                    
                                    if key == 'p':
                                        print("pause")
                                        battleList.append("pause")
                                    else:
                                        print(key)
                                        battleList.append(key)
                                    
                                    while True:
                                        released = win32api.GetKeyState(fn.VK_CODE[key])
                                        if released == 0 or released == 1:
                                            break
                                            
                                    
                                            
                        old = str(battleList)
                        new = ''
                        
                        for letter in old:
                            if letter == ']' or letter == '[':
                                continue
                            new += letter
                                
                        fn.battle("pause", *battleList)
                             
                        data ="\t\t\tfn.battle(\"pause\"," + new + ")\n\n"
                        phaseData, preliminaryData1 = addPhase(data, currentPhase, lastPhase, phaseData, preliminaryData1, duration, correctionFactor)
                        
                        input("press any key to continue...")
                        
                        print("finished battle")
                        lastPhase += 1
                        execution = False
                        break
                        
                    elif i == actions[4] and (action == -127 or action == -128):
                    
                        print ("adding clickBomb")
                        
                        while True:
                            keyUp = win32api.GetKeyState(i)
                            if keyUp == 0 or keyUp == 1:
                                break
                        
                        data = "\t\t\ttime.sleep(1)\n\t\t\tfn.clickBomb()\n\n"
                        phaseData, preliminaryData1 = addPhase(data, currentPhase, lastPhase, phaseData, preliminaryData1, duration, correctionFactor)
                        
                        noMenu = fn.clickBomb()
                        
                        print("finished adding clickBomb")
                        lastPhase += 1
                        execution = False
                        break
                        
                    elif i == actions[5] and (action == -127 or action == -128):
                    
                        print("adding BossBattle")
                        print("Press \"k\" to end recording")
                        
                        strategizing = True
                        battleList = []
                        
                        while strategizing == True:
                            keyList = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'c', 'v', 'm', 'g', 'k', 'p']
                            
                            for key in keyList:
                                pressed = win32api.GetKeyState(fn.VK_CODE[key])
                                if pressed == -128 or pressed == -127:
                                
                                    if key == 'k':
                                        strategizing = False
                                        break
                                    
                                    if key == 'p':
                                        print("pause")
                                        battleList.append("pause")
                                    else:
                                        print(key)
                                        battleList.append(key)
                                    
                                    while True:
                                        released = win32api.GeKeyState(fn.VK_CODE[key])
                                        if released == 0 or released == 1:
                                            break
                                            
                                    
                                            
                        old = str(battleList)
                        new = ''
                        
                        for letter in old:
                            if letter == ']' or letter == '[':
                                continue
                            new += letter
                        
                        data = "\t\t\ttime.sleep(1)\n\t\t\tfn.waitFor(fn.YES, doClick=True)\n"
                        data += "\t\t\tfn.horror(\"pause\", "  + new + ", \"done\")\n\n\t\t\tfn.waitFor(fn.path + \"menu.png\", clickUntil=True)\n"
                        phaseData, preliminaryData1 = addPhase(data, currentPhase, lastPhase, phaseData, preliminaryData1, duration, correctionFactor)
                        
                        print("finished adding BossBattle")
                        lastPhase += 1
                        execution = False
                        break
                        
                    elif i == actions[3] and (action == -127 or action == -128):
                        
                        while True:
                            keyUp = win32api.GetKeyState(i)
                            if keyUp == 0 or keyUp == 1:
                                break
                        
                        endData = "\t\t\t\n\t\t\truns = fn.countRuns(start, times, runs)  \n\t\t\tloop, phase = fn.goAgain(mapName, difficulty, mapNameList, mapIndex, innerMap=innerMapName)\n\t\t\t\n\t\t\n\t\tphase += 1\n\t\t\n\tprint(\"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\")\n\t\nif __name__ == \"__main__\":\n\tphase = input(\"What phase? \")\n\tmain([\"City of Lost Paradise\"], 0, phaseNum=int(phase))"
                        
                        file = open(fn.path + "tempDungeon.txt", 'w')
                        file.write(preliminaryData0)
                        file.write(phaseTables)
                        file.write(preliminaryData1)
                        file.write(preliminaryData2)
                        file.write(phaseData)
                        file.write(endData)
                        file.close()
                        
                        execution = False
                        programState = False
                        
                        quit()
                                
                    elif i == actions[6] and (action == -127 or action == -128):
                        
                        while True:
                            keyUp = win32api.GetKeyState(i)
                            if keyUp == 0 or keyUp == 1:
                                break
                        
                        input("Press any enter to continue...")
                        execution = False
                        break
                    
                    elif i == actions[7] and (action == -127 or action == -128):
                        print ("entering new room")
                        
                        while True:
                            keyUp = win32api.GetKeyState(i)
                            if keyUp == 0 or keyUp == 1:
                                break
                        
                        data = "\t\t\tfn.waitFor(fn.path + \"menu.png\", clickUntil=True)\n\n"      
                        phaseData, preliminaryData1 = addPhase(data, currentPhase, lastPhase, phaseData, preliminaryData1, duration, correctionFactor)
                        
                        print("finished entering new room")
                        lastPhase += 1
                        execution = False
                        break

if __name__ == "__main__":
    main()