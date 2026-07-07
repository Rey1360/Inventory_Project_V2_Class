"""
sample code by Gemini
"""
import os
import logging

# Configure local logging format
logging.basicConfig(
    filename='inventory_system.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class Product:
    """Class blueprint representing an individual stock item."""
    def __init__(self, product_id, name, quantity, threshold):
        self.product_id = product_id
        self.name = name
        self.quantity = int(quantity)
        self.threshold = int(threshold)

    def restock(self, amount):
        """Increments item quantity."""
        if amount > 0:
            self.quantity += amount
            logging.info(f"Product '{self.name}' (ID: {self.product_id}) restocked by {amount}. New total: {self.quantity}")
        else:
            raise ValueError("Restock quantities must be positive integers.")

    def use_stock(self, amount):
        """Decrements item quantity and returns True if low stock alert fires."""
        if amount <= self.quantity:
            self.quantity -= amount
            logging.info(f"Deducted {amount} units from product '{self.name}'. Remaining: {self.quantity}")
            return self.is_low_stock()
        else:
            logging.error(f"Failed transaction: Insufficient stock for item '{self.name}'. Request: {amount}, Available: {self.quantity}")
            raise ValueError(f"Insufficient stock balance available for {self.name}.")

    def is_low_stock(self):
        """Checks if current units drop beneath target safe threshold."""
        return self.quantity <= self.threshold


class InventoryManager:
    """Class responsible for handling File I/O operations and collection tracking."""
    def __init__(self, data_file_path):
        self.data_file = data_file_path
        self.products = {} # Dictionary storage: {product_id: Product Object}

    def load_inventory(self):
        """File I/O: Reads inventory data from a comma-separated database file."""
        if not os.path.exists(self.data_file):
            logging.warning(f"Database path '{self.data_file}' not found. Initializing empty tracker record.")
            return

        try:
            with open(self.data_file, 'r') as file:
                for line_num, line in enumerate(file, 1):
                    # Clean whitespaces and strip newline values
                    line = line.strip()
                    if not line or line.startswith("#"): # Skip blank lines/comments
                        continue
                        
                    # Error Handling during row parsing
                    try:
                        p_id, name, qty, thresh = line.split(',')
                        # Instantiate object and store in dictionary collection
                        self.products[p_id] = Product(p_id, name, qty, thresh)
                    except ValueError:
                        logging.error(f"Skipping corrupted entry line #{line_num} inside file: '{line}'")
                        
            logging.info(f"Successfully tracked {len(self.products)} products from flat database.")
        except IOError as e:
            logging.critical(f"System failed reading inventory source database file. Raw exception: {e}")

    def save_inventory(self):
        """File I/O: Persists runtime state configurations back to disk database."""
        try:
            with open(self.data_file, 'w') as file:
                for prod in self.products.values():
                    file.write(f"{prod.product_id},{prod.name},{prod.quantity},{prod.threshold}\n")
            logging.info("Inventory transaction state safely saved to database file.")
        except IOError as e:
            logging.error(f"Could not persist active state modifications back to file system data. Exception: {e}")

    def check_alerts(self):
        """Loops through tracking dictionaries to check for critical thresholds."""
        alerts_triggered = 0
        print("\n--- SYSTEM STOCK STATUS SCREEN ---")
        for prod in self.products.values():
            if prod.is_low_stock():
                print(f"[ALERT] Item '{prod.name}' (ID: {prod.product_id}) is running low! Status: {prod.quantity}/{prod.threshold}")
                logging.warning(f"Low Stock Trigger Alert fired for '{prod.name}' (ID: {prod.product_id}). Balance: {prod.quantity}")
                alerts_triggered += 1
            else:
                print(f"[OK] {prod.name}: {prod.quantity} available.")
        return alerts_triggered


# Local Testing Execution 
if __name__ == "__main__":
    db_path = "mock_inventory.txt"
    
    # Setup test file database
    with open(db_path, "w") as f:
        f.write("101,Laptop,15,5\n")
        f.write("102,WirelessMouse,3,8\n") # This starts in a triggered low state
        f.write("103,HDMI_Cable,25,10\n")

    # Instantiate manager system controller object
    manager = InventoryManager(db_path)
    manager.load_inventory()
    
    # Process and execute operations
    manager.check_alerts()
    
    print("\nSimulating stock transaction updates...")
    try:
        # Pull item from dictionary and execute class methods
        laptop_item = manager.products.get("101")
        if laptop_item:
            # Use 12 items, dropping level from 15 to 3 (threshold is 5)
            laptop_item.use_stock(12) 
    except ValueError as err:
        print(f"Transaction aborted: {err}")

    # Check alert statuses after updates and rewrite back to storage database
    manager.check_alerts()
    manager.save_inventory()
