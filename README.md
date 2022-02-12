# Description
The script deletes versions of minecraft what makes TLauncher.
Just my son likes to install lot of version the game and mod packs into his TLauncher on my PC.
Python version 3.9 (i think it can to work in all versions Python3)

# How to configure
1. Create a file "root_path.txt" at the root repo directory on your PC
2. Text a path to your 'versions' minecraft directory (my path is that: C:/Users/myProfile/AppData/Roaming/.minecraft/versions)
3. Create a file "versions_to_save.txt"
4. Text lines with versions (name of version folder, for example: 1.18.1). One version on a row.

# How to use
Just start a 'main.py' script.

You can to start it from comandline: python ./main.py (or write full path to the file)

You need to have Python in your system. 

# How to compile .exe
You need to install pyinstaller or different compilator (pip install pyinstaller).

Use "pyinstaller -F main.py" at console in your repo directory.

It will make "main.exe" file at inner directory "dist".

Enjoy!
