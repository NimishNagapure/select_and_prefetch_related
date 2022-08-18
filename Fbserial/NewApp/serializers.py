from rest_framework import serializers
from NewApp.models import Student

class  StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','score']