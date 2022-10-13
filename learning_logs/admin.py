from django.contrib import admin
from .models import Topic, Entry
# Зарешистрируйте здесь ваши модели.
admin.site.register(Topic) 
admin.site.register(Entry)
