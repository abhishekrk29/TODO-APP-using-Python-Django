from django.contrib import admin
from todoapp.models.users import User
from todoapp.models.todo import TODO

# Register your models here.

admin.site.register(User)
admin.site.register(TODO)