from django.contrib import admin
from .models import UserMentor, UserMentee, CustomUser


class MentorAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "email",
    ]
    list_filter = [
                    "email",
                    ]
    search_fields = [
        "first_name",
        "last_name",
    ]


class MenteeAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "email",
    ]
    list_filter = [
                    "email",
                    ]
    search_fields = [
        "first_name",
        "last_name",
    ]


admin.site.register(UserMentor, MentorAdmin)
admin.site.register(UserMentee, MenteeAdmin)
