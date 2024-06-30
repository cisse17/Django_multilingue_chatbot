
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # file static for deployement 

from django.conf.urls.i18n import i18n_patterns


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('', include('main.urls')),
    path('', include('chatbot.urls')),

    prefix_default_language=False # l' URL pour la langue par défaut ne seront pas préfixée avec le code de langue
)

urlpatterns += staticfiles_urlpatterns()




# test
"""from django.views.i18n import set_language
urlpatterns = [
    path('set_language/', set_language, name='set_language'),
    path('rosetta/', include('rosetta.urls')),
    #path('', index, name='index'),
    
]

urlpatterns += i18n_patterns(
    path('', include('main.urls')),
    
)"""