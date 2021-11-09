from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):    
   
   use_in_migrations = True    
   
   def create_user(self,username,mom_name,baby_name,baby_birth,baby_gender,address,phone, email, password):        
       
       if not email:            
           raise ValueError('must have user eamil')
       if not password:            
           raise ValueError('must have user password')

       user = self.model(  
           username=username,
           mom_name=mom_name,
           baby_name=baby_name,
           baby_birth=baby_birth,
           baby_gender=baby_gender,
           address=address,
           phone=phone,
           email=email,
       )        
       user.set_password(password)        
       user.save(using=self._db)        
       return user

   def create_superuser(self, email, password):        
   
       user = self.create_user(            
           email = email,
           password=password        
       )
       user.is_admin = True
       user.is_superuser = True
       user.save(using=self._db)
       return user 




class User(AbstractBaseUser, PermissionsMixin):
    """ User Model """
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    username        = models.CharField(max_length=100, null=True)
    baby_name       = models.CharField(max_length=100)
    baby_gender     = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
    baby_birth      = models.DateField(null=True)
    address         = models.CharField(max_length=200)
    mom_name        = models.CharField(max_length=200)
    phone           = models.CharField(max_length=100)
    email           = models.EmailField(max_length=100, unique=True, default='')
    password        = models.CharField(max_length=300)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    is_active       = models.BooleanField(default=True)
    is_admin        = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()
    @property
    def is_staff(self):
       return self.is_admin


class Host(models.Model):
    user_id         = models.OneToOneField('User',on_delete=models.CASCADE, related_name="host_info")
    id_card1        = models.IntegerField()
    id_card2        = models.IntegerField()
    certificate_id  = models.IntegerField()
    crimelog        = models.ImageField(upload_to='ßimages/crimeLogImage',blank=True, null=True)
    crime_bool      = models.BooleanField(default=False)
    bank_img        = models.ImageField(upload_to='images/bankImage',blank=True, null=True)
    bank_num        = models.IntegerField()
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
