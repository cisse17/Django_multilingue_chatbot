
from django.urls import path
from .views import index
from django.conf.urls.i18n import set_language
from main.views import DetailBlog, connexion, inscription, deconnexion


urlpatterns = [
    path('', index, name='index'),
    path('article/<int:pk>/', DetailBlog.as_view(), name='detail-article'),
    path('inscription/', inscription, name='inscription'),
    path('connexion/', connexion, name='connexion'),
    path('deconnexion/', deconnexion, name='deconnexion'),
    
    # path('i18nsetlang/', set_language, name='set_language'),
   
    
]



