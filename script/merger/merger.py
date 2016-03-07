__author__ = 'rpdcorbion'

import codecs, csv, os
import sys
maxInt = sys.maxsize
decrement = True
while decrement:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.
    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True


sys.path.append("../lib")
from functions import csv_list_to_raw_str, findposition, unzip

def merger(files,env_to_merge, dossier_work, separateurcsv=','):
    ### create dir new
    if not os.path.exists(dossier_work+'new/'): os.makedirs(dossier_work+'new/')
    ### create dir env
    ### unzip all env in dir
    for environement in env_to_merge:
        if not os.path.exists(dossier_work+environement+'/'): os.makedirs(dossier_work+environement+'/')
        unzip(dossier_work+environement+'.zip', dossier_work+environement+'/')
        ## delete dl zip
        os.remove(dossier_work+environement+'.zip')
    for fichier in files:
        print(environement+ '--' +fichier[0])
        output = codecs.open(dossier_work+'new/'+fichier[0]+'.txt', 'w', 'utf-8')
        header=[]
        for champs in fichier[1]:  # Write header
            header.append(champs[0])
        temp=csv_list_to_raw_str(header)
        output.write(temp)
        for environement in env_to_merge:
            if os.path.isfile(dossier_work+environement+'/'+fichier[0]+'.txt'):
                marker=environement.replace('-','_')+':'
                file = codecs.open(dossier_work+environement+'/'+fichier[0]+'.txt', 'r', 'utf-8')
                reader = csv.reader(file, delimiter=separateurcsv, quoting=csv.QUOTE_MINIMAL)
                count=0
                positions=[]
                for row in reader:
                    if count==0:
                        for champs in fichier[1]:
                             positions.append(findposition(champs[0],row)) #Find position of every fields
                    else:
                        row_to_write=[]
                        i=0
                        for champs in fichier[1]:
                            if positions[i]!=999:
                                value=row[positions[i]]
                                if champs[1]==1:
                                    value=marker+value
                            else:
                                value=''
                            row_to_write.append(value)
                            i+=1
                        temp=csv_list_to_raw_str(row_to_write)
                        output.write(temp)
                    count+=1
            else:
                print("FILE "+environement+" - "+fichier[0]+" NOT EXIST")

