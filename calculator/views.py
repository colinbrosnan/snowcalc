from django.shortcuts import render, redirect
from .models import Search
from .forms import SearchForm
import requests
import urllib
import datetime
from math import sqrt, pow


def home(request):

    def calculate(info):
        zip = info['zip']
        snow_days_this_year = info['snow_days_this_year']
        school_type = info['school_type']

        google_url = "https://maps.googleapis.com/maps/api/geocode/json?address="
        google_api = '&key=AIzaSyCGaAwOVp6ICcFkDDqtTshLGxuvNfwBS5M'

        google_response = requests.request(
            "GET", google_url + zip + google_api).json()

        latitute = google_response['results'][0]['geometry']['location']['lat']
        longitude = google_response['results'][0]['geometry']['location']['lng']

        headers = {
            'User-Agent': "colinbrosnan13@gmail.com",
        }

        weather_api = '0b39703acec239fa31144483a13e6fc3'
        weather_url = "https://api.openweathermap.org/data/2.5/onecall?lat=" + \
            str(latitute) + "&lon=" + str(longitude) + "&units=imperial&appid=" + weather_api

        weather_response = requests.request("GET", weather_url).json()
        first_timestamp = weather_response['hourly'][0]['dt']

        time_offset = requests.request("GET", "https://maps.googleapis.com/maps/api/timezone/json?location=" +
                                       str(latitute) + "," + str(longitude) + "&timestamp=" + str(first_timestamp) + google_api).json()

        time_offset = time_offset["rawOffset"]
        first_hour = int(first_timestamp + time_offset)
        first_hour = datetime.datetime.fromtimestamp(first_hour)
        first_hour = first_hour.hour

        target_call_time = 6
        index = 24 + target_call_time - first_hour
        target_forecast = weather_response['hourly'][index]

        if target_forecast.get('snow') is not None:
            inches_snow = target_forecast['snow']['1h'] * 10 * .0393
        else:
            inches_snow = 0

        feels_like = target_forecast['feels_like']
        temp = target_forecast['temp']

        chance_snowday = 0

        chance_snowday += 20 * sqrt(inches_snow)
        chance_snowday += pow(1.2589, -1 * feels_like)
        chance_snowday *= 2 / (1 + pow(2.7272, -.06*(36 - latitute)))

        def truncate(f, n):
            '''Truncates/pads a float f to n decimal places without rounding'''
            s = '{}'.format(f)
            if 'e' in s or 'E' in s:
                return '{0:.{1}f}'.format(f, n)
            i, p, d = s.partition('.')
            return '.'.join([i, (d+'0'*n)[:n]])

        return truncate(chance_snowday, 2)

    form = SearchForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

            info = {
                'zip': form.cleaned_data.get('zip'),
                'snow_days_this_year': form.cleaned_data.get('snow_days_this_year'),
                'school_type': form.cleaned_data.get('school_type'),
            }

            context = float(calculate(info))
            if (context > 100):
                context = 99.9
            if(context < 0):
                context = 00.0

            return render(request, 'calculator/results.html', {'context': context})
    else:
        form = SearchForm()

    return render(request, 'calculator/home.html', {'form': form})


def about(request):
    return render(request, 'calculator/about.html')


def contact_us(request):
    return render(request, 'calculator/contact-us.html')


def under_construction(request):
    return render(request, 'calculator/construction.html')


def privacy_policy(request):
    return render(request, 'calculator/privacy_policy.html')
