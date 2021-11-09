from django.db import models

# Create your models here.
class FAQ(models.Model):
    questioner      = models.OneToOneField('User', on_delete=models.CASCADE)
    faq_content     = models.OneToOneField('Content', on_delete=models.CASCADE)
    question        = models.CharField(max_length=250)
    answer_id       = models.OneToOneField('FAQ_Answer', on_delete=models.CASCADE)
    answer_done     = models.BooleanField()

class FAQ_Answer(models.Model):
    answerer        = models.OneToOneField('User', on_delete=models.CASCADE)
    question_id     = models.OneToOneField('FAQ', on_delete=models.CASCADE)
    answer          = models.CharField(max_length=250)
    


