"""
Inventory manager class (All items)
check inventory 
update inventory: save file from local variables
"""
import file_module
from log_module import logger

class inventory_manager:
    def __init__(self, attr):
        self.attr = attr #dummy
        
    def check_inventory(self, path):
        c = 0
        content = file_module.read_file(path)
        for key_ in content:#content is dict of dict with keys as name of items 'item_1':{'ID':'item_1','quantity':1,'minimum':1}
            if content[key_]['quantity'] < content[key_]['minimum']:
                logger.warning(f'item {key_} in inventory is less than minimum threshold')
                c = c + 1
            if c == 0:#one log only for all items OK
                logger.debug('All items are in good quantity')
    
    def update_inventory(self, path, inventory_dict):
        """
        Read inventory, compare to local inventory variable
        add/update items from local, keep items exclusive to inventory
        log difference, save back to inventory file
        """
        content = file_module.read_file(path)#dict of dict with key=item name, similar to local inventory var
        
        for key_ in inventory_dict.keys():#if item exists in both update the item dictionary, if not add it to content
            if key_ in content.keys():
                content[key_] = inventory_dict[key_].copy()#uodating item that exists in both local and file inventory
                logger.debug(f'Item ({key_}) was update in inventory file')
            else:
                content.update({key_:inventory_dict[key_]})#adding item that exists in local inventory dict but not in inventory file
                logger.debug(f'Item ({key_}) was added to inventory file')
                
        file_module.write_file(path, list(content.values()))#list(content.values()) has original form for inventory file dictionary with field names
        
        
        
        

        
        
        