from django.contrib import admin
from .models import BlogType, Blog

@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    # 在admin中列表展示
    list_display = ("id","type_name")
    # 排序 加负号 -id 倒序
    ordering = ("id",)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # 在admin中列表展示
    list_display = ("id", "title", "blog_type", "author", "get_read_num", "created_time", "last_updated_time")
    # 排序 加负号 -id 倒序
    ordering = ("created_time",)
