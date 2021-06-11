import csv
import os


from modules.inventory import Inventory
from modules.customer import Customers

my_path = os.path.abspath(os.path.dirname(__file__))
customer_path = os.path.join(my_path, "../data/customers.csv")


class Interface():

	def __init__(self):
		self.Inventory = Inventory.get_inventory()
		self.customers = Customers.get_customers()
		self.checkin_customer()


	def checkin_customer(self):
		while True:
			user_input = int(input(f"""
			Please checkin to the customer portal
			1. New customer
			2. Existing customer
			3. Exit
			"""))
			print(user_input)
			if user_input == 1:
				print("Welcome!")
				self.add_customer()
			elif user_input == 2:
				self.login()
			elif user_input == 3:
				break

	def main_menu(self):
		while True:
			user_input = int(input(f"""
			Welcome to Code Platoon Video!
			1. View video inventory
			2. View customer's rented videos
			3. Rent video
			4. Return video
			5. Exit
			"""))


			if user_input == 1:
				self.view_inventory()
			elif user_input == 2:
				self.view_rentals()
			elif user_input == 3:
				self.rent_video()
			elif user_input == 4:
				self.return_video()
			elif user_input == 5:
				self.logged_in_user = None
				self.logged_in = False
				break

	def add_customer(self):
		customer_details = {'first_name': 'customer'}
		customer_details['id'] = input("Enter an ID number: ")
		customer_details['first_name'] = input("Enter your first name: ")
		customer_details['last_name'] = input("Enter your last name: ")
		customer_details['current_video_rentals'] = ''

		customers = Customers.get_customers()

		for customer in customers:
			if str(customer.id) == str(customer_details['id']):
				print("This ID already exists. Enter a new one.")
				return self.add_customer()
		customers.append(Customers(**dict(customer_details)))
		self.save_customers(customers)


	def save_customers(self, customers):
		for customer in customers:
			print(customer)
		with open(customer_path, 'w') as c_file:
			c_csv = csv.writer(c_file, delimiter=',')
			c_csv.writerow(['id', "first_name", "last_name", "current_video_rentals"])

			for customer in customers:
				print(customer)
				c_csv.writerow([customer.id, customer.first_name, customer.last_name, customer.current_video_rentals])
		
		print(f"Welcome {customer.first_name}!")
		return self.main_menu()


	def login(self):
		c_id = input("Enter customer ID number: ")
		for c in Customers.get_customers():
			if c.id == c_id:
				self.current_customer = c
				self.all_inventory = Inventory.get_inventory()
				print(f"Welcome {c.first_name}")
			return self.main_menu()

	
	def view_inventory(self):
		inventory = Inventory.get_inventory()
		print("Current inventory:")
		for i in inventory:
			print(F"{i.copies_available} copies of {i.title}")

	
	def view_rentals(self):
		Customers.get_customers()
		print(f"""
		Customer ID: {self.current_customer.id}
		Customer Name: {self.current_customer.first_name} {self.current_customer.last_name}
		Current Movies: {self.current_customer.current_video_rentals}
		""")


	def rent_video(self):
		pass


	def return_video(self):
		pass

			