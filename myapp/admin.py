from django.contrib import admin
from myapp.models import *
# Register your models here.

class AdminPortfolio(admin.ModelAdmin):
    list_display = ['id','name','client','picture1','date',]

admin.site.register(Portifolio,AdminPortfolio)


class AdminCategory(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(Category,AdminCategory)


class AdminService(admin.ModelAdmin):
    list_display = ['id','picture','name','information']

admin.site.register(Service,AdminService)


class AdminTeam(admin.ModelAdmin):
    list_display = ['id','picture','name','position','information','url1']

admin.site.register(Team,AdminTeam)

class AdminContact(admin.ModelAdmin):
    list_display = ['id','name','email','subject','message']

admin.site.register(Contact,AdminContact)