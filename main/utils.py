from main.models import ShortedLink
from django.utils.crypto import get_random_string


def get_valid_shorted_link():
    shorted_link = get_random_string(length=8)
    counter = 0
    while ShortedLink.objects.filter(shorted=shorted_link).exists() and counter <= 10:
        counter += 1
        print('while', counter)
        shorted_link = get_random_string(length=8)
    return shorted_link
