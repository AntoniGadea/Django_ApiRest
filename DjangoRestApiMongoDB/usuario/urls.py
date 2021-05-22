from django.conf.urls import url 
from usuario import views 

urlpatterns = [ 
    url(r'^api/usuario$', views.usuario_list),
    #url(r'^api/usuario/(?P<pk>[0-9]+)$', views.usuario_detail),
]