import csv
import os

from modules.inventory import Inventory
from modules.customer import Customers

class Videos(Inventory):
    def __init__(self, id, title, rating, copies_available):
        super().__init__(id, title, rating, copies_available)
        self.checked_out = 'y'

    def __str__(self):
        return f"""
        Video ID: {self.id}
        Title:  {self.title}
        Rating: {self.rating}
        Copies Avaliable: {self.copies_available}
        Checked out: {self.checked_out}
        """