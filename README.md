# ANOTHER EDEN DUNGEON SCRIPTS
User Guide

## I. Introduction
The purpose of this code base is to automate the repetitive parts of Another Eden: The Cat Beyond Space and Time. This will allow the user to spend more time with the story and challenge the more engaging content. Though the user cannot use their account while the scripts are running, they can still use their computer to do other things.
## II. Terminology
Below lists how this guide denotes certain actions and items.

|***Action/Item***|***Denotation***|
|:------------------------------------|----------------------|
|Keys to press on the keyboard|“Key”|
|Key combinations to press on keyboard|“Key + Key”|
|Buttons/clickable items|“Button Name”|
|Item name to look for|“Item Name”|
|File names|filename.extention|
|Folder name|folder name|
|Code snippet|        print(“code”)|
|User inputs|User Input|
|Sections|**I.**, **II**., **III**...|
|Parts|A., B., C....|
|Steps|1-, 2-, 3-...|

Table 1: Terminology formatting used in this guide.
## III. System Requirements

|***Minimum***|***Recommended***|
|:------------------------------------|----------------------|
|Intel / AMD Processor x86 / x86_64|AMD Ryzen 5 1600 or better|
|Windows XP|Windows 10|
|Windows DirectX 11 / Graphics Driver with OpenGL 2.0|Nvidia GeForce GTX 970 or better|
|2 GB system memory (RAM)|16 GB system memory (RAM) or better|
|50 GB of free drive space|100 GB or more of free drive space|

