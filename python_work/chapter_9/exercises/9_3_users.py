class User():
	"""A class that models a user for an online forum"""
	def __init__(self, f_name, l_name,
				 age, city, hometown, *languages):
		"""Constructor - creates attributes, initialises them"""
		self.first_name = f_name;
		self.last_name = l_name;
		self.age = age
		self.city = city
		self.hometown = hometown
		self.languages = languages   	#languages is a tuple

	def describe_user(self):
		"""Prints all information about user as a neatly formatted string"""
		print("Name:\t" + self.first_name.title() 
			+ " " + self.last_name.title())
		print("Age:\t" + str(self.age))
		print("City:\t" + self.city)
		print("Hometown:\t" + self.hometown)
		print("Languages:\t" + str(self.languages))

	def greet_user(self):
		"""Displays a personalised greeting for the user"""
		print("Hello, " + self.first_name.title() + "! Welcome back!")

"""Creating three instances of user - calling both methods for each"""
saad = User('saad', 'siddiqui', 21, 'karachi', 'karachi',
	'english', 'urdu')
mashkoor = User('mashkoor', 'ahmed', 63, 'karachi', 'chittagong',
	'english', 'urdu', 'bangla')
nasreen = User('zarina', 'nasreen', 58, 'karachi', 'karachi', 
	'english', 'urdu')

"""Calling both functions for each instance"""
print("Saad".upper())
saad.greet_user()
saad.describe_user()

print("\nMashkoor".upper())
mashkoor.greet_user()
mashkoor.describe_user()

print("\nNasreen".upper())
nasreen.greet_user()
nasreen.describe_user()
