from django import forms

import datetime

from .models import Event


class EventForm(forms.ModelForm):
    title = forms.CharField(
        label='Название события',
        max_length=200,
    )
    allow_wife = forms.BooleanField(
        label='Допускаются жены',
        required=False,
    )
    allow_family = forms.BooleanField(
        label='Допускается семья',
        required=False,
    )
    for_kids = forms.BooleanField(
        label='Для детей',
        required=False,
    )
    number_of_participants = forms.IntegerField(
        label='Число участников',
        max_value=1000,
    )
    event_date = forms.DateField(
        initial=datetime.date.today,
        label='Дата проведения',
        help_text='ГГГГ-ММ-ДД',
    )
    prepay_date = forms.DateField(
        required=False,
        label='Дата предоплаты',
        help_text='ГГГГ-ММ-ДД',
    )
    personal_transportation = forms.BooleanField(
        label='Персональный транспорт',
        required=False,
    )
    company_transport = forms.CharField(
        required=False,
        label='Транспорт компании',
        max_length=500,
        widget=forms.Textarea,
    )
    company_transport_size = forms.IntegerField(
        required=False,
        label='Вместительность транспорта компании',
        max_value=1000,
    )
    main_price = forms.IntegerField(
        required=False,
        label='Цена',
        max_value=1000000,
    )
    other_prices = forms.CharField(
        required=False,
        label='Цены на дополнительные вещи',
        max_length=500,
        widget=forms.Textarea,
    )
    deposit = forms.IntegerField(
        required=False,
        label='Депозит',
    )
    some_properties = forms.CharField(
        required=False,
        label='Описание',
        max_length=1000,
        widget=forms.Textarea,
    )

    owner = forms.ChoiceField(
        choices=(),
        disabled=True,
        widget=forms.HiddenInput,
        required=False,
    )

    class Meta:
        model = Event
        exclude = ['owner']
