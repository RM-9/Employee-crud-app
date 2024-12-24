from django import forms
from .models import Employee

class Employeeform(forms.ModelForm):
    
        class Meta:
            model=Employee
            fields=('name','emp_id','mobile','position')
            labels={
                'name':'Fullname',
                'emp_id':'Employee ID'
            }
            
        def __init__(self, *args, **kwargs):
            super(Employeeform, self).__init__(*args, **kwargs)
            self.fields['position'].empty_label = "Select"
