from django.contrib import admin

# Look for models in the same directory as this module
from .models import Topic, Entry

# Manage the model through the admin site
admin.site.register(Topic)
admin.site.register(Entry)