Table 2: System Requirements.
## IV. Setup
This section details how to setup a system to run this code base from scratch. It assumes the user is has none of the software installed on their system.
### A. Installing LDPlayer9
LDPlayer9 is an emulator which mimics an Android phone environment. It allows the user to use Android applications on their Windows computer.
1. Download  the installer [https://www.ldplayer.net/].
2. Double click on the downloaded installer. Make note of the download path by clicking on “Setup path”. LDPlayer will open when it is done downloading.
4. Click on the hexagon with a dot (settings) on the right tool bar. Set DPI to 1600x900.
5. Change wallpaper to solid black. A solid black background can be procured by opening paint program, filling it in black, and saving it.
### B. Installing Another Eden
1. Install the XAPK file from APKPure ["https://d.apkpure.com/b/XAPK/games.wfs.anothereden?version=latest"].
2. Drag and drop the XAPK file into LDPlayer. A “parsing...” popup will show up in the bottom-right corner of the screen. Another Eden will appear on the home screen when it is done downloading.
### C. Installing Microsoft Infrastructure.
The image processing package requires Microsoft Redistributable 2015-2022 and Microsoft Media Feature Pack.
1. Install Microsoft Redistributable 2015-2022 
	1. Download the installer form Microsoft [https://aka.ms/vs/17/release/vc_redist.x86.exe].
	2. Complete the system reboot.
2. Install Microsoft Media Feature Pack
	1. Open (Windows) Settings.
	2. Type Add an Optional Feature in search bar and click on it.
	3. Type Media Feature Pack in the search bar. If it appears in the list below the search bar, it is already installed; Continue to the next section.
	4. Click on “Add a Feature”.
	5. Search and select Media Feature Pack. Click “Add”.
	6. Complete a system reboot. There will be no prompt for a reboot however, it is required for the changes to fully take place.
### D. Installing Python
Python is the language all the scripts use. To ensure everything runs smoothly, it is recommended to use same version that the scripts were coded in (as of this time: 3.10.9)
1. Download Python 3.10.9 [https://www.python.org/downloads/release/python-3109/].
2. In the installer window, check “Add python.exe to PATH”.
3. Click on Customize installation. Ensure the following are checked:
    • “pip”
    • “tcl/tk and IDLE”
    • “Python test suite”
    • “pylauncher”.
Though it is not a requirement, it is recommended to download python for all users and as an admin. Click “Next”.
4. Ensure the following are checked:
    • “Associate files with Python (requires the ’py’ launcher)”
    • “Add Python to environment variables”
    • “Precompile standard library”.
      Once again, it is recommended to install for all users. Click “Install”.
5. Open command prompt by pressing “Win”, typing cmd, and pressing “Enter”. Type in python and press “Enter”. If the command prompt switches to a python terminal, the installation was successful. Type quit() to exit.
6. Type in the following into the open command prompt:
pip install pywin32 numpy pillow pyscreeze pyautogui pytesseract opencv-python opencv-contrib-python

### E. Downloading the Scripts
There are some modifications the user needs to make to their local installation before the scripts can run.
1. Navigate to https://github.com/tree-sap-goose/AnotherEdenScripts 
2. Click on the green “<> Code” button. Download the zip file.
3. Unzip the code base. It is recommended to extract into “Documents” or another user folder.
4. Open _user_console_.py with any text editor. Type in the path where the files were extracted to. The path name must have all double forward slashes and much end with a pair of forward slashes. For example: C:\\Users\\tree-sap-goose\\AnotherEdenScripts-main\\. If there are any spaces in the path name, it must be encased in quotes: “C:\\Users\\Tree Sap Goose\\AnotherEdenScripts-main\\”. Save and close the file.
5. Open StartRunsGL.bat in a text editor. Confirm the LDPlayer path is as noted in section IV part A  step 2. Replace “C\....\AnotherEdenScripts” with the path input into _user_console_.py. Save and close the file.
6. Move the files in virtual keyboard to “...\LDPlayer\LDPlayer9\vms\customizeConfigs”.
## V. Using the Scripts
This section explains how to use the scripts. There are two sample dungeons provided as a baseline. The user will need to edit these to fit the play style of their party. It is recommended to use  getDurations_v2.py to remake the sample dungeons.
### A. Running Scripts with Python
1. Double click StartRunsGL.bat. A command prompt will open up. Ldplayer will also start up.
2. (Optional) Right-click the command prompt window bar, click on “Properties”, click on the “Color” tab, and set the opacity slider to around 80%. 
3. (Optional) Press “f11” to make the command prompt full screen.
4. If the program hangs for more than 2 minutes, see Section VI.
### B. Using getDurations_v2.py to Create Dungeon Scripts
getDurations_v2.py .allows the user to create their own dungeon map and strategies without needing too much coding knowledge.  As it gets updated, the goal is for the usage to require 0 coding knowledge.
1. Run Another Eden in LDPlayer. Navigate until in the dungeon that needs a script. For instance, if making a dungeon for “The Lost City of Paradise”, the user should be in “Lunar Ghost City . Area Brigitte”. This is the starting map for the dungeon and not the “Spacetime Rift”.
2. Double click getDurations_v2.py. It will open another command prompt.
3. Answer the first prompt, “What phase are we staring on?”, with “0”. 
4. Answer the second prompt, “Would you like to gauge clicks? (y/n)”, with “n”.
5. Answer the final prompt, “do u want phases? (y/n)”, with “y”.
6. Do not to make any movements outside of running the dungeon-. All actions are now being logged by getDurations_v2.py and will be replicated in the resulting dungeon script.
7. Drag the mouse right, left, up, or down to create a movement log.
8. Press “z” to being up the actions menu. The actions menu encompasses all other actions that are not movement related. This includes actions like opening a chest, encountering (and defeating) a horror, moving to a new room, etc. 
9. Press“8” in the action menu to save the dungeon and exit. The script creates a dungeon file called TempDungeon.txt in the img\gl directory.
10. Rename TempDungeon.txt to map_dungeonname.py, replacing “dungeonname” with the actual dungeon name.
11. Move map_dungeonname.py to the main directory, AnotherEdenScripts/ or AnotherEdenScripts-main/.
12. Open  map_dungeonname.py with a text editor. Enter the correct map information into lines 9 – 13 of the document using the definitions in Table 4 (below). Available continents and maps are in the “Image Folder Path”. The “Naming Scheme” denotes how the files are queried by the scripts. See Section VI Part 1 for adding new maps and images.

|***Data name***|***Description***|***Image Folder Path***|***Naming Scheme***|
|:----|----|----|----|
|mapName|Dungeon name used when naming the dungeon script. Ex: for map_industrialruins.py, use “industrialruins”|/img/gl/maps/|Prefix: map_|
|mapEra|Dungeon era. The keys are as follows: Antiquity:“past”; Future:“future”; Hollow:“hollow”; Present:“present”; ???:“timestop”|N/A|N/A|
|continent|Dungeon continent. This data point is used to find the continent in game. The continents are spelled the way they are in game. Ex: for “Zerberiya Continent”, use “zerberiya”|/img/gl/maps|Prefix: continent_|
|difficulty|Dungeon difficulty. The two options are “hard” and “veryHard”. “hard” means green card, while “veryHard” means red card.|N/A|/NA|
|innerMapName|This map is inside another map. For example, “Snake Liver Damaku” is “Snake Bone Island”’s inner map.|/img/gl/maps|Prefix: map_|

Table 3: Dungeon script data block descriptors.

13. Go to line 26 in  map_dungeonname.py. Fill the quotes with the party name that will run the dungeon. If the party in /img/gl/partys/ is “party_redCard.png”, type redCard. To add party to image library, see section VI part A.  
14. The file can now be ran from the command prompt by typing the following one after the other: 
cd “C:/.../AnotherEdenScripts” 
map_dungeonname
15. To run the dungeon from StartRunsGL.bat, open mapChooser.py in a text editor.
16. Copy and paste the Omegapolis block in the main function like so:
		
		elif mapNameList[mapIndex] == "Omegapolis":
			
            print("~~~~~~~~~~~~~~~~~~~~~~ Omegapolis ~~~~~~~~~~~~~~~~~~~~~~~")
            import map_omegapolis
            map_omegapolis.main(mapNameList, mapIndex)
            mapIndex += 1
			
		elif mapNameList[mapIndex] == "Omegapolis":
			
            print("~~~~~~~~~~~~~~~~~~~~~~ Omegapolis ~~~~~~~~~~~~~~~~~~~~~~~")
            import map_omegapolis
            map_omegapolis.main(mapNameList, mapIndex)
            mapIndex += 1


	Edit the second block to the other dungeon. For Industrial Ruins:
		
		elif mapNameList[mapIndex] == "Industrial Ruins":
			
            print("~~~~~~~~~~~~~~~~~~~~ Industrial Ruins ~~~~~~~~~~~~~~~~~~~~")
            import map_industrialruins
            map_industrialruins.main(mapNameList, mapIndex)
            mapIndex += 1

16. Edit the mapNameList at the top of the main function to include the new map. 
		
		mapNameList = ["City of Lost Paradise", "Omegapolis"]
	
		mapNameList = ["Industrial Ruins", "Omegapolis"]
	
	The name of the map must be the same as the name used in the block. It is also important to note that two red card dungeons being in the same list is not supported. The first red card dungeon will use all the cards, and the second one will not run. The same goes for green card dungeons. Save and close the file.
17. Double click StartRunsGL.bat. The new dungeon will run.
### C. (Optional) Setting up Automatic Dungeon Runs
The purpose of StartRunsGL.bat, mapChooser.py, and updateByPass.py is to allow for daily automated dungeon runs. This can be setup using only Window’s software, however does require registry edits. This section requires administer privileges, and is entirely optional.
1. Set up a daily startup time BIOS. This will differ from computer to computer. Defer to the specific BIOS manual. It is recommended to start 10 mins after the Lynx delivery service.
2. Press “Win”, type Task Scheduler, and press “Enter”.
3. Click on “Add a Basic Task” from the Actions pane on the right.
4. Fill out the name and description. Click “Next”.
5. Select “Daily” for the frequency. Click “Next”.
6. Set the start date to tomorrow. Make sure “Recur every:” is set to “1”. It is recommended to set the time to 10 mins after the BIOS startup time. Click “Next”.
7. Select “Start a Program”. Click “Next”.
8. Browse for StartRunsGL.bat in the “Program/script” field. Leave the optional fields blank. Click “Next”.
9. Click “Finish”.
10. Press “Win”, type regedit, and press “Enter.
11. Click on “File”, and then “Export”. Save the current registry as a backup.
12. Navigate to “HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon” using the file explorer on the left, and double click “WinLogon”.
13. In the right pane, look for “AutoAdminLogon”, “DefaultDomainName”, “DefaultPassword”, and “DefaultUserName”. 
14. If any of the four are missing, simply click on “Edit” in the top toolabr, select “New”, and click on “String Value”. In the resulting popup, type the name of the missing value in “Value Name”. It must match exactly the way the values are written in step 13 of this part. Press “OK”. Repeat this step until all four values are present in the right pane.
14. Double click “AutoAdminLogon”. Change the “Value Data” to 1. Press OK.
15. Press “Win”, type “system information”, and press “Enter”. Note the value of “System Name”. 
16. In the registry editor, Double click “DefaultDomainName”. Change the “Value Data” to the system name in step 14. Press OK.
17. Double click “DefaultUserName”. Change the “Value Data” to the username of the account that will be running the scripts. Make certain this is a local standard account. It is a security risk to have any other account take this role. Press OK.
18. Double click “DefaultPassword”. Change the “Value Data” to the password of the account that will be running the scripts. Press OK
19. Close the registry editor. Tomorrow, the dungeons will run.
## VI. Gathering Data
This section explains how to add data to the scripts. Currently, there is only one category of data: Images. This section may expand in the future, however.
### A. Building an Image Library
This part focuses on getting images. The user may want to add images because they would like to run the scripts at a different resolution (current library only supports 1920x1080), or the user is creating a new map (See section V part B) that has elements that the image library lacks.
1. Run Another Eden with LDPlayer.
2. Navigate to the screen with the desired image.
3. Press “Win”, type Snipping Tool, and press “Enter”.
4. Click on “New”. Make a box around the desired image.
5. Press “Ctrl+S”. If the image is already in the library, overwrite that image. For all other images, refer to Table 5 (below) on where to save and naming conventions. To use saved images, use fn.path + “image.png” or fn.path + “gl\\image.png”

|***Image Type***|***Folder Path***|***Naming Scheme***|
|:----|----|----|
|Place/Map name, continent name, etc|See Table 3 Section V Part B Step 11|See Table 3 Section V Part B Step 11|
|Party names|/img/gl/partys/|Prefix: party_|
|Phantom Crystal Dimension Room|/img/|Prefix: pcd_|
|Images with words|/img/gl/|NA|
|All other images|/img/|NA|

Table 5: Save locations and naming conventions for image library.