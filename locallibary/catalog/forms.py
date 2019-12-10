from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text='Enter a date between now and 4 week.')

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Проверка временых границ
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - reneval in past'))

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - reneval more 4 week ahead'))

        return data
