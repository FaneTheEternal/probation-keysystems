from django import forms


class EventForm(forms.Form):
    title = forms.CharField()

    allow_wife = forms.BooleanField()
    allow_family = forms.BooleanField()
    for_kids = forms.BooleanField()
    number_of_participants = forms.IntegerField()
    event_date = forms.DateField()
    prepay_date = forms.DateField()
    personal_transportation = forms.BooleanField()
    company_transport = forms.TextField()
    company_transport_size = forms.IntegerField()
    main_price = forms.IntegerField()
    other_prices = forms.TextField()
    deposit = forms.IntegerField()
    some_properties = forms.TextField()
