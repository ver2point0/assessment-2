import csv
import os

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/inventory.csv")

class Inventory():

	def __init__(self, id, title, rating, copies_available):
		self.id = id
		self.title = title
		self.rating = rating
		self.copies_available = copies_available

	@classmethod
	def get_inventory(cls):
		with open(path, 'r') as inventory_file:
			inventory = csv.DictReader(inventory_file)
			inventory_list = []
			for video in inventory:
				new_video = Inventory(video['id'], video['title'], video['rating'], video['copies_available'])
				inventory_list.append(new_video)
			
			return inventory_list