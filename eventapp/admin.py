from django.contrib import admin

from eventapp import models

# Register your models here.
admin.site.register(models.Login)

admin.site.register(models.Teacher)
admin.site.register(models.Student)