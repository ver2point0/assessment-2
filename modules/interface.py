from modules.inventory import Inventory

class Interface():
	def __init__(self):
		self.videos, self.video_id = Inventory.objects('inventory')
		self.customers, self.customer_id = Inventory.objects('customers')

	def run(self):
		while True:
			user_input = input(
				"""
				Welcome to the video store!

				What would you like to do?
				Options:
				1. View the video inventory
				2. View a customer's rented videos
				3. Rent a video
				4. Return a video
				5. Add a new customer
				6. Exit
				"""
			)

			if user_input == '1':
				Inventory.view_video_inventory(self)
			elif user_input == '2':
				Inventory.view_customers_videos(self)
			elif user_input == '3':
				Inventory.rent_a_video(self)
			elif user_input == '4':
				Inventory.return_a_video(self)
			elif user_input == '5':
				Inventory.add_a_new_customer(self, self.customer_id)
			elif user_input == '6':
				break
			else:
				print("You have entered an invalid option.")