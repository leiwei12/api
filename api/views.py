from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from api.utils.serializer import course, degree
from api import models
from rest_framework.response import Response
from api.utils.response import BaseResponse
from django.http import JsonResponse


class DegreeCourse(APIView):
    """
        学位课
    """

    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            # a.查看所有学位课并打印学位课名称以及授课老师
            queryset = models.DegreeCourse.objects.all()
            # b.查看所有学位课并打印学位课名称以及学位课的奖学金
            # 见序列化类
            ser = degree.DegreeCourseSerializer(instance=queryset, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 0
            ret.errors = "数据获取失败"
        return Response(ret.dict)

    def post(self, request, *args, **kwargs):
        return HttpResponse("ok")


class DegreeCourseDetail(APIView):
    """
        学位课详情
    """

    def get(self, request, pk, *args, **kwargs):
        ret = BaseResponse()
        try:
            # d 查看id=1的学位课对应的所有模块名称
            queryset = models.DegreeCourse.objects.filter(id=pk)
            ser = degree.DegreeCourseSerializer(instance=queryset, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 0
            ret.errors = "数据获取失败"
        return Response(ret.dict)

    def put(self, request, pk, *args, **kwargs):
        return HttpResponse("ok")

    def delete(self, request, pk, *args, **kwargs):
        return HttpResponse("ok")


class Course(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("ok")

    def post(self, request, *args, **kwargs):
        return HttpResponse("ok")


class CourseDetail(APIView):
    def get(self, request, pk, *args, **kwargs):
        ret = BaseResponse()

        try:
            queryset = models.Course.objects.filter(id=pk, degree_course__isnull=True)
            ser = course.CourseSerializer(instance=queryset, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 0
            ret.errors = "数据获取失败"
        return Response(ret.dict)

    def put(self, request, *args, **kwargs):
        return HttpResponse("ok")

    def delete(self, request, *args, **kwargs):
        return HttpResponse("ok")
