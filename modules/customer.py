import csv
import os

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/customers.csv")

class Customers():

	def __init__(self, id, first_name, last_name, current_video_rentals):
		self.id = id
		self.first_name = first_name
		self.last_name = last_name
		self.current_video_rentals = current_video_rentals
    
	@classmethod
	def get_customers(cls):
		with open(path, 'r') as customer_file:
			customers = csv.DictReader(customer_file)
			customers_list = []
			for customer in customers:
				new_customer = Customers(customer['id'], customer['first_name'], customer['last_name'], customer['current_video_rentals'])
				customers_list.append(new_customer)
			
			return customers_list