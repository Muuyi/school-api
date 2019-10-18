from rest_framework import serializers
from . models import School

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ('name','logo','address','phone','created_date')