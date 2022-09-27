from django.contrib import admin

from .models import Element,Category,Type, ElementImages

# Register your models here.

class TypeAdmin(admin.ModelAdmin):
    list_display=('id','title')
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','title')



class ElementImagesInline():
    model = ElementImages
    extra = 3

class ElementAdmin(ImportExportModelAdmin):
    resource_class=ElementResource
    list_display=('id','title')
    inlines = [ElementImagesInline]




admin.site.register(Type, TypeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Element, ElementAdmin)