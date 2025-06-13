import functionScripts2 as scripts
import time, os, datetime, traceback, win32api
import _user_console_ as uc


def main():
    
    fn = scripts.Window("LDPlayer", "RenderWindow", uc.script_path + "img\\", "gl")
    
    win32api.SetCursorPos((0,0))

    smooth_sailing = True
    
    mapIndex = 0
    
    if fn.version == "gl":
        mapNameList = ["City of Lost Paradise", "Omegapolis"]
    
    #JP is no longer supported; keeping code here incase its picked up again.
    '''
    elif fn.version == "jp":
        mapNameList = ["City of Lost Paradise", "Underworld"]
    '''
    
    print(mapNameList)

    while smooth_sailing == True:

        if mapIndex > len(mapNameList):
            smooth_sailing = False
            break

        if mapNameList[mapIndex] == "City of Lost Paradise":

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~ City of Lost Paradise ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            import map_lua
            map_lua.main(mapNameList, mapIndex)
            mapIndex += 1
            
        elif mapNameList[mapIndex] == "Omegapolis":

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Omegapolis ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            import map_omegapolis
            map_omegapolis.main(mapNameList, mapIndex)
            mapIndex += 1
  

if __name__ == "__main__":
    main()