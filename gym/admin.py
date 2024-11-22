from django.contrib import admin
from .models import *

# Register your models here.

from django.contrib import admin
from .models import MemberEnquiry


class MemberEnquiryAdmin(admin.ModelAdmin):
    list_display = ["name", "contact", "emailid", "branch", "issue", "submitted_at"]
    list_filter = ["branch", "issue"]
    search_fields = ["name", "emailid"]


admin.site.register(Contact)
admin.site.register(Enquiry)
admin.site.register(Equipment)
admin.site.register(Member)
admin.site.register(Plan)
admin.site.register(MemberEnquiry, MemberEnquiryAdmin)
admin.site.register(Blog)
