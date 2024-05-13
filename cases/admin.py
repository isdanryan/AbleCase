from django.contrib import admin
from .models import Cases, CaseTypes, Communications

admin.site.register(Cases)
admin.site.register(CaseTypes)
admin.site.register(Communications)
