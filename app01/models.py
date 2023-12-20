# import datetime
#
# from mongoengine import Document, EmbeddedDocument, StringField, BooleanField, DateTimeField, IntField, ListField, \
#     EmbeddedDocumentField, SequenceField
#
#
# class Choice(EmbeddedDocument):
#     text = StringField(max_length=255, required=True)
#     true = BooleanField(default=False, required=True)
#
#     def __str__(self):
#         return self.text
#
# class Problem(Document):
#     id = SequenceField(primary_key=True)
#     text = StringField(max_length=255, required=True)
#     time = DateTimeField(default=datetime.datetime.now, required=True)
#     image = StringField(max_length=255, required=True)
#     publisher = IntField(default=0, required=True)
#     choice_ = ListField(EmbeddedDocumentField(Choice))
#
#     meta = {
#         'collection': 'problem',
#         'abstract': False,
#     }

from mongoengine import Document, EmbeddedDocument, fields, SequenceField

class Material(EmbeddedDocument):
    Material_ = fields.StringField(default='')
class Tag(EmbeddedDocument):
    tag_id = fields.IntField(required=True, default=0)  # 标签ID
    tag_name = fields.StringField(required=True, default='')  # 标签名称

class Image(EmbeddedDocument):
    has_image = fields.BooleanField(required=True, default=False)  # 题目是否提供图片
    image_id = fields.IntField(default=0)  # 图片ID
    file_name = fields.StringField(default='')  # 文件名
    file_path = fields.StringField(default='')  # 文件路径
    create_time = fields.DateTimeField()  # 创建时间
    creator_id = fields.IntField(default=0)  # 创建者ID

class SpecificOption(EmbeddedDocument):
    option = fields.StringField(required=True, default='')  # 选项
    text = fields.StringField(default='')  # 文本
    is_correct = fields.BooleanField(default=False)  # 是否正确选项
    images = fields.ListField(fields.EmbeddedDocumentField(Image), default=[])  # 图片列表

class Option(EmbeddedDocument):
    question_number = fields.IntField(default=0)  # 问题题号
    specific_options = fields.ListField(fields.EmbeddedDocumentField(SpecificOption), default=[])  # 具体选项列表

class QuestionStem(EmbeddedDocument):
    question_number = fields.IntField(default=0)  # 题号
    text = fields.StringField(default='')  # 文本
    score = fields.IntField(required=True, default=0)  # 分值
    images = fields.ListField(fields.EmbeddedDocumentField(Image), default=[])  # 图片列表
    options = fields.ListField(fields.EmbeddedDocumentField(Option), default=[])  # 选项列表
    answer = fields.StringField(required=True, default='')  # 答案
    explanation = fields.StringField(default='')  # 解析

class QuestionType(EmbeddedDocument):
    question_type_id = fields.IntField(required=True, default=0)  # 题型ID
    question_type_name = fields.StringField(required=True, default='')  # 题型名称

class Subject(EmbeddedDocument):
    subject_id = fields.IntField(required=True, default=0)  # 学科ID
    subject_name = fields.StringField(required=True, default='')  # 学科名称
    question_type = fields.EmbeddedDocumentField(QuestionType)  # 题型
    chapter = fields.IntField(default=0)  # 章
    section = fields.IntField(default=0)  # 节
    chapter_section_question_id = fields.IntField(default=0)  # 章节题目ID

class Question(Document):
    id = SequenceField(primary_key=True)  # 题库ID
    creator_id = fields.IntField(required=True, default=0)  # 创建者ID
    is_visible = fields.BooleanField(required=True, default=True)  # 是否可见
    subject = fields.EmbeddedDocumentField(Subject)  # 学科
    tags = fields.ListField(fields.EmbeddedDocumentField(Tag), default=[])  # 标签列表
    score = fields.IntField(required=True, default=0)  # 分值
    material = fields.ListField(fields.EmbeddedDocumentField(Material), default=[])  # 材料
    images = fields.EmbeddedDocumentField(Image)  # 图片
    stems = fields.ListField(fields.EmbeddedDocumentField(QuestionStem), default=[])  # 题干列表
    # options = fields.ListField(fields.EmbeddedDocumentField(Option), default=[])  # 选项列表
    # answer = fields.StringField(required=True, default='')  # 答案
    # explanation = fields.StringField(default='')  # 解析
    difficulty_level = fields.StringField(default='')  # 难度级别
    source = fields.StringField(default='')  # 题目来源
    question_status = fields.StringField(default='')  # 题目状态
