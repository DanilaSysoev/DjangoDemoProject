from django.db import models


class Human(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False)
    city = models.ForeignKey(
        "City",
        on_delete=models.SET_NULL,
        related_name='humans',
        null=True
    )
    
    def __str__(self):
        return self.name


class DriveLicense(models.Model):
    number = models.CharField(primary_key=True)
    human = models.OneToOneField(
        Human, related_name='drive_license', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.number


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False)
    
    def __str__(self):
        return f'{self.name}: население {self.humans.count()} человек(а)'


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False)    
    
    def __str__(self):
        return self.name
    

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False)
    students = models.ManyToManyField(Student, blank=True, related_name='courses')
    
    def __str__(self):
        return f'{self.name}: студентов записано - {self.students.count()}'