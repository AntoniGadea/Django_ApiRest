from django.conf.urls import url
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from usuario import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from allauth.account.views import confirm_email

urlpatterns = [ 
    
    url(r'^api/usuario/search$', views.UsuarioListView.as_view()),
    url(r'^api/usuarios$', views.usuarios),
    url(r'^api/usuarios/list$', views.usuarios_list),
    url(r'^api/usuario/update/(?P<email>.*)$', views.update),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
]