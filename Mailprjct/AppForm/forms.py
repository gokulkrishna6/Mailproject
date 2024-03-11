from django import forms
from AppForm.models import Students


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'


# from django import forms


# class StudentsFrom(forms.Form):
#     std_id = forms.IntegerField()
#     Name =forms.CharField()
#     Course=forms.CharField()
#     Email=forms.EmailField()

