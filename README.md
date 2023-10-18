# errorParser

errorParser.py program finds and extracts error messages from ".tzlog" files in a specified folder. This program aims to help support staff quickly identify users' problems, making it easier to troubleshoot issues.


## running the script:


use the following command in the proper terminal window:

```powershell
python errorParser.py
```



you will be prompted for a path, copy and enter the path from the folder you want to read the .tzlogs in into the terminal.

a new folder will be created in the designated path with all occuring error messages (No Model | Make lines are excluded to bypass always present error message in current tzlog files)


you can reference the FLOWCHART for a diagram on how the program is intended to operate.

---



### userFolderExample practice:


use userFolderExample and navigate to '**1 logs/2 tzLogs/downloadedLogFiles**'

you can copy the path to '**2 tzLogs**' after running the `python errorParser.py` in the terminal from the errorParser folder.

a new folder '**notes**' will be created in '**2 tzLogs**' folder and will have the file **tzNotes.txt** with the parsed through error message information.


[loom example](https://www.loom.com/share/8b66be96cb764a009cc5946f1a9e16d5?sid=9d8ed4e3-265f-4d36-81f3-17ffa597072a "loom video example")

---



#### future development example:

try running the same workflow but using the 'Installer Log.txt' in **'1 logs/1 installationLogs/'** notice that it still outputs a folder with the tzNotes.txt file but it is empty. would need to work to allow reading .txt files etc. this could also be adapted for other files and other patterns in search terms.

---



#### notes:

all current programs are created inside .toolkit

the program .createUser currently creates the folder structure used in userFolderExample

probably should integrate .errorParser into .createUser but haven't gotten to it just yet because you know life and all other type of things but whatever.

---
