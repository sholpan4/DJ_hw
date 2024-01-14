from django.contrib import admin

from .models import *

admin.site.register(AdvUser)
admin.site.register(Machine)
admin.site.register(Spare)
admin.site.register(SMS)