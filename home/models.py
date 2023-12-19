# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Patient(models.Model):

    #__Patient_FIELDS__
    first name = models.CharField(max_length=255, null=True, blank=True)
    last name = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)

    #__Patient_FIELDS__END

    class Meta:
        verbose_name        = _("Patient")
        verbose_name_plural = _("Patient")


class Doctor(models.Model):

    #__Doctor_FIELDS__
    firstname = models.CharField(max_length=255, null=True, blank=True)
    last name = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    speciality = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)

    #__Doctor_FIELDS__END

    class Meta:
        verbose_name        = _("Doctor")
        verbose_name_plural = _("Doctor")


class Appointment(models.Model):

    #__Appointment_FIELDS__
    patient = models.CharField(max_length=255, null=True, blank=True)
    doctor = models.CharField(max_length=255, null=True, blank=True)
    time = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)

    #__Appointment_FIELDS__END

    class Meta:
        verbose_name        = _("Appointment")
        verbose_name_plural = _("Appointment")



#__MODELS__END
