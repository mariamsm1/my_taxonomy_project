# my_taxonomy_project

taxonomy_proj.py is a python script to retrieve information regarding common name, scientific name, rank, genetic code, mitochondrial genetic code, and lineage for a particular input taxon ID.

**Dependecies:** 

python 3.7.4

**Description:** 

The program is run like: ./taxonomy_proj.py input database
#The code is user interactive in which the user has to input the desired taxon ID.

**Example on running the code:**

Get the data for this: wget ftp://ftp.ebi.ac.uk/pub/databases/taxonomy/taxonomy.dat 

./taxonomy.py taxonomy.dat 
--> RUN
--> INPUT DESIRED TAXON ID (e.g. 9606) 

**PROCEDURE:** 

First, the taxonomy database is parsed inorder to save all the needed
data in a dictionary. A big dictionary is created that will have the taxon IDs as keys
and nested dictionaries as values whereby each nested dictionary contains all the
information associated with that particular taxon ID as keys and values (e.g.
PARENT ID: 24352, Scientific name: Bacteria..etc). For lineage, if the taxon ID
was different from 1 (which is the root, which we don't want), the scientific
name of the taxon ID is saved and appended to a list, then the taxon ID will be over-
written and will evaluate to the value of PARENT ID in the nested dictionary. This
way, the program is managing to find the parent ID of each previous ID in order
to get the full lineage of the species. Common name, GC ID, MGC ID were extracted
easily for each taxon ID by using the nested dictionary syntax:
"variable = myDict[key][innerkey]"

**Example of output:**

"taxId":9606

"ScientificName": Homo sapiens

"CommonName": human

"rank": species

"lineage": cellular organisms; Eukaryota; Opisthokonta; Metazoa; Eumetazoa; Bilateria; Deuterostomia; Chordata; Craniata; Vertebrata; Gnathostomata; Teleostomi; Euteleostomi; Sarcopterygii; Dipnotetrapodomorpha; Tetrapoda; Amniota; Mammalia; Theria; Eutheria; Boreoeutheria; Euarchontoglires; Primates; Haplorrhini; Simiiformes; Catarrhini; Hominoidea; Hominidae; Homininae; Homo

"GeneticCode": 1

"mitochondrialGeneticCode": 2

The script outputs to the terminal so if you want to create an output file for each run, add to the script "open("my_output", "w") as out" and in the print statement add "file = out" . Run the program like ./taxonomy.py taxonomy.dat my_output
