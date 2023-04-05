from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Student, Teacher, Class


class StudentRegistrationForm(UserCreationForm):
    full_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('email', 'full_name', 'password1', 'password2', 'is_student')
        labels = {'is_student': 'Are you a student?'}

class TeacherRegistrationForm(UserCreationForm):
    full_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('email', 'full_name', 'password1', 'password2', 'is_teacher')
        labels = {'is_teacher': 'Are you a teacher?'}

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')


# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zip_code', 'school', 'grade', 'parent_name', 'parent_email', 'parent_phone')

# class TeacherForm(forms.ModelForm):
#     class Meta:
#         model = Teacher
#         fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zip_code', 'school', 'grade', 'parent_name', 'parent_email', 'parent_phone')

# class ClassForm(forms.ModelForm):
#     class Meta:
#         model = Class
#         fields = ('name', 'description', 'teacher', 'students', 'start_date', 'end_date', 'start_time', 'end_time', 'days', 'price', 'max_students', 'min_students')
