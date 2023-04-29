from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources,fields

class feesresource(resources.ModelResource):
    class Meta:
        model = feesdetails
        

class fees(ImportExportModelAdmin):
    resource_classes = [feesresource]
    

admin.site.register(feesdetails,fees)