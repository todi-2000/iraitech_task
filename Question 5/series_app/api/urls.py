from django.urls import path
from .views import MathFunctionView

urlpatterns = [
    path('calculate', MathFunctionView.as_view()),
]