from product_class import product_item
from inventory_manager_class import inventory_manager
import os
import file_module

path_inventory = r'D:/Programming/Python Codes/Codes/Project_2_Inventory/V2_class\inventory.txt'
path_logfile =   r'D:/Programming/Python Codes/Codes/Project_2_Inventory/V2_class\logfile.log'
inventory_dict = dict()

item_1 = product_item('item_1', quantity=300, minimum=300)
# item_1.update_item(inventory_dict)
item_1.quantity = 200
# item_1.check_item()

item_4 = product_item('item_4', 0, 0)
# item_4.update_item(inventory_dict)
# item_4.quantity = 200

content = item_4.save_item(path_inventory, item_4)

os.startfile(path_inventory)
os.startfile(path_logfile)
# manager = inventory_manager('attr')#dummy
# manager.check_inventory(path_inventory)

# print(item_1.__dict__)


