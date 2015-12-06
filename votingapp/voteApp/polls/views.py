from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)

def detail(request,question_id):
	question = get_object_or_404(Question,pk=question_id)
	return render(request, 'polls/details.html', {'question': question})

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

def results(request,question_id):
	question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
