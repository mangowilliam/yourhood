from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('^$', views.hood,name='hood'),
    url(r'register',views.register,name= 'signup'),
    url(r'^business',views.add_business, name = "business"),
    url(r'^nhood',views.add_hood, name = "nhood"),
    url(r'profile',views.profile,name= 'profile'),
    url(r'details',views.add_profile,name= 'details'),
    url(r'post', views.add_post, name = 'post'),
    url(r'update', views.hood_update, name = 'update'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)