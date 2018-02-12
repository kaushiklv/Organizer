#############################################################
# Author: Kaushik L V										#
# RollNo: 20172138											#
# Email : kaushik.lv@students.iiit.ac.in 					#
#############################################################

import os
import operator
import shutil
import sys
from os import path

fileMap = {}

def getFilesUtil(pathOfFiles):
	'''
	Function which recursively searchs the given directory for files and 
	updates their details in the map.
	'''
	l = os.listdir(pathOfFiles)
	dirList = []
	fileList = []	

	for ele in l:
		try:
			if path.isdir(pathOfFiles + "/" + ele):			# Recursive call if it is a directory
				getFilesUtil(pathOfFiles + "/" + ele)		
			else:
				fileList.append(ele)						# Add to the map if it is a file
				fileMap[pathOfFiles + "/" + ele] = os.path.getsize(pathOfFiles + "/" + ele) 	
		except Exception as e:
			continue;

def getFiles():
	'''
	Function which gets the list of files from the getFilesUtil method
	and picks the top 10 largest files from the map
	'''
	pathOfFiles = raw_input("Enter the path to search - ")
	getFilesUtil(pathOfFiles)

	# Sorting the map based on the value i.e. size of the files
	top10Files = sorted(fileMap.items(), key = operator.itemgetter(1))

	# Choosing the top 10 from the sorted list
	for file in top10Files[-10:]:
		print file
	
def organizeDirectory():
	'''
	Function that organizes the given directory by grouping files with 
	the same extension into folder with the same extension name.
	'''
	dirName = raw_input("Enter the path to organize - ")
	l = os.listdir(dirName)

	# Getting a list of all the types of files
	# i.e list of all extensions
	extList = []
	for file in l:
		extList.append(os.path.splitext(file)[-1])
	uniqList = list(set(extList))

	for file in os.listdir(dirName):
		if os.path.isdir(dirName + "/" + file) == False:		# Skipping the existing folders
			try:
				for ext in uniqList:
					if file.endswith(ext):
							if os.path.isdir(dirName + "/" + ext[1:]) == False:
									# Make a new folder for the extension and place the file in it.
					    			os.mkdir(dirName + "/" + ext[1:])
							    	shutil.move(dirName + "/" + file, dirName + "/" + ext[1:] + "/" + file)
							        print(os.path.join(dirName, file))
							else:
									# Folder Already created so just move the file into it.
							    	shutil.move(dirName + "/" + file, dirName + "/" + ext[1:] + "/" + file)
							    	print(os.path.join(dirName, file))
			except Exception as e:
				continue;

def sysExit():
	'''
	Exit from the program
	'''
	sys.exit()

if __name__ == "__main__":

	# Map for the functions that can be called
	choices = {
		1: getFiles,
		2: organizeDirectory,
		3: sysExit,
	}

	# Simulating a switch case
	while True:
		userChoice = raw_input("\nEnter your choice - \
							\n1. Search for top 10 largest files in a directory.\
							\n2. Unclutter a directory.\
							\n3. Exit\n\n")

		choices[int(userChoice)]()

	