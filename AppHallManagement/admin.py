from django.contrib import admin
from .models import Student_Allocation
from .models import notice,author,category,frmGeneralInstructions
# Register your models here.

class authorModel(admin.ModelAdmin):
	list_display=["__str__"]
	search_fields=["__str__","details"]
	class Meta:
		Model=author
admin.site.register(author,authorModel)
class noticeModel(admin.ModelAdmin):
	list_display=["__str__",'posted_on']
	search_fields=["__str__","details"]
	list_per_page=10
	list_filter=["posted_on",'category']
	class Meta:
		Model=author
admin.site.register(notice,noticeModel)
class categoryModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    list_per_page = 10

    class Meta:
        Model = category
admin.site.register(category,categoryModel)
class studentModel(admin.ModelAdmin):
	search_fields=["__str__","roll_number"]
	list_per_page=10
	list_filter=['name']

	class Meta:
		Model=author
admin.site.register(Student_Allocation,studentModel)
class frmGeneral(admin.ModelAdmin):
	list_display=["__str__",'posted_on']
	search_fields=["__str__","details"]
	list_per_page=10
	list_filter=["posted_on",'category']
	class Meta:
		Model=author
admin.site.register(frmGeneralInstructions,frmGeneral)
