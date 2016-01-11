__author__ = 'rpdcorbion'
import zipfile

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