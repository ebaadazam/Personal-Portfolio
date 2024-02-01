from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(("name"), max_length=50)
    email = models.CharField(("email"), max_length=50)
    number = models.CharField(("number"), max_length=10)
    enquiry = models.CharField(("enquiry"), max_length=100)
    # city = models.CharField(("city"), max_length=50)
    # state = models.CharField(("state"), max_length=50)
    date = models.DateField(("date"), auto_now=False, auto_now_add=False)
    
     # Now we want the name of the person who submit the form not the contact_obj in database
    def __str__(self):
        return self.name