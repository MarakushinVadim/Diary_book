from django.forms import ModelForm

from record.models import Record
from users.forms import StyleFormMixin


class RecordForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Record
        exclude = (
            "author",
            "created_at",
        )
