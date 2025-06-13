import time, sys, threading, win32gui
import functionScripts2 as scripts
import updateByPass, mapChooser
import _user_console_ as uc

def main():
    
    time.sleep(10)
    
    fn = scripts.AEWindow("LDPlayer", "RenderWindow", uc.script_path + "img\\", "gl")

    fn.waitFor(fn.path + "ldStore.png")
    fn.press('f11')
    time.sleep(2)
    fn.click(1198, 228)

    param = sys.argv

    updateByPass.timeLoop()

    try:

        p = param[3].lower()

        if p == "false" or p == "f":
            print("No Dungeon")
    except:
        mapChooser.main()

if __name__ == "__main__":
    main()