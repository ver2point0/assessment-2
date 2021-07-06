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
		pass


	# rent a video
	def rent_a_video(self):
		pass

	# return a video
	def return_a_video(self):
		pass


	# add a new customer
	def add_a_new_customer(self, customer_id):
		pass


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