__author__ = 'rpdcorbion'
import sys, os
sys.path.append("../lib")
from functions import charge_json, download_file, zip, delete_folder, send_ftp, delete_duplicate_stops
sys.path.append("../..")
import __root__
import merger
import shutil
sys.path.append("../../private_config")
from ftp import *



def charge_from_ODS(workspace,coverage,base_format='GTFS'):
    # we have to find the data
    ODS_platform='https://navitia.opendatasoft.com'
    data=charge_json(ODS_platform+'/api/v2/catalog/datasets/'+coverage+'/records?q='+coverage+'-'+base_format)
    print(data)
    id_to_download=data['records'][0]['record']['fields']['download']['id']
    print (id_to_download)
    # now we download the data
    url=ODS_platform+'/explore/dataset/'+coverage+'/files/'+id_to_download+'/download/'
    download_file(url,workspace+coverage+'.zip')



if __name__ == "__main__":
    move_to_ftp=1
    list_coverage=sys.argv[1].split(',')
    print(list_coverage)
    outname=sys.argv[2]
    if len(sys.argv) > 3:
        base_format=sys.argv[3]
    else:
        base_format='GTFS'
    workspace=__root__.real_path() +'data/'
    for coverage in list_coverage:
        charge_from_ODS(workspace,coverage,base_format)
    if base_format=='GTFS':
        from GTFS_merger import *
    elif base_format=='NTFS':
        from NTFS_merger import *
    else:
        print('ERROR TO DETERMINE FORMAT')

    merger(files,list_coverage, workspace)
    new_stop_file=delete_duplicate_stops(workspace+'new/stops.txt')
    shutil.move(new_stop_file,workspace+'new/stops.txt')
    try:
        zip(workspace+outname+'.zip',workspace+'new/')
    except Exception as e:
        print('ERREUR LORS DU ZIPPAGE DE '+workspace+outname+'.zip')
    for coverage in list_coverage:
        delete_folder(workspace+coverage+'/')
    delete_folder(workspace+'new/')
    if move_to_ftp:
        ## import private configuration for FTP (host,login,password, repository)
        send_ftp(host,login,password, workspace+outname+'.zip', ODS_repository)
        os.remove(workspace+outname+'.zip')

