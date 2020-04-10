from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('about/', views.about, name ='about'),
    path('countries/', views.countries_index, name='index'),
    path('countries/new/', views.new_country, name='new_country'),
    path('countries/<int:country_id>/', views.countries_detail, name='detail'),
    path('countries/<int:countries_id>/edit', views.countries_update, name='countries_update'),
    path('countries/<int:countries_id>/delete', views.countries_delete, name='countries_delete'),
    path('countries/<int:country_id>/add_city', views.add_city, name='add_city'),
    path('countries/<int:country_id>/assoc_cruise/<int:cruise_id>/', views.assoc_cruise, name='assoc_cruise'),
    path('cruises/', views.CruiseList.as_view(), name='cruises_index'),
    path('cruises/<int:pk>/', views.CruiseDetail.as_view(), name='cruises_detail'),
    path('cruises/create/', views.CruiseCreate.as_view(), name='cruises_create'),
    path('cruises/<int:pk>/update/', views.CruiseUpdate.as_view(), name='cruises_update'),
    path('cruises/<int:pk>/delete/', views.CruiseDelete.as_view(), name='cruises_delete')
]