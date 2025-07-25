from django.urls import path
from .views import WheelSpecificationView, BogieChecksheetCreateView

urlpatterns = [
    path('forms/wheel-specifications', WheelSpecificationView.as_view(), name='wheel-specification'),
    path('forms/bogie-checksheet', BogieChecksheetCreateView.as_view(), name='bogie-checksheet'),
]
