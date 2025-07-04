# <img src="https://cdn2.steamgriddb.com/icon/8ddd389dc325faeb9e252d331df22b72/32/256x256.png" alt="Icon" width="40" > R.E.P.O Save Manager

## Overview

**R.E.P.O Save Manager** a lightweight desktop application for managing R.E.P.O. game save files. This tool allows you to easily back up and restore save files, keeping your game progress safe and organized. With simple functionality and automatic save detection, it’s an efficient solution for managing R.E.P.O. saves.

## Screenshot
<img src="https://raw.githubusercontent.com/TiramisuAddict/r.e.p.o-save-manager/refs/heads/main/img.png" alt="app_screenshot" >

## Direct Download

1. Download the latest version from the [Releases page](https://github.com/TiramisuAddict/r.e.p.o-save-manager/releases)
2. Extract the ZIP file to a folder of your choice
3. Run the `.exe` file

## Installation from Source

Before running the source code, make sure you have the following installed:
  - Python 3.x (preferably the latest version)
  - `pip` for installing dependencies
> **Optional but recommended** : Create and activate a virtual environment

1. **Clone the repository :** <br><br>
   ```sh
     git clone https://github.com/TiramisuAddict/r.e.p.o-save-manager.git
     cd r.e.p.o-save-manager
   ```
3. **Install dependencies :**<br><br>
   ```sh
    pip install -r requirements.txt
   ```
4. **Run the application :**<br><br>
   ```sh
     python main.py
   ```
The application is written in Python using PyQt5. The project structure is:

```
r.e.p.o-save-manager/
├── app.ui                # User interface
├── main.py               # Source code
├── repo.ico              # App icon
├── decrypt.py            # Decryption code
└── requirements.txt      # Dependencies
```
