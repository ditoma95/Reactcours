from django.urls import path
from .views import ContactList,ContactDetail,ContactDelete,ContactUpdate

urlpatterns = [
    path('v1/contacts/', ContactList.as_view(), name='contacts'),
    path('v1/contact-show/<int:pk>', ContactDetail.as_view(), name='contact-show'),
    path('v1/contact-update/<int:pk>', ContactUpdate.as_view(), name='contact-update'),
    path('v1/contact-delete/<int:pk>', ContactDelete.as_view(), name='contact-delete'),
]