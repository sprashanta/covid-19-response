from django.conf import settings
from django.db import models


class Hospital(models.Model):
    name = models.CharField('Hospital Name', max_length=30)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Specialist(models.Model):
    name = models.CharField('Specialist', max_length=30)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Degree(models.Model):
    degree = models.CharField('Degree', max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.degree


class IcuBed(models.Model):
    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE, verbose_name='Hospital Name')
    icu_bed_number = models.IntegerField(verbose_name='Hospital ICU Bed Number')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hospital


class OxygenCylinder(models.Model):
    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE, verbose_name='Hospital Name')
    oxygen_cylinder_number = models.IntegerField(verbose_name='Oxygen Cylinder Number')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hospital


class Plasma(models.Model):
    donor_name = models.CharField(max_length=35, verbose_name='Donor Name')
    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE, verbose_name='Hospital Name')
    group = (
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    blood_group = models.CharField(default=False, choices=group, max_length=4, verbose_name='Blood Group')
    donor_location = models.TextField(verbose_name='Donor Location')
    phone_number = models.CharField(max_length=12, verbose_name='Phone Number')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.donor_name
