from django.contrib import admin
from .models import Post, Category, Author,Signup, CourseOverview,Comment


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Signup)
admin.site.register(CourseOverview)
admin.site.register(Comment)


# Register your models here.
