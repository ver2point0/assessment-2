import csv
import os
from modules.videos import Video
from modules.customer import Customer

class Inventory():

	# view the video inventory
	def view_video_inventory(self):
		for v in self.videos:
			print(v)


	# view a customer's rented videos
	def view_customers_videos(self):
		c_id = input(f"\nEnter the customer id:\t")
		for c in self.customers:
			if c['id'] == c_id and c['current_video_rentals'] != '':
				return(print(f"\n{c['first_name']} {c['last_name']} is currently renting: {c['current_video_rentals']}\n"))
			elif c['id'] == c_id and c['current_video_rentals'] == '':
				return(print(f"\n{c['first_name']} {c['last_name']} is not currently renting a movie.\n"))
		print(f"\nCustomer ID is not found.")


	# rent a video
	def rent_a_video(self):
		pass

	# return a video
	def return_a_video(self):
		pass


	# add a new customer
	def add_a_new_customer(self, customer_id):
		first_name = input(f"\nEnter a first name: ")
		last_name = input(f"Enter a last name: ")
		self.customers.append({'id': customer_id + 1, 'first_name': first_name, 'last_name:': last_name, 'current_video_rentals': ''})
		Inventory.save_data('customers', ['id', 'first_name', 'last_name', 'current_video_rentals'], self.customers)

	# read a csv
	@classmethod
	def objects(cls, file_name):
		data = []
		my_path = os.path.abspath(os.path.dirname(__file__))
		path = os.path.join(my_path, f"../data/{file_name}.csv")
		with open(path) as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				data.append(row)
		return data, int(row['id'])

	# write to csv
	@classmethod
	def save_data(cls, file_name, header_row, data):
		my_path = os.path.abspath(os.path.dirname(__file__))
		path = os.path.join(my_path, f"../data/{file_name}.csv")
		n_list = []
		for i in data:
			n_list.append(list(i.values()))
		with open(path, 'w') as csvfile:
			csv_data = csv.writer(csvfile, delimiter=',')
			csv_data.writerow(header_row)
			csv_data.writerows(n_list)