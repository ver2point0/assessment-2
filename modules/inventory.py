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
		c_id = input(f'\n Enter customer id: ')
		v_title = input(f'Enter video title: ')
		cust_id = False
		available_id = False

		# are copies available
		for v in self.videos:
			if v['title'] == v_title and int(v['copies_available']) > 0:
				available_id = True
				break
			elif v['title'] == v_title and int(v['copies_available']) < 0:
				print(f"\n There are no copies of {v['title']}.\n")
				return

		# is the move title in the inventory
		if available_id == False:
			print(f"\n{v_title} is not in the inventory.\n")

		# rental limit
		for c in self.customers:
			if c['id'] == c_id and len(c['current_video_rentals'].split('/')) < 3:
				cust_id = True
				break
			elif c['id'] == c_id and len(c['current_video_rentals'].split('/')) == 3:
				print(f'\n{c["first_name"]} {c["last_name"]} is currently renting three movies, return a movie to borrow another one.')
				return

		if cust_id == False:
			print(f'\nThe customer ID is not found.\n')
			return

		if c['current_video_rentals'] == '':
			c['current_video_rentals'] = v['title']
		else:
			c['current_video_rentals'] += f"/{v['title']}"
			v['copies_available'] = str(int(v['copies_available']) - 1)
			Inventory.save_data('inventory', ['id', 'title', 'rating', 'copies_available'], self.videos)
			Inventory.save_data('customers', ['id', 'first_name', 'last_name', 'current_video_rentals'], self.customers)

	# return a video
	def return_a_video(self):
		pass


	# add a new customer
	def add_a_new_customer(self, customer_id):
		f_name = input(f"\nEnter a first name: ")
		l_name = input(f"Enter a last name: ")
		self.customers.append({'id': customer_id + 1, 'first_name': f_name, 'last_name:': l_name, 'current_video_rentals': ''})
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