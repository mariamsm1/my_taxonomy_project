#!/usr/bin/env python3
'''
Title: taxonomy database project #5

Date: 11.03.2020

Author: Mariam Miari

List of functions: open-import-print-exit / List of methods: strip-rstrip-append
-join-reversed().
'''

import sys
myDict = {} # this is the big dictionary that will contain the nested dictionaries.
mylist = []
tax = open(sys.argv[1], 'r')

input_taxid = input('Enter your taxid: ')

with open (sys.argv[1],"r") as tax:
	for line in tax:
		if line.startswith("ID"):
			taxId = line.split(":")[1].strip()#take the taxId number.
			myDict[taxId] = {}
		elif line.startswith("PARENT"):
			parent = line.split(":")[0].rstrip() #rstrip at the end because keys had a long trailing white space. so done after split.
			parentId = line.split(":")[1].strip()
			myDict[taxId][parent]= parentId #parent is nested key and parentId is the value
		elif line.startswith("SCIENTIFIC"):
			scient = line.split(":")[0].rstrip()
			scient_name = line.rstrip().split(":")[1]
			myDict[taxId][scient] = scient_name
		elif line.startswith("GENBANK"):
			genb = line.split(":")[0].rstrip()
			genb_name = line.rstrip().split(":")[1]
			myDict[taxId][genb] = genb_name
		elif line.startswith("COMMON"):
			com = line.split(":")[0].rstrip()
			com_name = line.rstrip().split(":")[1]
			myDict[taxId][com] = com_name
		elif line.startswith("RANK"):
			rank = line.split(":")[0].rstrip()
			rank_name = line.rstrip().split(":")[1]
			myDict[taxId][rank] = rank_name
		elif line.startswith("GC"):
			GC = line.split(":")[0].rstrip()
			GC_num = line.rstrip().split(":")[1]
			myDict[taxId][GC] = GC_num
		elif line.startswith("MGC"):
			MGC = line.split(":")[0].rstrip()
			MGC_num = line.rstrip().split(":")[1]
			myDict[taxId][MGC] = MGC_num

#rename input_taxid to another variable which will be used in the print statement. input_taxid will be overwritten before the print statement.
myTaxId = input_taxid
if input_taxid in myDict: #will be executed only if the user inputs a taxon ID which is present in the dictionary.
	if "GENBANK COMMON NAME" in myDict[input_taxid]:# to overcome the problem that some taxon IDs do not have common names or GC numbers of MGC numbers.
		Common_Name = myDict[input_taxid]["GENBANK COMMON NAME"]
	elif "COMMON NAME" in myDict[myTaxId]:
		Common_Name = myDict[input_taxid]["COMMON NAME"]
	else:
		Common_Name = "Not defined"
	if "GC ID" in myDict[input_taxid]:
		GC_number = myDict[input_taxid]["GC ID"]
	else:
		GC_number = "Not defined"
	if "MGC ID" in myDict[input_taxid]:
		MGC_number = myDict[input_taxid]["MGC ID"]
	else:
		MGC_number = "Not defined"
	RanK = myDict[input_taxid]["RANK"] #save the variable name (will be used for printing)
	ScientificName = myDict[input_taxid]["SCIENTIFIC NAME"] #used for printing because the next line will be overwritten each time the loop iterates the two lines below it.
	while input_taxid != "1": # the root ID is 1 and we do not want to include that.
		my_scientific_name_taxid = myDict[input_taxid]["SCIENTIFIC NAME"] #extracting scientific names for each taxid
		mylist.append(my_scientific_name_taxid)  # append the scientific name to the list.
		input_taxid=myDict[input_taxid]["PARENT ID"] #i overwrote the taxid of the input by the parent ID.
else:#Because the user may input a taxon ID that is not in the dictionary.
	print("input_taxid not found")
	sys.exit()
prelist = list(reversed(mylist))
prelineage= prelist[:-1] # delete last element from the list which is the scientific name because it is already reported in the output.
lineage = ";".join(prelineage)

print('"taxId"'+":"+myTaxId+"\n"+'"ScientificName"'+":"+ScientificName+"\n"+'"CommonName"'+":"+Common_Name+"\n"+'"rank"'+":"+RanK+"\n"+'"lineage"'+":"+lineage+"\n"+'"GeneticCode"'+":"+GC_number+"\n"+'"mitochondrialGeneticCode"'+":"+MGC_number)
