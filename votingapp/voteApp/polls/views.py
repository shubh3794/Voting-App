from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice,alreadyVoted
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from authentication.models import Account
import datetime
# Create your views here.
class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	voted = None
	
	def get_queryset(self):
		return Question.objects.order_by('-pub_date')

	def get_context_data(self, *args, **kwargs):
		
		context = super(IndexView,self).get_context_data(*args, **kwargs)
		if self.request.user.is_authenticated():
			self.voted = alreadyVoted.objects.filter(user=self.request.user).values_list('ques',flat=True).order_by('id')
			print self.voted
			context['voted'] = self.voted
		return context

class DetailsView(generic.DetailView):
	model = Question
	template_name = 'polls/details.html'
	def get_context_data(self, **kwargs):
		context = super(DetailsView, self).get_context_data(**kwargs)
		if self.request.user.is_authenticated():
			a = self.request.get_full_path()
			ques = int(a[1:])
			ques = Question.objects.get(pk=ques)
			context['voted'] = alreadyVoted.objects.filter(user=self.request.user,ques=ques).values_list('ques',flat=True)
			context['voted'] = context['voted'][0]
		return context

class ProfileView(generic.ListView):
	context_object_name = "Profile"
	template_name = "polls/Profile.html"
	def get_queryset(self):
		return Account.objects.filter(email=self.request.user.email,username=self.request.user.username)
	def get_context_data(self,**kwargs):
		context = super(ProfileView, self).get_context_data(**kwargs)
		ques = alreadyVoted.objects.filter(user=self.request.user).values_list('ques',flat=True)
		self.votedQues=[]
		for i in ques:
			self.votedQues.append(Question.objects.get(pk=i))

		self.created = Question.objects.filter(createdby=self.request.user)
		context['created'] = self.created
		context['voted'] = self.votedQues
		return context





class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'
	
@login_required
def vote(request,question_id):
	ques = get_object_or_404(Question,pk=question_id)
	try:
		selected_choice = ques.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request,'polls/details.html',{
			'question':ques,
			'error_message':'No choice selected',
			})
	selected_choice.votes += 1
	selected_choice.save()
	savedVote = alreadyVoted.objects.create(user = request.user, ques=Question.objects.get(pk=question_id))
	savedVote.save()
	return HttpResponseRedirect(reverse('polls:results', args=(ques.id,)))

@login_required
def create(request):
	ques, created = Question.objects.get_or_create(createdby=request.user,question_text=request.POST['newques'], pub_date=datetime.datetime.now())
	if created:
		flag = False
		ques.save()
		a = request.POST.getlist('choice')
		for i in range(len(a)):
			Choice.objects.create(choice_text=a[i],question=ques) 
		print ques, "\n", ques.choice_set
		return HttpResponseRedirect(reverse('polls:index'))
	else:
		print created
		return render(request,'polls/index.html',{
			'error_message':'Try again later',
			})


