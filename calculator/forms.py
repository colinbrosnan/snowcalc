from django import forms
from .models import Search


class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['zip', 'snow_days_this_year', 'school_type']
