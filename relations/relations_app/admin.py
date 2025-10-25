from django.contrib import admin
from relations_app.models import Human, DriveLicense, City, Student, Course

admin.site.register(Human)
admin.site.register(DriveLicense)
admin.site.register(City)
admin.site.register(Student)
admin.site.register(Course)
