from django.shortcuts import render
from django.http.response import JsonResponse

from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer

from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

import json


@csrf_exempt
@api_view(['GET', 'POST'])
def companies(request):
    if request.method == 'GET':
        try:
            companies = Company.objects.all()
            serializer = CompanySerializer(companies, many=True)
            return JsonResponse(serializer.data, safe=False)
        except:
            return JsonResponse({"message": "no data"}, safe=False)
    
    elif request.method == 'POST':
        serializer = CompanySerializer(data = json.loads(request.body))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(json.loads(request.body), status=status.HTTP_400_BAD_REQUEST)
    

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def company_detailed(request, id):
    try:
        company = Company.objects.get(id = id)
    except:
        return JsonResponse({"message": "no data"}, safe=False)

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        serializer = CompanySerializer(instance=company, data=json.loads(request.body))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"error": "error"})

    elif request.method == 'DELETE':
        company.delete()
        return Response({'deleted': 'true'})

def company_vacancy(request, id):
    try:
        company = Company.objects.get(id = id)
        vacancies = company.vacancy_set.all()
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)
    except:
        return JsonResponse({"message": "no data"}, safe=False)






# vacancies:
def vacancies(request):
    try:
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)
    except:
        return JsonResponse({"message": "no data"}, safe=False)

def vacancy_detailed(request, id):
    try:
        vacancies = Vacancy.objects.get(id = id)
        serializer = VacancySerializer(vacancies)
        return JsonResponse(serializer.data, safe=False)
    except:
        return JsonResponse({"message": "no data"}, safe=False)


def vacancy_top(request):
    try:
        vacancies = Vacancy.objects.order_by('-salary')[:10]
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)
    except:
        return JsonResponse({"message": "no data"}, safe=False)
        

class VacancyViews(APIView):
    def get(self, request):
        try:
            vacancies = Vacancy.objects.all()
            serializer = VacancySerializer(vacancies, many=True)
            return JsonResponse(serializer.data, safe=False)
        except:
            return JsonResponse({"message": "no data"}, safe=False)

    def post(self, request):
        serializer = VacancySerializer(data=json.loads(request.body))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'Error': serializer.errors})


class VacancyDetailedView(APIView):
    def get_object(self, id):
        try:
            return Vacancy.objects.get(id = id)
        except:
            return Response({"error": "error"})
    
    def get(self, request, id):
        vacancy = self.get_object(id)
        serializer = VacancySerializer(vacancy)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request, id):
        vacancy = self.get_object(id)
        serializer = VacancySerializer(instance=vacancy, data=json.loads(request.body))
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "updated succesfully"})
        return Response({"error": serializer.errors})

    def delete(self, request, id):
        vacancy = self.get_object(id)
        vacancy.delete()

        return Response({"message": "deleted succesfully"})