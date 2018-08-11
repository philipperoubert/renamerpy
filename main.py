############################################
################# Renamerpy ################
######### Made by Philippe Roubert #########
################ Version 1.0 ###############
############################################

import os, re

os.chdir("/Users/philippe/Desktop/renameTest")


def rename_string(item):
	L = ""
	for i in item:
		if (ord(i) == 776):
			i = 'e'
		elif(ord(i) == 32):
			i = ''
		elif(ord(i) == 35):
			i = ''
		elif(ord(i) == 223):
			i = 'ss'
		L += i
	return L

C = [0]

def recurseList(listOfItems):
	itemList = os.listdir()
	for i in itemList:
		C[0] += 1
		try:
			os.rename(i, rename_string(i))
			os.chdir(i)
			recurseList(os.listdir())
		except: 
			continue
	os.chdir("..")

recurseList(os.listdir())

print("Succesfully scanned and renamed " + str(C[0]) + " objects")
