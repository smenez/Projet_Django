from django.contrib import admin
from django.contrib import admin
from .models import Inscription, ToDoUserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(Inscription)

class ToDoUserProfileInLine(admin.StackedInline):
    model = ToDoUserProfile
    
class ToDoUserAdmin(UserAdmin):
    inlines = (ToDoUserProfileInLine, )
    
admin.site.unregister(User)
admin.site.register(User, ToDoUserAdmin)
