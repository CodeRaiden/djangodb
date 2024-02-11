from django.contrib import admin
# import the Member model
from .models import Member

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
 list_display = ['fname', 'lname', 'email']

admin.site.register(Member, MemberAdmin)