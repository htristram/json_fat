import wget
import csv
import json
import os.path
import sys
from zipfile import ZipFile
from time import perf_counter

# Changer ces 2 lignes pour varier le test.
nombre_lignes = 500000 # nombre d'enregistrements à transformer 
reduice = True    # Si true, drop les valeurs vides

def convert_bytes(size):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0

if not os.path.isfile("sirene.zip"):
    wget.download("https://files.data.gouv.fr/insee-sirene/StockEtablissement_utf8.zip", out="sirene.zip")

with ZipFile("sirene.zip", 'r') as zip:
    dst = zip.namelist()
    if not os.path.isfile(dst[0]):
        print("\nDécompression en cours du fichier ", dst[0] )
        zip.extract(dst[0], ".")
    
t_start_global = perf_counter()
i=0
data={}
print("Lecture du csv. ",nombre_lignes," enregistrements")
with open(dst[0], encoding = 'utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for rows in csv_reader:
        if reduice:
            for c in csv_reader.fieldnames:
                if rows[c]=='':
                    del rows[c]

        data[rows["siret"]]=rows
        if i>=nombre_lignes:
            break
        i+=1 
csv_file.close()

t_finish_read = perf_counter()
print("durée de la lecture du csv (réduction=",reduice,") : ",round(t_finish_read- t_start_global,2) )

t_start_export = perf_counter()
with open("resultat.json", 'w', encoding = 'utf-8') as json_file:
    print("Création du json")
    json_file.write(json.dumps(data, indent = 4))
t_finish_export = perf_counter()
print("durée de l'export = ",round(t_finish_export- t_start_export,2))

t_finish_global = perf_counter()
print("Temps nécessaire à la lecture du CSV et à l'écriture du Json = ", round(t_finish_global - t_start_global,2))

print("Taille du fichier produit : ",convert_bytes(os.path.getsize("resultat.json")))