from django.db import models
from django.db.models.constraints import CheckConstraint
from staff.models import Course_Instructor
from PIL import Image

class Course_Detail(models.Model):
    course_name = models.CharField(max_length=150, unique= True)
    course_instructor = models.ForeignKey(Course_Instructor, on_delete=models.CASCADE)
    about_course = models.TextField()
    prerequisit = models.TextField()
    course_duration = models.CharField(max_length=30)
    syllabus =models.TextField(null=True, blank=True)
    course_info = models.TextField(null=True, blank=True)
    course_image = models.ImageField(default='default.jpg', upload_to='course_cover_pics')
    course_fee = models.IntegerField()
    course_requirement = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.course_name


    def save(self,*args, **kwargs):
        super(Course_Detail, self).save(*args, **kwargs)

        img = Image.open(self.course_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Course_Video(models.Model):
    course_id = models.ForeignKey(Course_Detail, on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=50, unique=True)
    topic_order = models.SmallIntegerField()
    video = models.FileField(upload_to='course_videos')

    def __str__(self):
        return self.topic_name