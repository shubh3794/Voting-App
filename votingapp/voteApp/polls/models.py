from django.db import models
from django.conf import settings
from authentication.models import Account
from django.utils import timezone
import datetime
# Create your models here.
class Question(models.Model):
	createdby = models.ForeignKey(Account,on_delete=models.CASCADE, null=True,blank=True)
	question_text = models.CharField(max_length=2000,null=False)
	pub_date = models.DateTimeField('date published')
	def save(self, *args, **kwargs):
		print settings.BASE_DIR
		print self.question_text
		if self.question_text[len(self.question_text)-1] != '?':
			print 'question should end with question mark'
			return
		else:
			super(Question,self).save(*args,**kwargs)
	def was_published_recently(self):
		return self.pub_date >= self.pub_date - datetime.timedelta(days=1)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'
	def __unicode__(self):
		return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
		return self.choice_text
