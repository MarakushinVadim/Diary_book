from django.contrib.auth.forms import UserCreationForm
from django.forms import BooleanField, ModelForm

from users.models import User


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password1", "password2")


class UserForm(StyleFormMixin, ModelForm):
    class Meta:
        model = User
        fields = (
            "email",
            "password",
        )
