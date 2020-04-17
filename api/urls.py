from django.urls import path
from api import views
from api.views import VacancyViews, VacancyDetailedView

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('companies/', views.companies),
    path('companies/<int:id>/', views.company_detailed),
    path('companies/<int:id>/vacancies/', views.company_vacancy),
    path('vacancies/', VacancyViews.as_view()),
    path('vacancies/<int:id>/', VacancyDetailedView.as_view()),
    path('vacancies/top_ten/', views.vacancy_top)
]