from django.contrib import admin
from .models import *
# Register your models he
# 
# re.
class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category)
admin.site.register(Post)
