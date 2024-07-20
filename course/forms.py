from django import forms
from .models import Course,Teacher,Speciality

# class CourseForm(forms.Form):
    # title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=200)
    # description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # mentor = forms.IntegerField()
    # image = forms.ImageField()
    # price = forms.FloatField()
    # rating = forms.FloatField()

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'mentor', 'price', 'rating']
class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model=Course
        fields = ['title', 'description',  'price', 'rating','active_students']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['full_name', 'position']
class TeacherUpdateForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields = ['full_name', 'position']




class SpecialityForm(forms.ModelForm):
    class Meta:
        model = Speciality
        fields = ['title', 'course']
class SpecialityUpdateForm(forms.ModelForm):
    class Meta:
        model=Speciality
        fields = ['title', 'created']



