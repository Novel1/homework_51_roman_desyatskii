from django.urls import path

from webapp import views

urlpatterns = [
    path('', views.index_view),
    path('inform_cat', views.cat_name),
    path('game', views.cat_game),
    path('cat_info_view', views.name_view),
]