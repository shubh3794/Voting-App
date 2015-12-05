from django.db import models

# Create your models here.
class Question(models.Model):
	question = models.TextField(null=False,blank=False)
	pub_date = models.DateTimeField('date published',auto_now_add=True)
	def save(self, *args, **kwargs):
		if self.question[len(self.question)-1] != '?':
			print 'question should end with question mark'
			return
		else:
			super(Question,self).save(*args,**kwargs)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
