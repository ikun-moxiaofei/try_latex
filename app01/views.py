from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app01.models import Problem
from app01.serializers import ProblemSerializer

from app01.tests import markdown_to_latex

class ProblemList(APIView):
    def get(self, request, format=None):
        # 获取所有问题的查询集

        problems = Problem.objects.all()
        # print(problems[1].text)
        # 使用问题模型的序列化器将查询集序列化为JSON格式
        serializer = ProblemSerializer(problems, many=True)

        for data in serializer.data:
            data['text'] = markdown_to_latex(data['text'])

        # 返回序列化后的数据作为API响应
        return Response(serializer.data)

    def post(self, request):
        # 使用问题模型的序列化器处理传入的数据
        serializer = ProblemSerializer(data=request.data)

        # 检查数据是否有效，如果有效则保存并返回201 Created状态，否则返回400 Bad Request状态
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProblemDetail(APIView):
    def get_object(self, pk):
        # 根据主键（pk）获取单个问题对象，如果对象不存在则抛出Http404异常
        try:
            return Problem.objects.get(pk=pk)
        except Problem:
            raise Http404

    def get(self, request, pk):
        # 根据主键获取单个问题对象
        problem = self.get_object(pk)
        problem.text = markdown_to_latex(problem.text)

        # 使用问题模型的序列化器将问题对象序列化为JSON格式
        serializer = ProblemSerializer(problem)

         # 返回序列化后的数据作为API响应
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        # 根据主键获取单个问题对象
        problem = self.get_object(pk)

        # 使用问题模型的序列化器处理传入的数据
        serializer = ProblemSerializer(problem, data=request.data)

        # 检查数据是否有效，如果有效则保存并返回更新后的数据，否则返回400 Bad Request状态
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        # 根据主键获取单个问题对象并删除
        problem = self.get_object(pk)
        problem.delete()

        # 返回204 No Content状态，表示删除成功且无需返回内容
        return Response(status=status.HTTP_204_NO_CONTENT)
