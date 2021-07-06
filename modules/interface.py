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
				print("View inventory")
				Inventory.view_video_inventory()
			elif user_input == '2':
				print("View a customer's rented videos")
				Inventory.view_customers_videos()
			elif user_input == '3':
				print("Rent a video")
				Inventory.rent_a_video()
			elif user_input == '4':
				print("Return a video")
				Inventory.return_a_video()
			elif user_input == '5':
				print("Add a new customer")
			elif user_input == '6':
				break
			else:
				print("You have entered an invalid option.")