class Customer():
	def __init__(self, customer_id, first_name, last_name):
		self.id = customer_id
		self.first_name = first_name
		self.last_name = last_name
		self.current_video_rentals = []