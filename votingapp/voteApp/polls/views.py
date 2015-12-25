from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.
class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]

class DetailsView(generic.DetailView):
	model = Question
	template_name = 'polls/details.html'


class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'
	
@login_required
def vote(request,question_id):
	ques = get_object_or_404(Question,pk=question_id)
	print request.user.is_authenticated(),"trytrytrytyryrtyrytrytyrytyrytyrytr"
	try:
		selected_choice = ques.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request,'polls/details.html',{
			'question':ques,
			'error_message':'No choice selected',
			})
	selected_choice.votes += 1
	selected_choice.save()
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


