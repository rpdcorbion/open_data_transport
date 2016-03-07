__author__ = 'rpdcorbion'
import zipfile
import urllib.request
import json
import os
import shutil
import ftplib as ftp
import math
import codecs
import csv


def isinlist(value, list):
    for item in list:
        if item==value:
            return True
    return False

def charge_json(api, auth=''):
    req = urllib.request.Request(api)
    if auth:
        req.add_header('Authorization', auth)
    try:
        data=urllib.request.urlopen(req)
        data=str(data.read(), encoding='utf-8')
        data = json.loads(data)
    except Exception as e:
        print('ACCESS ERROR ON '+api)
        data=''
    return data

def cellneedprotection(cell, separateurcsv):
    rep=False
    list_of_protection=[separateurcsv,"'"]
    cell=str(cell)
    for letter in cell:
        for value in list_of_protection:
            if letter == value:
                rep=True
    return rep

def csv_list_to_raw_str(list, separateurcsv=','):
    result = ""
    lb_first = True
    for cell in list :
        if cell:
            cell=cell.replace('"','""')
        if not lb_first:
            result += separateurcsv
        lb_first = False
        if cellneedprotection(cell, separateurcsv):
            result += '"'+str(cell)+'"'
        else:
            result += str(cell)
    return result + "\n"

def findposition(chain, list):
    count=0
    rep=999
    for valeur in list:
        valeur_bom=valeur.replace('"','')
        valeur_bom=valeur_bom[1:]
        if valeur == chain or valeur_bom == chain:
            rep=count
        count+=1
    return rep

def unzip(archive, destination):
    zfile = zipfile.ZipFile(archive,'r')
    for filename in zfile.namelist():
        end_filename=filename.split('/')[-1]
        #print(filename)
        write_file=0
        data = zfile.read(filename)
        try:
            file = open(destination+end_filename, 'w+b')
            write_file=1
        except Exception as e:
            print('error when unzip '+filename)
        if write_file:
            file.write(data)
            file.close()

def zip(archive, dossier):
    file_list=[f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f))]
    zip_file=os.path.realpath(archive)
    zip=zipfile.ZipFile(zip_file, "w", compression=zipfile.ZIP_DEFLATED, allowZip64=True)
    for filename in file_list:
        f=os.path.join(dossier,filename)
        zip.write(os.path.realpath(f), os.path.basename(f))

def download_file(url, destination):
    print("Start Download : "+ url)
    urllib.request.urlretrieve(url, os.path.realpath(destination))
    print("End Download")

def delete_folder(folder):
    try:
        if(os.path.isdir(folder)):
            shutil.rmtree(folder)
    except (KeyError, TypeError, ValueError):
        print('ERROR ON DELETTE FOLDER '+folder)
    print('DELETTE FOLDER OK '+folder)

def send_ftp(host,user,password, fichier,repository):
    print('connexion to '+host)
    print(fichier)
    print(repository)
    connect = ftp.FTP(host,user,password) # on se connecte
    file = open(fichier, 'rb')
    connect.sendcmd('CWD '+repository)
    connect.storbinary('STOR '+os.path.basename(fichier), file)
    file.close()
    etat = connect.getwelcome()
    print("Status : ", etat)
    connect.quit()

def distance_wgs84(lat1, lon1, lat2, lon2):
    R=6371
    if lat1==lat2 and lon1==lon2:
        dist1=0
    else:
        dist1=R*math.acos(math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.cos(math.radians(lon2)-math.radians(lon1))+math.sin(math.radians(lat1))*math.sin(math.radians(lat2)))
    return (dist1*1000)

def delete_duplicate_stops(stops_file, separateurcsv=','):
    file = codecs.open(stops_file, 'r', 'utf-8')
    reader = csv.reader(file, delimiter=separateurcsv, quoting=csv.QUOTE_MINIMAL)
    output = codecs.open(stops_file+'_temp.txt', 'w', 'utf-8')
    count=0
    list_of_stops_write=[]
    ignore_stops=0
    for row in reader:
        if count==0:
            stop_id_pos=findposition('stop_id',row)
            ##coverage_pos=findposition('coverage',row)
            temp=csv_list_to_raw_str(row)
            output.write(temp)
        else:
            if not isinlist(row[stop_id_pos], list_of_stops_write):
                list_of_stops_write.append(row[stop_id_pos])
                temp=csv_list_to_raw_str(row)
                output.write(temp)
            else:
                ignore_stops+=1
        count+=1
    print('ignore_stops : '+str(ignore_stops))
    return stops_file+'_temp.txt'