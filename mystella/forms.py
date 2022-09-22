from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .models import Review,RATE_CHOICES

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Userprofile
        fields = ['name','Sex', 'Address','Email', 'Phone','is_admin',]




from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class AddReviewForm(forms.ModelForm):
    class Meta :
        model = Review
        fields = '__all__'




class RateForm(forms.ModelForm):
	rate = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True)
	class Meta:
		model = Review
		fields = ('rate',)

from .models import Customer
class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'

class AddProductForm(forms.ModelForm):
    class Meta :
        model = Product
        fields = '__all__'

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = Images
        fields = ('image',)

class AddCatalogForm(forms.ModelForm):
    class Meta :
        model = Catalogue
        fields = ['title', 'description', 'image']

class AddBrandForm(forms.ModelForm):
    class Meta :
        model = Brand
        fields = ['name', 'image']

class OrderForm(forms.ModelForm):
    class Meta :
        model = OrderItem
        fields = '__all__'



