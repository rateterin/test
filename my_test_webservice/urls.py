from my_test_webservice import views
from django.urls import path, re_path


urlpatterns = [
    path('link/', views.link_minimizer),
    re_path(r'link/[a-zA-Z0-9]{12}$', views.link_deminimizer),
]
