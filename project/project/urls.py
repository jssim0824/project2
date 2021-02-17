from django.contrib import admin
from django.urls import path
import coin.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', coin.views.home, name='home' ),
    path('bitcoin/', coin.views.bitcoin, name='bitcoin' ),
    path('how/', coin.views.how, name='how' )
]

