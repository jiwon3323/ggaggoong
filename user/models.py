from django.db import models

class User(models.Model):
    """ User Model """
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    baby_name       = models.CharField(max_length=100)
    baby_gender     = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
    baby_birth      = models.DateField()
    address         = models.CharField(max_length=200)
    mom_name        = models.CharField(max_length=200)
    phone           = models.CharField(max_length=100)
    email           = models.EmailField(max_length=100, unique=True, default='')
    password        = models.CharField(max_length=300)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)


class Host(models.Model):
    user_id         = models.ForeignKey('User',on_delete=models.CASCADE)
    id_card         = models.IntegerField()
    certificate_id  = models.IntegerField()
    crimelog        = models.ImageField()
    crime_bool      = models.BooleanField()
    bank_img        = models.ImageField()
    bank_num        = models.IntegerField()
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
