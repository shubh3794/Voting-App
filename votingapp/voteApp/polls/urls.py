from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [

	url('^$',views.IndexView.as_view(),name='index'),
	url('^create/$',views.create,name='create'),
	url('^(?P<pk>[0-9]+)$',views.DetailsView.as_view(),name='details'),
	url('^(?P<pk>[0-9]+)/results/$',views.ResultsView.as_view(),name='results'),
	url('^(?P<question_id>[0-9]+)/votes/$',views.vote,name='votes'),
	url('^profile/$',login_required(views.ProfileView.as_view()),name='profile'),

] 