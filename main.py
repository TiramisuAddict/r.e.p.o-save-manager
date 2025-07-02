from PyQt5.QtWidgets import QApplication,QFileDialog,QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon

from os import getlogin,walk,path,mkdir
import shutil
from decrypt import decrypt_es3
import json

app = QApplication([])
w = loadUi("app.ui")
w.show()

icon = QIcon('./repo.ico')
w.setWindowIcon(icon)

default_path = "C:\\Users\\" + getlogin() + "\\AppData\\LocalLow\\semiwork\\REPO\\saves"
w.default_path_label.setText(default_path)

backup_folder_path = "C:\\Users\\" + getlogin() + "\\Documents\\R.E.P.O_saveFiles"

global saveFiles
saveFiles = []

def select_folder():
        folder_path = QFileDialog.getExistingDirectory(w, "Select Folder")
        if folder_path:
            w.default_path_label.setText(folder_path)
            default_path = folder_path

def getSaveFiles():
        saveFiles.clear()
        if not (path.isdir(backup_folder_path)):
                try :
                        mkdir(backup_folder_path)
                except FileExistsError:
                        print(backup_folder_path," already exists.")

        dest_folder_path = backup_folder_path
        shutil.copytree(default_path, dest_folder_path ,dirs_exist_ok=True)
        print("operation done from \n ",default_path, " \n to ",dest_folder_path)

        box = QMessageBox(QMessageBox.Information, "R.E.P.O Save Manager", "Your backup has been successfully created \nYou can find it in: \nDocuments > R.E.P.O_saveFiles.")
        box.setWindowIcon(icon)
        box.exec_()

        loadBackupSaves()

def open_file(file_path, index):
        global json_data
        if file_path:        
                decrypted_data = decrypt_es3(file_path, "Why would you want to cheat?... :o It's no fun. :') :'D")
                json_data = json.loads(decrypted_data)
                
                level = json_data['dictionaryOfDictionaries']['value']['runStats']["level"]
                timePlayed = json_data['timePlayed']["value"]
                dateAndTime = json_data['dateAndTime']["value"]
                teamName = json_data['teamName']["value"]

                playerNames = list(json_data['playerNames']["value"].values())
                
                save = { "index" : index,
                        "path" : file_path,
                        "name" : teamName,
                        "level" : level,
                        "playtime" : timePlayed,
                        "date" : dateAndTime,
                        "players" : playerNames}
                
                return save

def updateSaveListGUI(saveFiles):
        w.saveListB.clear()
        for i in range (len(saveFiles)) :
                w.saveListB.addItem(str(saveFiles[i]["name"])+" | Level : "+str(saveFiles[i]["level"]))
        
def seconds_to_hours_minutes(total_seconds):
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    return int(hours), int(minutes)

def updateNamesListGUI(index):
        w.namesListB.clear()
        for i in range (len(saveFiles)) :
                if saveFiles[i]["index"] == index :
                        for j in range(len(saveFiles[i]["players"])):
                                w.namesListB.addItem(str(saveFiles[i]["players"][j]))
                        w.saveName_.setText(str(saveFiles[i]["name"]))
                        w.saveLevel_.setText("Level : "+str(saveFiles[i]["level"]))
                        w.saveDate_.setText(str(saveFiles[i]["date"]))
                        h,m = seconds_to_hours_minutes(saveFiles[i]["playtime"])
                        w.savePlayTime_.setText(str(h)+"h : "+str(m)+"mins")
                
def loadBackupSaves():
        if path.isdir(backup_folder_path):
                k = 0
                for root, dirs, files in walk(backup_folder_path, topdown=True):
                                for name in files:
                                        if name.endswith(".es3"):
                                                if path.join(root, name).find("BACKUP") == -1:       
                                                        save = open_file(path.join(root, name),k)
                                                        saveFiles.append(save)
                                                        k += 1
                updateSaveListGUI(saveFiles)
                #print(saveFiles)

def clearGUIAndFolder():
        saveFiles.clear()
        w.namesListB.clear()
        w.saveListB.clear()
        try :
                shutil.rmtree(backup_folder_path)
        except FileNotFoundError:
                box = QMessageBox(QMessageBox.Warning, "R.E.P.O Save Manager", "Nothing to delete."); box.setWindowIcon(icon); box.exec_()


def restoreSave() :
        try :
                row = w.saveListB.currentRow()
                source_path = path.dirname(saveFiles[row]["path"])
                dest_path = default_path
                shutil.copytree(source_path, dest_path+"\\"+source_path[source_path.find("REPO"):] ,dirs_exist_ok=True)
                box = QMessageBox(QMessageBox.Information, "R.E.P.O Save Manager", "Save file restored."); box.setWindowIcon(icon); box.exec_()
        except IndexError:
                box = QMessageBox(QMessageBox.Warning, "R.E.P.O Save Manager", "No selected save to restore."); box.setWindowIcon(icon); box.exec_()

def restoreAllSaves() :
        if saveFiles == []:
                box = QMessageBox(QMessageBox.Warning, "R.E.P.O Save Manager", "No save files to restore."); box.setWindowIcon(icon); box.exec_()
        else :
                for i in range(len(saveFiles)):
                        source_path = path.dirname(saveFiles[i]["path"])
                        dest_path = default_path
                        shutil.copytree(source_path, dest_path+"\\"+source_path[source_path.find("REPO"):] ,dirs_exist_ok=True)
                box = QMessageBox(QMessageBox.Information, "R.E.P.O Save Manager", "All save files restored."); box.setWindowIcon(icon); box.exec_()

loadBackupSaves()
w.game_path_button.clicked.connect(select_folder)
w.backupButton.clicked.connect(getSaveFiles)
w.clearButton.clicked.connect(clearGUIAndFolder)
w.restoreallButton.clicked.connect(restoreAllSaves)
w.restoreButton.clicked.connect(restoreSave)
w.saveListB.currentRowChanged.connect(updateNamesListGUI)

app.exec_()