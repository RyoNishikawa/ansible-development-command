from adc.models.inventory import InventoryFile
from adc.services.management.abstracts import List


class Inventory(List):

    global_inventory: InventoryFile
    project_inventory: InventoryFile

    def __init__(self):
        pj_inventory = InventoryFile()
        pj_inventory.read_hosts()
        self.project_inventory = pj_inventory
        pass

    def __str__(self):
        return self.project_inventory
