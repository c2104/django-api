from django.urls import include, path
from api import views

urlpatterns = [
    path('api/v1/', views.AiAnalysisLogList.as_view()),
    path('', include('web.urls'))
]