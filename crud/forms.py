from .models import Employee
from django import forms

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ("__all__")

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class']='form-control'
            field.widget.attrs['placeholder'] ='Enter '+field.label+" *"

