__author__ = 'rpdcorbion'
import sys, codecs, csv
sys.path.append("../lib")
from functions import csv_list_to_raw_str, findposition, distance_wgs84



def create_transfer(dossier, separateurcsv=','):
    dist_max=300
    vitesse=1.12
    wait_time=60
    nb_transfer=0
    nb_SA=0
    reports=''
    file = codecs.open(dossier+'stops.txt', 'r', 'utf-8')
    output = codecs.open(dossier+'transfers.txt', 'w', 'utf-8')
    reader = csv.reader(file, delimiter=separateurcsv, quoting=csv.QUOTE_MINIMAL)
    count=0
    SA_list=[]
    ### list of the SA not null
    for row in reader:
        if count==0:
            stop_id_pos=findposition('stop_id',row)
            name_pos=findposition('stop_name',row)
            location_type_pos=findposition('location_type',row)
            lat_pos=findposition('stop_lat',row)
            lon_pos=findposition('stop_lon',row)
        else:
            if len(row) > 1:
                if row[location_type_pos]=='0':
                    if row[lat_pos]:
                        lat1=float(row[lat_pos])
                        if row[lon_pos]:
                            lon1=float(row[lon_pos])
                            code=row[stop_id_pos]
                            name=row[name_pos]
                            SA_list.append((code,lat1,lon1,name))
        count+=1
    ### search for each stops, who is at xxx m (dist_max) arroud
    temp=csv_list_to_raw_str(['from_stop_id','to_stop_id','transfer_type','min_transfer_time'])
    output.write(temp)
    for Stop_area1 in SA_list:
        temp=csv_list_to_raw_str([Stop_area1[0],Stop_area1[0],'2',str(wait_time)])
        output.write(temp)
        reports+=report_log('transfer write from '+str(Stop_area1[3])+ 'to '+str(Stop_area1[3])+' ('+str(wait_time)+')')
        nb_SA+=1
        for Stop_area2 in SA_list:
            if Stop_area1!=Stop_area2:
                distance=distance_wgs84(Stop_area1[1], Stop_area1[2], Stop_area2[1], Stop_area2[2])
                if distance<dist_max:
                    nb_transfer+=1
                    time_transfer=int(1.4142*distance*vitesse)
                    temp=csv_list_to_raw_str([Stop_area1[0],Stop_area2[0],'2',str(time_transfer)])
                    output.write(temp)
                    reports+=report_log('transfer write from '+str(Stop_area1[3])+ 'to '+str(Stop_area2[3])+' ('+str(time_transfer)+')')
    reports+=report_log('transfer create : '+str(nb_transfer)+ '(+'+str(nb_SA)+')')
    return reports