from django.contrib import admin
from .models import ReadNum, ReadDetail

@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    # 在admin中列表展示
    list_display = ("read_num", "content_object")

@admin.register(ReadDetail)
class ReadNumAdmin(admin.ModelAdmin):
    # 在admin中列表展示
    list_display = ("date", "read_num", "content_object")