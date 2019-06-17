
class car():
	def __init__(self, make, model, color, price):
		self.make = make
		self.model = model
		self.color = color
		self.price = price
		
	def start(self):
		self.speed = 0
		return 0
	
	def move(self):
		self.speed += 5
		
	def stop(self):
		self.speed = 0
		
	def info(self):
		print('\nMake:', self.make, '\nModel:', self.model, '\nColor:', self.color, '\nPrice:', self.price, '\nSpeed:', self.speed, '\n')
		
		
mini = car('BMW', 'Mini Cooper', 'Matte Black', 5300000)

mini.start()
mini.move()
mini.move()
mini.move()
mini.move()
mini.info()
mini.stop()
mini.info()



