import os
try:
    from renamer import Renamer
except:
    from renamer_nogui import Renamer

def main():
	r = Renamer()
	rootFolder = r.getRootFolder()
	r.confirmRename(rootFolder)
	print('Renaming conetents of ' + rootFolder)

	for movieFolder, innerFolder, movieFolderFiles in os.walk(rootFolder):

		movieName = r.getFolderNameFromPath(movieFolder)

		for file in movieFolderFiles:

			if os.path.isdir(file):
				continue
			else:
				extension = r.getFileExtension(file)
				src = os.path.join(movieFolder + '/' + file)
				dst = os.path.join(movieFolder + '/' + movieName + extension)
				print(src)
				print(dst)

				try:
					os.replace(src, dst)
				except OSError as e:
					raise e
					continue

		return 1
				

if __name__ == '__main__': 
    main() 