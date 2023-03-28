from django.contrib import admin
from .models import Job, Employee


@admin.register(Job)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('job', 'salary', 'created', 'modified')


@admin.register(Employee)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('name', 'job', 'image', 'active', 'created', 'modified')
