from django.db import models

class Faculty(models.Model):
    status = models.CharField(default='active',max_length=8)
    created_date = models.DateTimeField(auto_now_add=True)
    deleted_date = models.DateTimeField(null=True)

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

class School(models.Model):
    status = models.CharField(default='active',max_length=8)
    created_date = models.DateTimeField(auto_now_add=True)
    deleted_date = models.DateTimeField(null=True)

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    faculty_fk = models.ForeignKey(Faculty, on_delete=models.CASCADE)

class Section(models.Model):
    status = models.CharField(default='active',max_length=8)
    created_date = models.DateTimeField(auto_now_add=True)
    deleted_date = models.DateTimeField(null=True)

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    uc = models.IntegerField()
    semester = models.IntegerField()
    TYPE = (
        ('M', 'mandatory'),
        ('E', 'elective'),
    )
    type = models.CharField(max_length=1, choices=TYPE)
    ht = models.FloatField()
    hp = models.FloatField()
    hl = models.FloatField()
    school_fk = models.ForeignKey(School, on_delete=models.CASCADE)

class Enrollment(models.Model):
    status = models.CharField(default='active',max_length=8)
    created_date = models.DateTimeField(auto_now_add=True)
    deleted_date = models.DateTimeField(null=True)

    TYPE = (
        ('S', 'student'),
        ('T', 'teacher'),
    )
    type = models.CharField(max_length=1, choices=TYPE)

class Enroll_Sect(models.Model):
    enrollment_fk = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    section_fk = models.ForeignKey(Section, on_delete=models.CASCADE)

class Person(models.Model):
    status = models.CharField(default='active',max_length=8)
    created_date = models.DateTimeField(auto_now_add=True)
    deleted_date = models.DateTimeField(null=True)

    cedula = models.CharField(max_length= 11)
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length=20)
    enrollment_fk = models.ForeignKey(Enrollment, on_delete=models.CASCADE)


