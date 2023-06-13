from rest_framework.views import APIView
from rest_framework.response import Response
from app_in_proj.models import City, Person
import random
from django.db import connection
from django.db.models import Count
from rest_framework import serializers

class RandomDataAPIView(APIView):
    def post(self, request):
        cities = []
        cities.append(City(name='Moscow'))
        cities.append(City(name='New York'))
        cities.append(City(name='Pekin'))
        cities.append(City(name='Paris'))
        cities.append(City(name='England'))
        City.objects.bulk_create(cities)
        
        i=0
        persons = []
        for city in cities:
            for j in range(random.randint(1, 500)):
                i+=1
                persons.append(Person(name=f'Random Person {i}', age=random.randint(1, 100), city=city)) 
        Person.objects.bulk_create(persons)

        return Response('Random data created!')

    def delete(self, request):
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM app_in_proj_person;")
            cursor.execute("DELETE FROM app_in_proj_city;")
            
        return Response('Random data cleared!')
    
class CitySerializer(serializers.Serializer):
    name = serializers.CharField()
    person_count = serializers.IntegerField()

class CityPopulationAPIView(APIView):
    def get(self, request):
        cities = City.objects.annotate(person_count=Count('person')).order_by('-person_count')[:5]
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)
    
class TestAPIView(APIView):
    def get(self, request):
        cities = City.objects.order_by('name')
        data = [{'name': city.name} for city in cities]
        data.reverse()
        return Response(data)
    
# [{"name":"England","person_count":457},{"name":"Pekin","person_count":394},{"name":"Paris","person_count":341},
# {"name":"New York","person_count":250},{"name":"Moscow","person_count":131}]
    
class Hi(APIView):
    def get(self, request):
        return Response('Hi!')
