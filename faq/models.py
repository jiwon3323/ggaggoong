from django.db import models
from content.models import Contents
from user.models import User, Host
# Create your models here.
class FAQ(models.Model):
    questioner      = models.ForeignKey('user.User', on_delete=models.CASCADE)
    faq_content     = models.ForeignKey('content.Contents', on_delete=models.CASCADE, related_name="host_content")
    question        = models.CharField(max_length=250)
    answer_id       = models.ForeignKey('FAQ_Answer', on_delete=models.CASCADE,null=True, blank=True)
    answer_done     = models.BooleanField(null=True, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at      = models.DateTimeField(auto_now=True,null=True, blank=True)

class FAQ_Answer(models.Model):
    answerer        = models.ForeignKey(Host, on_delete=models.CASCADE)
    question_id     = models.ForeignKey('FAQ', on_delete=models.CASCADE)
    answer          = models.CharField(max_length=250)
    created_at      = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at      = models.DateTimeField(auto_now=True,null=True, blank=True)
    


