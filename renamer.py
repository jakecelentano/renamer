import tkinter as tk
from tkinter import filedialog
import os


class Renamer():

    def __init__(self):
        super(Renamer, self).__init__()

    file_path = ""

    def getRootFolder(self):
        root = tk.Tk()
        root.withdraw()
        root_folder = filedialog.askdirectory()

        return root_folder

    def getSeason(self, seasonFolder ):
        try:
            season = seasonFolder.lower().split("season ")[1]
        except IndexError as e:
            print("Format your season dir as Season XX")
            exit()

        if not season.isdigit():
            print("Unable to get season name from: " + seasonFolder)
            exit()

        if len(season) == 1:
            season = "s0" + season
        else:
            season = "s" + season

        return season


    def getFileExtension(self, file):
        temp = file.split(".")
        extension = "." + temp[len(temp)-1]

        return extension

    def renames00e000(self, episodes, season, seasonFolder):
        count = 0

        for episode in episodes:
            extension = self.getFileExtension(episode)

            if episode.split(".")[0] == 's01e001':
            	print('alraedy been renamed - first episode is named s01e001')
            	exit()
            
            src = os.path.join(seasonFolder + '/' + episode)

            dst = season +  'e' + (f'{count+1:03}') 
            dst = os.path.join(seasonFolder + '/' + dst + extension)
            count+=1
            print(dst+extension)
            os.rename(src, dst)


    def getFolderNameFromPath(self, folderName):
        return os.path.basename(os.path.normpath(folderName))


    def confirmRename(self, rootFolder):
        confirm = input("Are you sure you want to rename all files in " + rootFolder + "?" + '\n' + "Type yes to continue:")

        if confirm.lower() != 'yes':
            print("Exiting - response: " + confirm)
            exit()
        else:
            return 1
  
