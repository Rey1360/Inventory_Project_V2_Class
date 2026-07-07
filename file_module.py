"""
file module
read file
save file
"""
import csv
import os
from log_module import logger

def read_file(path):
    """
    reading csv files as dictionary
    input: file path
    output: file content as list
    """
    dir_path, file_name = os.path.split(path)
    dict_ = dict()
    
    if os.path.exists(dir_path):#check dir/folder exists
        if file_name in os.listdir(dir_path):#check file exists
            try: 
                with open(path, 'r') as f:
                    content = csv.DictReader(f, 
                                             delimiter=',',
                                             skipinitialspace=True,
                                             quotechar="'")
                    #content = list(content)
                    for dict_row in content:#returns dict of dict with key as name of item similar to inventory dictionary
                                            #benefit is able to search keys
                        dict_.update({list(dict_row.values())[0]:dict_row})
         
            except OSError as e:
                
                logger.critical(f'OSError {e}')
    
            return dict_ #content
        else:
            logger.warning('file does not exist in the directory')
            return dict_# it returns empty original dictionary, without it it returns none type
    else:
        logger.warning('Directory path does not exist')
        return dict_

def write_file(path, content):
    dir_path, file_name = os.path.split(path)
    fieldnames = ['ID', 'quantity', 'minimum']
    
    if os.path.exists(dir_path):#check dir/folder exists
        if file_name in os.listdir(dir_path):#check file exists
            try: 
                with open(path, 'w', newline='') as f:
                    dict_writer = csv.DictWriter(f,fieldnames=fieldnames);
                    dict_writer.writeheader()#fix header issue
                    dict_writer.writerows(content)
                    #logger.debug(f'file is updated: {file_name}')
                    
            except OSError:
                print('error!')
                logger.critical('OSError')
    
        else:
            logger.warning('file does not exist in the directory')
    else:
        logger.warning('Directory path does not exist')
            












