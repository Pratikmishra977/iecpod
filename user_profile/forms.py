from django.contrib.auth.models import User
from django import forms
from .models import Student_Detail, Student_Education

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Student_Detail
        fields = ['contact_no', 'dob', 'father_name', 'mother_name','gender', 'aadhaar_no', 'image']

class EducationUpdateForm(forms.ModelForm):

    class Meta:
        model = Student_Education
        fields = ['X_passing_year', 'X_school','X_board', 'X_marks','XII_passing_year', 'XII_school','XII_board', 'XII_marks','UG_passing_year', 'UG_college','UG_university', 'UG_marks', 'PG_passing_year', 'PG_college','PG_university', 'PG_marks']