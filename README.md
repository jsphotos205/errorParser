# errorParser

the errorParser.py program is a tool specifically designed to locate and extract error messages from ".tzlog" files within a designated folder.

its primary aim is to facilitate the support staff's quick identification of user issues, simplifying the troubleshooting process.

the errorParser.py program finds and extracts error messages from ".tzlog" files in a specified folder.

---

## using errorParser

before using errorParser.py you must have python installed on your system.

run the program by following these steps:

1. **navigate to the errorParser folder** in your terminal.
2. run the following command:

```powershell
python errorParser.py
```

1. a prompt will appear in your terminal window, requesting you to enter the targeted folder path

```powershell
enter targeted folder path:
```

1. enter the path to the folder containing the ".tzlog" files you want to process.

once entered a new folder named 'notes' will be generated within the targeted folder. inside this 'notes' folder, you will find a file named 'tzNotes.txt'.

* it is important to note that some error messages are intentionally excluded from 'tzNotes.txt'. for instance messages like "No Model" or "Make" "lines are excluded to bypass always present error messages in current .tzlog files.

---

you can reference the FLOWCHART for a diagram on how the program is intended to operate.

---

## userFolderExample

use the provided 'userFolderExample' to illustrate how to use errorParser.py

### pathing userFolderExample:

1. navigate to the 'userFolderExample'
2. navigate to '1 logs/2 tzLogs/downloadedLogFiles'
   1. these downloadedLogFiles are already provided in the example
3. copy the path to '2 tzLogs' after running the `python errorParser.py` command in the terminal from the errorParser folder.

a new folder 'notes' will be created in the '2 tzLogs' folder

* in the new folder 'notes' there will be a the file 'tzNotes.txt', even if it remains empty.

this program can be futrher adapted to handle various file types and search patterns.

---

for a practical example, you can watch this [loom video example](https://www.loom.com/share/8b66be96cb764a009cc5946f1a9e16d5?sid=9d8ed4e3-265f-4d36-81f3-17ffa597072a "loom video example").

---

## Notes

* all current programs are located inside the .toolkit folder.
* the program '.createUser' is responsible for creating the folder structure used in 'userFolderExample'.
  * further development may integrate '.errorParser' into '.createUser'
    * this would streamline the process for added convience

however, this is a work in progress, influenced by the unpredictabiiteies of life and various other factors.

---
