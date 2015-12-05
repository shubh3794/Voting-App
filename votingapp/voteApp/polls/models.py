from django.db import models

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=2000,null=False)
	pub_date = models.DateTimeField('date published',auto_now_add=True)
	def save(self, *args, **kwargs):
		print self.question_text
		if self.question_text[len(self.question_text)-1] != '?':
			print 'question should end with question mark'
			return
		else:
			super(Question,self).save(*args,**kwargs)
	def __unicode__(self):
		return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
		return self.choice_text
