from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
# Create your views here.
class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]

class DetailsView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'
	
@login_required
def vote(request,question_id):
	ques = get_object_or_404(Question,pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except:
		return render(request,polls/details.html,{
			'question':ques,
			'error':'No choice selected',
			})
	return HttpResponseRedirect(reverse('polls:results', args=(ques.id,)))


