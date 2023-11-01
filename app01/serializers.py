from django.forms import models
from rest_framework import serializers
import datetime
from django.db import models
from app01.models import Problem, Choice

class ChoiceSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=255, required=True)
    true = serializers.BooleanField(required=True)  # 或者删除 default，或者设置为 default=None

class ProblemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(max_length=255, required=True)
    time = serializers.DateTimeField(required=True)
    image = serializers.CharField(max_length=255, required=True)
    publisher = serializers.IntegerField(required=True)  # 或者删除 default，或者设置为 default=None
    choice_ = ChoiceSerializer(many=True, required=False)

    def create(self, validated_data):
        choices_data = validated_data.pop('choice_', [])
        problem = Problem.objects.create(**validated_data)

        for choice_data in choices_data:
            # 直接创建 Choice 实例
            choice_instance = Choice(**choice_data)

            # 将 Choice 实例添加到 Problem 的 choice_ 列表中
            problem.choice_.append(choice_instance)

        problem.save()

        return problem
