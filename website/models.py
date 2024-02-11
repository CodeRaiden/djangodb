from django.db import models

# Create your models here.
class Member(models.Model):
 fname = models.CharField(max_length = 50)
 lname = models.CharField(max_length = 100)
 email = models.EmailField(max_length = 100)
 password = models.CharField(max_length = 50)
 # note we do not need to include a maximum length for IntegerField function
 age = models.IntegerField()

 # given the model object/instance a string representation
 def __str__ (self):
  return self.fname + " " + self.lname

 # after creating the model and adding/pushing the migrations to the database server, we can register the created model in the admin.py server file of our application inorder for the table to be rendered in the admin server page