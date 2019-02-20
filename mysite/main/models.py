from django.db import models
import datetime

availableRooms = (
		('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'),
)

class Burd326(models.Model):

	# which apartment number on the street
	apartmentNumbers = (
		('1', '1'),
		('2', '2'),
		('3', '3'),
	)
	apartment_number = models.CharField(max_length=1,choices=apartmentNumbers,default=1)
	def __str__(self):
		return self.apartment_number
	
	# Is the apartment available
	availability = (
		('Yes', 'Yes'),
		('No', 'No'),
	)
	is_available = models.CharField(max_length=3,choices=availability,default=1)
	def __str__(self):
		return self.is_available

	# If not avaiable, how long is it committed until
	next_date_available = models.DateField(default=datetime.date.today)

	# how many bedrooms
	number_of_bedrooms = models.CharField(max_length=1,choices=availableRooms,default=1)
	def __str__(self):
		return self.number_of_bedrooms

	# rent per month (also the amount of the security deposit
	rent_per_month = models.PositiveSmallIntegerField(default=0)
	
	# features
	features = models.TextField(default='', blank=True)

	# appliances
	appliances = models.TextField(default='', blank=True)

	# additional notes
	notes = models.TextField(default='', blank=True)

class Burd328(models.Model):

	# which apartment number on the street
	apartmentNumbers = (
		('1', '1'),
		('2', '2'),
	)
	apartment_number = models.CharField(max_length=1,choices=apartmentNumbers,default=1)
	def __str__(self):
		return self.apartment_number
	
	# Is the apartment available
	availability = (
		('Yes', 'Yes'),
		('No', 'No'),
	)
	is_available = models.CharField(max_length=3,choices=availability,default=1)
	def __str__(self):
		return self.is_available

	# If not avaiable, how long is it committed until
	next_date_available = models.DateField(default=datetime.date.today)

	# how many bedrooms
	number_of_bedrooms = models.CharField(max_length=1,choices=availableRooms,default=1)
	def __str__(self):
		return self.number_of_bedrooms

	# rent per month (also the amount of the security deposit
	rent_per_month = models.PositiveSmallIntegerField(default=0)
	
	# features
	features = models.TextField(default='', blank=True)

	# appliances
	appliances = models.TextField(default='', blank=True)

	# additional notes
	notes = models.TextField(default='', blank=True)

class Orange229(models.Model):

	# which apartment number on the street
	apartmentNumbers = (
		('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'),
		('5', '5'),
		('6', '6'),
	)
	apartment_number = models.CharField(max_length=1,choices=apartmentNumbers,default=1)
	def __str__(self):
		return self.apartment_number
	
	# Is the apartment available
	availability = (
		('Yes', 'Yes'),
		('No', 'No'),
	)
	is_available = models.CharField(max_length=3,choices=availability,default=1)
	def __str__(self):
		return self.is_available

	# If not avaiable, how long is it committed until
	next_date_available = models.DateField(default=datetime.date.today)

	# how many bedrooms
	number_of_bedrooms = models.CharField(max_length=1,choices=availableRooms,default=1)
	def __str__(self):
		return self.number_of_bedrooms

	# rent per month (also the amount of the security deposit
	rent_per_month = models.PositiveSmallIntegerField(default=0)
	
	# features
	features = models.TextField(default='', blank=True)

	# appliances
	appliances = models.TextField(default='', blank=True)

	# additional notes
	notes = models.TextField(default='', blank=True)

class Earl44(models.Model):

	# which apartment number on the street
	apartmentNumbers = (
		('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'),
		('5', '5'),
		('6', '6'),
		('7', '7'),
		('8', '8'),
	)
	apartment_number = models.CharField(max_length=1,choices=apartmentNumbers,default=1)
	def __str__(self):
		return self.apartment_number
	
	# Is the apartment available
	availability = (
		('Yes', 'Yes'),
		('No', 'No'),
	)
	is_available = models.CharField(max_length=3,choices=availability,default=1)
	def __str__(self):
		return self.is_available

	# If not avaiable, how long is it committed until
	next_date_available = models.DateField(default=datetime.date.today)

	# how many bedrooms
	number_of_bedrooms = models.CharField(max_length=1,choices=availableRooms,default=1)
	def __str__(self):
		return self.number_of_bedrooms

	# rent per month (also the amount of the security deposit
	rent_per_month = models.PositiveSmallIntegerField(default=0)
	
	# features
	features = models.TextField(default='', blank=True)

	# appliances
	appliances = models.TextField(default='', blank=True)

	# additional notes
	notes = models.TextField(default='', blank=True)

class Earl46(models.Model):

	# which apartment number on the street
	apartmentNumbers = (
		('1', '1'),
		('2', '2'),
	)
	apartment_number = models.CharField(max_length=1,choices=apartmentNumbers,default=1)
	def __str__(self):
		return self.apartment_number
	
	# Is the apartment available
	availability = (
		('Yes', 'Yes'),
		('No', 'No'),
	)
	is_available = models.CharField(max_length=3,choices=availability,default=1)
	def __str__(self):
		return self.is_available

	# If not avaiable, how long is it committed until
	next_date_available = models.DateField(default=datetime.date.today)

	# how many bedrooms
	number_of_bedrooms = models.CharField(max_length=1,choices=availableRooms,default=1)
	def __str__(self):
		return self.number_of_bedrooms

	# rent per month (also the amount of the security deposit
	rent_per_month = models.PositiveSmallIntegerField(default=0)
	
	# features
	features = models.TextField(default='', blank=True)

	# appliances
	appliances = models.TextField(default='', blank=True)

	# additional notes
	notes = models.TextField(default='', blank=True)

class Earl48(models.Model):

	# which apartment number on the street
	apartmentNumbers = (
		('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'),
	)
	apartment_number = models.CharField(max_length=1,choices=apartmentNumbers,default=1)
	def __str__(self):
		return self.apartment_number
	
	# Is the apartment available
	availability = (
		('Yes', 'Yes'),
		('No', 'No'),
	)
	is_available = models.CharField(max_length=3,choices=availability,default=1)
	def __str__(self):
		return self.is_available

	# If not avaiable, how long is it committed until
	next_date_available = models.DateField(default=datetime.date.today)

	# how many bedrooms
	number_of_bedrooms = models.CharField(max_length=1,choices=availableRooms,default=1)
	def __str__(self):
		return self.number_of_bedrooms

	# rent per month (also the amount of the security deposit
	rent_per_month = models.PositiveSmallIntegerField(default=0)
	
	# features
	features = models.TextField(default='', blank=True)

	# appliances
	appliances = models.TextField(default='', blank=True)

	# additional notes
	notes = models.TextField(default='', blank=True)
