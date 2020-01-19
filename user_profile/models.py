from django.db import models
from django.db.models.constraints import CheckConstraint
from django.contrib.auth.models import User
from PIL import Image

class Student_Detail(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=12, unique= True, null=True, blank= False)
    dob = models.DateField(null=True, blank= False)
    gender = models.CharField(max_length=1, null=True, blank= False)
    father_name = models.CharField(max_length=30, null=True, blank= False)
    mother_name = models.CharField(max_length= 30, null=True, blank= False)
    aadhaar_no = models.CharField(max_length=12, unique= True ,null=True, blank= False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username +'Profile'

    def save(self,*args, **kwargs):
        super(Student_Detail, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



class Student_Education(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    X_passing_year = models.IntegerField( null=True, blank= True,)
    X_school = models.CharField(max_length= 50, null=True, blank= True)
    X_board = models.CharField(max_length= 50, null=True, blank= True)
    X_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    XII_passing_year = models.IntegerField( null=True, blank=True)
    XII_school = models.CharField(max_length=50, null=True, blank=True)
    XII_board = models.CharField(max_length=50, null=True, blank=True)
    XII_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    UG_passing_year = models.IntegerField( null=True, blank=True)
    UG_college = models.CharField(max_length=50, null=True, blank=True)
    UG_university = models.CharField(max_length=50, null=True, blank=True)
    UG_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    PG_passing_year = models.IntegerField( null=True, blank=True)
    PG_college = models.CharField(max_length=50, null=True, blank=True)
    PG_university = models.CharField(max_length=50, null=True, blank=True)
    PG_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.user.username + 'Profile'