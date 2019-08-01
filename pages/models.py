from django.db import models
from django.urls import reverse


class Bio(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    birth_cert = models.CharField(max_length=100)
    nat_id = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('new_school')

    def __str__(self):
        return self.first_name + self.last_name


class SchoolInfo(models.Model):
    school_name = models.CharField(max_length=100)
    school_address = models.CharField(max_length=100)
    academic_level = models.CharField(max_length=100)
    year_of_completion = models.CharField(max_length=100)
