from django import forms
from .models import Course_Instructor
from online_course.models import Course_Detail, Course_Video

class StaffLoginForm(forms.ModelForm):
    class Meta:
        model = Course_Instructor
        fields = ['email', 'password']

class StaffUpdateForm(forms.ModelForm):
    class Meta:
        model = Course_Instructor
        fields = ['email', 'name', 'contact_no', 'desc', 'image']



class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course_Detail
        fields = ['course_name','about_course', 'prerequisit', 'course_duration',
                  'syllabus', 'course_info', 'course_image', 'course_fee', 'course_requirement']

class VideoUpdationForm(forms.ModelForm):
    class Meta:
        model = Course_Video
        fields = ['topic_name', 'topic_order', 'video']
