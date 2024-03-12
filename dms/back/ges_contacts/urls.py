from django.urls import path
import ges_contacts.views as views
urlpatterns = [
    path('', views.index, name='index'),
    path('search/<str:q>', views.search, name='search'),
    path('contact/<int:pk>/show', views.contact_show, name='contact_show'),
    path('contact/create/', views.contact_create, name='contact_create'),
    path('contact/<int:pk>/update/', views.contact_update, name='contact_update'),
    path('contact/<int:pk>/delete/', views.contact_delete, name='contact_delete'),
]