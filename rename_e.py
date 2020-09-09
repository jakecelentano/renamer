import os

try:
    from renamer import Renamer
except:
    from renamer_nogui import Renamer
 
def main(): 
    r = Renamer()
    rootFolder= r.getRootFolder()

    r.confirmRename(rootFolder)

    for seasonFolder, innerFolders, episodes in os.walk(rootFolder):
        print(seasonFolder)
        print(innerFolders)
        print(seasonFolder)
        if seasonFolder == rootFolder:
            print("season folder is root folder")
            print("do you want to rename contents of " + seasonFolder)
            userin = input("y/n: ")
            if userin.lower() == "n":
                continue
            else:
                r.confirmRename(rootFolder)
                season = r.getSeason(seasonFolder)   
                r.renames00e000(episodes, season, seasonFolder)
                print(seasonFolder[:300].replace("\\", '/') + seasonFolder[300:])
            
        else:
            season = r.getSeason(seasonFolder)   
            r.renames00e000(episodes, season, seasonFolder)
            print(seasonFolder[:300].replace("\\", '/') + seasonFolder[300:])


if __name__ == '__main__': 
    main()
