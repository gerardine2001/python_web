from django.urls  import path,include
from events import views

urlpatterns = [
    path('',views.index,name='index'),
]
