from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app01.models import User
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    # 添加自定义字段到管理界面
    list_display = ['username', 'email', 'is_staff', 'mobile']  # 包含自定义字段
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('mobile',)}),  # 添加自定义字段的显示区域
    )

admin.site.register(User, CustomUserAdmin)