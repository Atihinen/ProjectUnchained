from django import forms
from company.models import Company

def get_company_fields(dis_fields = None):
    disabled_fields = ["id", "admin"]
    if dis_fields:
        disabled_fields = dis_fields
    fields = []
    for f in Company._meta.fields:
        if f.name not in disabled_fields:
            fields.append(f.name)
    return fields

class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            if self.fields[f].widget.__class__.__name__ != "CheckboxInput":
                classes = self.fields[f].widget.attrs.get('class', '')
                classes += ' form-control'
                self.fields[f].widget.attrs['class'] = classes            
    
class BootstrapForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BootstrapForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            classes = self.fields[f].widget.attrs.get('class', '')
            classes += ' form-control'
            self.fields[f].widget.attrs['class'] = classes
    

class RegisterForm(BootstrapForm):
    username = forms.CharField(max_length=20, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    email = forms.EmailField(required=True)
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

class CompanyForm(BootstrapModelForm):
    class Meta:
        model = Company
        fields = get_company_fields()
    
    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)

class CompanyRegistrationForm(BootstrapModelForm):
    class Meta:
        model = Company
        fields = get_company_fields(['id', 'admin'])
    
    def __init__(self, *args, **kwargs):
        super(CompanyRegistrationForm, self).__init__(*args, **kwargs)        
        
    