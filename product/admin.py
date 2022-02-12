from django.contrib import admin

# Register your models here.
class HomepageAdmin(admin.ModelAdmin):
    list_display = ('name')