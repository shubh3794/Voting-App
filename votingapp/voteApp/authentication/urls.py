from django.conf.urls import url
from . import views
urlpatterns = [

	
	url('^login/$',views.user_login,name='login'),
	url('^logout/$',views.user_logout,name='logout'),
	url('^signup/$',views.user_signup,name='signup'),

] 