############################################
################# Renamerpy ################
######### Made by Philippe Roubert #########
################ Version 1.1 ###############
############################################

import os, re

os.chdir("C:/Users/GastGast/Desktop/testFolder")


def rename_string(item):
	L = ""
	for i in item:
		if (ord(i) == 776): # Umlaut => e
			i = 'e'
		elif(ord(i) == 32): # ' ' => ''
			i = ''
		elif(ord(i) == 35): # # => ''
			i = ''
		elif(ord(i) == 223): # ß => ss
			i = 'ss'
		elif(ord(i) == 246): # ö => oe
			i = 'oe'
		elif(ord(i) == 228): # ä => ae
			i = 'ae'
		elif(ord(i) == 252): # ü => ue
			i = 'ue'
		elif(ord(i) == 214): # Ö => OE
			i = 'OE'
		elif(ord(i) == 196): # Ä => AE
			i = 'AE'
		elif(ord(i) == 220): # Ü => UE
			i = 'UE'
		L += i
	return L

C = [0]

def recurseList(listOfItems):
	itemList = os.listdir()
	for i in itemList:
		try:
			new_i = rename_string(i)
			if (i != new_i):
				print(i, " => ", new_i)
				os.rename(i, new_i)
				C[0] += 1
			os.chdir(new_i)
			recurseList(os.listdir())
		except:
			continue
	os.chdir("..")

recurseList(os.listdir())

print("Succesfully renamed " + str(C[0]) + " objects")
