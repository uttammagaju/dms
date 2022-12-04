from django import forms

from . models import *

class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['name',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control',
                }
            )

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = []

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class' : 'form-control',
                }
            )