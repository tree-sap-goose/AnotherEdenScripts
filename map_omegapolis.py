import time
import functionScripts2 as scripts
import _user_console_ as uc


def main(mapNameList, mapIndex, phaseNum=0):

    fn = scripts.AEWindow("LDPlayer", "RenderWindow", uc.script_path + "img\\", "gl")

    mapName = "omegapolis"
    mapEra = "hollow"
    continent = "metallanica"
    difficulty = "hard"
    innerMapName = None

    runs = 0
    start = time.time()
    times = []

    phase = phaseNum#     0,         1,         2,         3,         4,         5,         6,         7,         8,         9,        10,        11,        12,        13,        14,        15,        16,        17,        18,        19,        20,        21,        22,        23,        24,        25,        26,        27,        28,        29,        30,        31,        32,        33,        34,        35,        36,        37,        38,        39,        40,        41,        42,        43,        44,        45,        46,        47,        48,        49,        50,        51,        52,        53,
    duration  = [     1.053,       1.3,    15.567,     3.228,     0.948,       1.3,     1.193,     3.485,       1.3,      1.03,     2.202,     1.108,       1.3,     3.672,     0.997,       1.3,      2.25,       1.3,     1.381,      3.33,       1.3,     1.637,     6.479,     0.802,       1.3,      0.83,     0.764,       1.3,     1.488,     1.045,       1.3,     2.772,     6.582,      1.73,       1.3,     1.166,       1.3,     2.299,     1.093,       1.3,     1.117,       1.3,     0.964,     0.871,       1.3,     3.177,       1.3,       1.3,     1.145,       1.3,     1.044,       1.3,     2.876,]
    direction = [   "right",    "down",    "left",   "right",    "left",      "up",   "right",    "left",      "up",    "left",   "right",    "left",    "down",    "left",   "right",    "down",    "left",    "down",    "left",   "right",    "down",    "left",   "right",    "left",      "up",   "right",    "left",    "down",   "right",   "right",      "up",    "left",   "right",   "right",      "up",    "left",      "up",    "left",   "right",      "up",    "left",      "up",   "right",    "left",    "down",    "left",    "down",      "up",   "right",      "up",    "left",      "up",    "left",]

    loop = True

    if phase == 0:
        fn.validateParty("greenCard")
        '''
        Member:     Yukino AS
        
        -------------------------------------Grasta--------------------------------------
        G1:         Spell:
        G1u:
        
        G2:
        G2u:
        
        G3:
        G3u:
        
        G4:
        G4u:
        
        ------------------------------------Equipment-------------------------------------
        Weapon:
        
        Armor:
        
        Badge1:
        Badge2:
        
        ------------------------------------Skills-----------------------------------------
        s1:
        
        s2:
        
        s3:
        
        s4:
        '''

        if mapIndex == 0:
            loop, phase = fn.returnToDungeonGates(mapName, mapEra, continent, mapNameList, mapIndex, innerMapName, True, difficulty)

        else:
            loop, phase = fn.changeDungeon(mapName, mapEra, continent, mapNameList, mapIndex, innerMapName, True, difficulty)


    while loop == True:

        print("---------------------phase", end=' ')
        print(phase, end="---------------------\n")
        
        if phase < 0:
            fn.waitFor(fn.path + "menu.png")
            time.sleep(3)
        
        if phase >= 0:
            if direction == "up" or direction == "down":
                fn.drag(direction[phase], 0.1)
                time.sleep(1.3)
            else:
                fn.drag(direction[phase], duration[phase])

        if phase == 2:
            time.sleep(1)
            fn.clickBomb()
            
        elif phase == 3:
            time.sleep(1)
            fn.waitFor(fn.EXCLAMATION[2], doClick=True)
            fn.waitFor(fn.path + "menu.png", clickUntil=True)

        elif phase == 5:
            fn.horror("pause", 'a', 'e', 's', 'e', 'd', 'e', 'f', 'r', 'g', "done")

        elif phase == 6:
            time.sleep(1)
            fn.clickBomb()

        elif phase == 9:
            time.sleep(1)
            fn.clickBomb()
            
        elif phase == 10:
            time.sleep(1)
            noVines, vineCoords = fn.waitFor(fn.path + "omegapolisVines.png", grayscale=False, confidence=0.8, timeout=3)
            print(vineCoords)
            if noVines == True:
                fn.drag("up", 0.1)
                time.sleep(1.1)
                
                fn.waitFor(fn.EXCLAMATION[2], doClick=True)
                fn.waitFor(fn.path + "menu.png", clickUntil=True)
                
                fn.drag("down", 0.1)
                time.sleep(1.1)
                
                fn.drag("left", 1.076)
                phase = 11

        elif phase == 13:
            time.sleep(1)
            fn.clickBomb()

        elif phase == 15:
            fn.horror("pause", 'g', "done")

        elif phase == 18:
            time.sleep(1)
            fn.clickBomb()

        elif phase == 19:
            fn.horror("pause", 'g', "done")

        elif phase == 20:
            fn.horror("pause", 'g', "done")

        elif phase == 21:
            time.sleep(1)
            fn.clickBomb()

        elif phase == 22:
            time.sleep(1)
            fn.clickBomb()

        elif phase == 25:
            time.sleep(1)
            fn.clickBomb()

        elif phase == 28:
            time.sleep(1)
            fn.waitFor(fn.EXCLAMATION[2], doClick=True)
            fn.waitFor(fn.vspath + "cancel.png")
            time.sleep(2)
            fn.click(612, 782)
            fn.waitFor(fn.path + "menu.png")

        elif phase == 30:
            time.sleep(1)
            fn.waitFor(fn.vspath + "yes.png", doClick=True)
            fn.waitFor(fn.path + "menu.png", clickUntil=True)

        elif phase == 31:
            time.sleep(1)
            fn.waitFor(fn.EXCLAMATION[0], doClick=True)
            fn.waitFor(fn.path + "menu.png", clickUntil=True)

        elif phase == 32:
            time.sleep(1)
            fn.waitFor(fn.EXCLAMATION[0], doClick=True)
            fn.waitFor(fn.path + "menu.png", clickUntil=True)

        elif phase == 34:
            fn.horror("pause", 'pause', 'g', "done")

        elif phase == 37:
            time.sleep(1)
            fn.waitFor(fn.EXCLAMATION[0], doClick=True)
            fn.waitFor(fn.path + "menu.png", clickUntil=True)

        elif phase == 42:
            time.sleep(1)
            fn.waitFor(fn.EXCLAMATION[0], doClick=True)
            fn.waitFor(fn.path + "menu.png", clickUntil=True)

        elif phase == 46:
            fn.horror("pause", 'g', "done")

        elif phase == 51:
            time.sleep(1)
            fn.waitFor(fn.EXCLAMATION[10], doClick=True)
            fn.waitFor(fn.path + "menu.png", clickUntil=True)

        elif phase == 52:
            fn.waitFor(fn.vspath + "yes.png", doClick=True)
            fn.horror("pause", 'm', 'e', 'e', 'e', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', "done")

            fn.waitFor(fn.path + "menu.png", clickUntil=True)

            runs = fn.countRuns(start, times, runs)
            loop, phase = fn.goAgain(mapName, difficulty, mapNameList, mapIndex, innerMap=innerMapName)

        phase += 1

if __name__ == "__main__":
    phase = input("What phase? ")
    index = input("Index? ")
    main(["Omegapolis"], int(index), int(phase))