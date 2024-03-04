from django.urls import path
from .views import StaffApiView, PositionApiView

urlpatterns = [
    path('staffs', StaffApiView.as_view(), name='staffs'),
    path('positions', PositionApiView.as_view(), name='positions'),
]