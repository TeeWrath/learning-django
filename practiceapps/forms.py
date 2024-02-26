from django import forms

class usersForm(forms.Form) :
    num1 = forms.CharField(label="Value1", required=False)
    num2 = forms.CharField(label="Value2", required=False)
    num3 = forms.CharField(label="Value3", required=False)
    num4 = forms.CharField(label="Value4", required=False)
    num5 = forms.CharField(label="Value5", required=False)
    # num6 = forms.CharField(label="Value6", required=False)