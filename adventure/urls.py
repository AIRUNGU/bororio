from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from adventure import views as a_views
urlpatterns = [
    path('', a_views.home,name='home'),
    path('practice/', a_views.practice,name='practice'),
    path('about/', a_views.about,name='about'),
    path(r'^details/(?P<safari_id>[0-9])+/', a_views.safarisdetail, name = "details"),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)