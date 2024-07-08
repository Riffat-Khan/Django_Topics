from django.contrib import admin
from .models import members
    
    # def parserecord(self):
    #     return filter(lambda x:x in 'riffat', self.list_display)
    
def salary_including_bonus(modeladmin, request, queryset):
    for member in queryset:
        member.salary += member.bonus
        member.save()
    
salary_including_bonus.short_description = 'total salary'

class members_data(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "phone", "salary")
    actions = [salary_including_bonus,]
         

# Register your models here.
admin.site.register(members, members_data)
