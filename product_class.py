"""
Product class
intances are individual items
methods acts on individual items
"""
import file_module
from log_module import logger

class product_item:
    """
    Attributes:
        ID, quantity, minimum
        Methods: order, sold, check against min., update local, save item
    """
    def __init__(self, ID: str, quantity: int, minimum: int):
        self.ID = ID
        self.quantity = quantity
        self.minimum = minimum
        
    def item_order(self, order_quantity):
        """
        Get item order and check against min. threshold
        """
        self.order = order_quantity #order quantity of an item becomes attribute of the item
        if (
            (self.quantity - self.order < self.minimum)
            or (self.quantity < self.order)
            ): 

            logger.warning(f"warning!: {self.ID} in inventory will be low" 
                  "or quantity is lower than the number of order!")
        
        return self.order
    
    def item_sold(self, sold_quantity, inventory_dict):
        """
        Get number of sold items, check against min. threshold
        """
        self.sold = sold_quantity
        self.quantity = self.quantity - self.sold
        if self.quantity > self.minimum: 
            #print(f'{self.ID} in inventory is OK')
            logger.debug(f'{self.ID} in inventory is OK')
        else:
            print('warning!, item in inventory if less than minimum allowed!')
            logger.warning('warning!, item in inventory if less than minimum allowed!')
        self.update_item(inventory_dict) #caling update method
        
        return self.sold, self.quantity
    
    def check_item(self):
        """
        Check item number against min. threshold
        Deddicated method
        """
        if self.quantity > self.minimum: 
            logger.debug(f'{self.ID} in inventory is OK')
        else:
            raise Exception(f'{self.ID} in inventory is less than allowed minimum')
            logger.critical(f'{self.ID} in inventory is less than allowed minimum')
        
    def update_item(self, inventory_dict): #update local inventory in variable  
        inventory_dict[self.ID]=self.__dict__.copy()
        logger.debug('Item is updated locally')
        
    def save_item(self, path, item):
        """
        Open inventory file, update it locally, save it back
        item is a class object, item.__dict__ -> keys/values
        """
        content = file_module.read_file(path)#dict of dict with key as name of item
        print(content)
        if item.__dict__['ID'] in content.keys():
            content[item.__dict__['ID']] = item.__dict__.copy()#uodating item that exists in both local and file inventory
            logger.debug(f'Item ({item.__dict__['ID']}) was update in inventory file')
        else:
            content.update({item.__dict__['ID']:item.__dict__})#adding item that exists in local inventory dict but not in inventory file
            logger.debug(f'Item ({item.__dict__['ID']}) was added to inventory file')

        file_module.write_file(path, list(content.values()))
        
        return content   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        