from user_storage import UserStorage

class Signup:

	def __init__(self, builder, observers=None):

		self.observers = observers or []

	def signUp():

		# make a user_storage + user_observer
		UserStorage.save('teste')
		
        password = self.builder.get_password()
		
		for observer in self.observers:
        	observer.update(user)
		
		
	def login():
		pass
