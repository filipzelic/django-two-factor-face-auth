from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserFaceImage
from .utils import base64_file


class UserCreationForm(UserCreationForm):
    image = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserFaceImage without database save")
        user = super(UserCreationForm, self).save(commit=True)
        image = base64_file(self.data['image'])
        face_image = UserFaceImage(user=user, image=image)
        face_image.save()
        return user

class AuthenticationForm(AuthenticationForm):
    image = forms.CharField(widget=forms.HiddenInput())