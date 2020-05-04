from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from anvorguesa import views

urlpatterns = [
    path('', views.api_root),
    path('ingrediente',views.ingrediente_list,name='ingrediente-list'),
    path('ingrediente/<pk>',views.ingrediente_detail,name='ingrediente-detail'),
    path('hamburguesa',views.hamburguesa_list,name='hamburguesa-list'),
    path('hamburguesa/<pk>',views.hamburguesa_detail,name='hamburguesa-detail'),
    path('hamburguesa/<h_pk>/ingrediente/<i_pk>',views.ingredient_to_hamburger,name='ingredient-to-hamburger'),

]
urlpatterns = format_suffix_patterns(urlpatterns)





