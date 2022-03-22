# -*- coding: utf-8 -*-

#%% Import libreries
import pandas as pd
import datetime

#%% Open config.txt
try:
    with open("config.txt") as file:
        lines = file.readlines()
        for line in lines:
            if "secuency_1" in line:
                name_archive_1 = line.split("=")[1].strip()
            if "secuency_2" in line:
                name_archive_2 = line.split("=")[1].strip()
            if "index_file" in line:
                name_archive_index = line.split("=")[1].strip()
            else:
                continue
    
    print("config.txt was readed successfully")

except Exception as e:
    print(f"An error occurred while try to open config.txt file: {e}")
    
#%% Read both secuencies FASTA files (.fas)
def read_genome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

try:
    sec_1 = read_genome(name_archive_1)
    sec_2 = read_genome(name_archive_2)
    
    print("FASTA secuencies files were readed successfully")
    
except Exception as e: 
    print(f"An error occurred while try to open FASTA secuencies files: {e}")

#%% Open index.xlsx
try:
    archivo_index = pd.read_excel(name_archive_index, header=None)
    archivo_index.columns = ["type", "name", "start", "end"]
    archivo_index = archivo_index[archivo_index.type == "DNA"]
    
    print("Index file was readed successfully")
    
except Exception as e: 
    print(f"An error occurred while try to open index file: {e}")

#%% Compare secuencies and set values to results files
archivo_index["na"] = 0
archivo_index["indel"] = 0
archivo_index["id"] = 0
archivo_index["snp"] = 0

# Set differents counters
na = 0
indel = 0
id = 0
snp = 0

for line_idx in archivo_index.index:
    start = archivo_index.loc[line_idx, "start"]
    end = archivo_index.loc[line_idx, "end"]
    
    sec_1_gen = sec_1[start-1: end-1]
    sec_2_gen = sec_2[start-1: end-1]

    for idx, nucleotid_sec_1 in enumerate(sec_1_gen):
        
        nucleotid_sec_2 = sec_2_gen[idx]
    
        if nucleotid_sec_1 == "-" or nucleotid_sec_2 == "-":
            if nucleotid_sec_1 == "-" and nucleotid_sec_2 == "-":
                na += 1
            else:
                indel += 1
        else:
            if nucleotid_sec_1 == nucleotid_sec_2:
                id += 1
            
            else:
                snp += 1
    
    try:
        archivo_index.loc[line_idx, "na"] = na
        archivo_index.loc[line_idx, "indel"] = indel
        archivo_index.loc[line_idx, "id"] = id
        archivo_index.loc[line_idx, "snp"] = snp
        
    except Exception as e:
        print(e)
                
#%% Set results file name with date and time
date_today = datetime.datetime.today().strftime("%d-%m-%Y_%Hh_%Mm_%Ssec")
name_archive_results = f"results_{date_today}.xlsx"
archivo_index.to_excel(name_archive_results)
print("- - - - - - - - - - - - - - - - - - - -")
print(f"Count:\nna = {na}, indel = {indel}, id = {id}, snp = {snp}")
print("- - - - - - - - - - - - - - - - - - - -")
print(f"{name_archive_results} was generated successfully")
