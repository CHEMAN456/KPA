from django.urls import path
from .views import BogieChecksheetView,WheelSpecificationListView,LoginAPIView

urlpatterns = [
    path('forms/bogie-checksheet/', BogieChecksheetView.as_view() , name='bogie-checksheet'),
    path('forms/wheel-specifications/', WheelSpecificationListView.as_view() , name='wheel-specifications'),
    path('users/login/', LoginAPIView.as_view() , name='login')
]
