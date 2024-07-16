from django.contrib import admin
from .models import members, Profile, Project, Task, Document, Comment
    
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
         
class display(admin.ModelAdmin):
    list_display = ("user", "role", "contact_number")

class project_display(admin.ModelAdmin):
    list_display = ("title", "start_date", "end_date")
         

# Register your models here.
admin.site.register(Profile, display)
admin.site.register(Project, project_display)
admin.site.register(Task)
admin.site.register(Document)
admin.site.register(Comment)
