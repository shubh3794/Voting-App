from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.core.urlresolvers import reverse
from django.views import generic
# Create your views here.
class IndexView(generic.ListView):
	queryset = Question.objects.order_by('-pub_date')[:5]
	context = 'latest_question_list'
	template = 'polls/index.html'

class DetailsView(generic.DetailView):
	template_name = 'polls/detail.html'
	model = Question

class ResultsView(generic.DetailView):
	template_name = 'polls/results.html'
	model = Question

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


