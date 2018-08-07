from rest_framework import serializers
from api import models


class A(serializers.Serializer):
    value = serializers.IntegerField(source='value')


class DegreeCourseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    teachers = serializers.CharField(source="teachers.all")
    # scholarship = serializers.CharField(source='scholarship_set.all')
    scholarship = serializers.SerializerMethodField()
    model = serializers.SerializerMethodField()

    def get_scholarship(self, obj):
        li = []
        for item in obj.scholarship_set.all():
            li.append(item.value)
        return li

    def get_model(self,obj):
        li = []
        for item in obj.course_set.all():
            li.append(item.name)
        return li