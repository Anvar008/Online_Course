from django.contrib import admin
from course.models import Category, Course, Event, Register

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author_name', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_add_time', 'price')
    search_fields = ('title', 'price')
    list_filter = ('price',)

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')
