from django.contrib import admin
from portal_fresia import models
from django.contrib.auth.models import Permission



def load():
    admin.site.register(Permission)

