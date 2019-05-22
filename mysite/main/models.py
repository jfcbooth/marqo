from django.db import models #Go get me the models python module from the django.db package.

class Name(models.Model):
    first = models.CharField(max_length=32)
    last = models.CharField(max_length=32)

    # Gets called whenever we ask for a string representation of the model
    def __str__(self):
      return "%s %s" % (self.first, self.last)


# Defines many names can go with one email
class Email(models.Model):
    #name = models.ForeignKey(Name, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=32, default='')
    last_name = models.CharField(max_length=32, default='')
    email = models.CharField(max_length=32, default='')
    questions = models.CharField(max_length=1024, default='')
    
    # Gets called whenever we ask for a string representation of the model
    def __str__(self):
      return "%s (%s, %s)" % (self.email, self.last_name, self.first_name)
