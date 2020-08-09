'''
URLS files for Puppies App
'''

from django.urls import path
from .views import Puppies

urlpatterns = [
     path('', Puppies.as_view(), name='puppies')
]
