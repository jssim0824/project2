from django.contrib import admin
from django.urls import path
import coin.views
from django.conf.urls import handler500

handler500 = 'coin.views.error'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', coin.views.home, name='home' ),
    path('bitcoin/', coin.views.bitcoin, name='bitcoin' ),
    path('how/', coin.views.how, name='how' )
]

