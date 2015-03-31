from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class History(models.Model):
    sku = models.IntegerField()
    pic_url = models.CharField(max_length=128)
    cleaned_status = models.IntegerField()
    cleaned_by = models.ForeignKey('OptUser')
    cleaned_at = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return self.sku
    
class OptUser(models.Model):
    user = models.OneToOneField(User)
    regist_at = models.DateTimeField(auto_now_add = True)
    lst_login = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return self.user.username

