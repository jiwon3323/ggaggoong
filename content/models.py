from django.db import models
from user.models import User, Host

# Create your models here.
class Contents(models.Model):
    title_img = models.ImageField(
        upload_to="content/image/",
        blank=True,
        null=True
    )
    title_name = models.CharField(max_length=100)
    sub_title_name = models.CharField(max_length=100)
    content_date = models.DateTimeField()
    duration = models.IntegerField()
    location = models.CharField(max_length=100)
    people_number = models.IntegerField()
    age_min = models.IntegerField()
    age_max = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    host_id = models.ForeignKey(Host, on_delete=models.CASCADE, null=True)

class Contents_Detail(models.Model):
    detail = models.CharField(max_length=500)
    detail_img = models.ImageField(
        upload_to="content/detail_image/",
        blank=True,
        null=True
    )
    contents_id = models.ForeignKey('Contents', on_delete=models.CASCADE, null=True)
    host_id = models.ForeignKey(Host, on_delete=models.CASCADE, null=True)


class Reserve(models.Model):
    content_id = models.ForeignKey(Contents, on_delete=models.PROTECT)
    reserve_user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    reserve_alive = models.BooleanField(default=True)
    canceled_at = models.DateTimeField(null=True)