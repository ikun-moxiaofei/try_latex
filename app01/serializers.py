# from django.forms import models
# from rest_framework import serializers
# import datetime
# from django.db import models
# from app01.models import Problem, Choice
#
# class ChoiceSerializer(serializers.Serializer):
#     text = serializers.CharField(max_length=255, required=True)
#     true = serializers.BooleanField(required=True)  # 或者删除 default，或者设置为 default=None
#
# class ProblemSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     text = serializers.CharField(max_length=255, required=True)
#     time = serializers.DateTimeField(required=True)
#     image = serializers.CharField(max_length=255, required=True)
#     publisher = serializers.IntegerField(required=True)  # 或者删除 default，或者设置为 default=None
#     choice_ = ChoiceSerializer(many=True, required=False)
#
#     def create(self, validated_data):
#         choices_data = validated_data.pop('choice_', [])
#         problem = Problem.objects.create(**validated_data)
#
#         for choice_data in choices_data:
#             # 直接创建 Choice 实例
#             choice_instance = Choice(**choice_data)
#
#             # 将 Choice 实例添加到 Problem 的 choice_ 列表中
#             problem.choice_.append(choice_instance)
#
#         problem.save()
#
#         return problem

from rest_framework import serializers
# from mongoengine import fields, EmbeddedDocument, Document


class MaterialSerializer(serializers.Serializer):
    Material_ = serializers.CharField(default='')

class ShareInfoSerializer(serializers.Serializer):
    share_count = serializers.IntegerField(default=0)
    share_link = serializers.CharField(default='')
class TagSerializer(serializers.Serializer):
    tag_id = serializers.IntegerField(required=True)
    tag_name = serializers.CharField(required=True)

class ImageSerializer(serializers.Serializer):
    has_image = serializers.BooleanField(required=True)
    image_id = serializers.IntegerField(default=0)
    file_name = serializers.CharField(default='')
    file_path = serializers.CharField(default='')
    create_time = serializers.DateTimeField()
    creator_id = serializers.IntegerField(default=0)

class SpecificOptionSerializer(serializers.Serializer):
    option = serializers.CharField(required=True)
    text = serializers.CharField()
    is_correct = serializers.BooleanField(default=False)
    images = ImageSerializer(many=True, default=[])

class OptionSerializer(serializers.Serializer):
    question_number = serializers.IntegerField(default=0)
    specific_options = SpecificOptionSerializer(many=True, default=[])

class QuestionStemSerializer(serializers.Serializer):
    question_number = serializers.IntegerField(default=0)
    text = serializers.CharField(default='')
    score = serializers.IntegerField(required=True)
    images = ImageSerializer(many=True, default=[])
    options = OptionSerializer(many=True, default=[])
    answer = serializers.CharField(required=True)
    explanation = serializers.CharField(default='')

class QuestionTypeSerializer(serializers.Serializer):
    question_type_id = serializers.IntegerField(required=True)
    question_type_name = serializers.CharField(required=True)

class SubjectSerializer(serializers.Serializer):
    subject_id = serializers.IntegerField(required=True)
    subject_name = serializers.CharField(required=True)
    question_type = QuestionTypeSerializer()
    chapter = serializers.IntegerField(default=0)
    section = serializers.IntegerField(default=0)
    chapter_section_question_id = serializers.IntegerField(default=0)

class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    creator_id = serializers.IntegerField(required=True)
    is_visible = serializers.BooleanField(required=True)
    subject = SubjectSerializer()
    tags = TagSerializer(many=True, default=[])
    score = serializers.IntegerField(required=True)
    material = MaterialSerializer(many=True, default=[])
    images = ImageSerializer()
    stems = QuestionStemSerializer(many=True, default=[])
    # options = OptionSerializer(many=True, default=[])
    # answer = serializers.CharField(required=True)
    # explanation = serializers.CharField(default='')
    difficulty_level = serializers.CharField(default='')
    source = serializers.CharField(default='')
    question_status = serializers.CharField(default='')
    # share_info = ShareInfoSerializer()

