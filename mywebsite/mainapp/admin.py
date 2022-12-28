from django.contrib import admin
from .models import Sample
from .models import FahisUser
from .models import Report
# Register your models here.

admin.site.register(Sample)
admin.site.register(FahisUser)
admin.site.register(Report)