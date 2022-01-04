from django.forms import ModelForm
from .models import Setting_Table


class SettingForm(ModelForm):
    class Meta:
        model = Setting_Table
        fields = '__all__'
