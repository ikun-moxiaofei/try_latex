# 完形填空
from mongoengine import connect
from datetime import datetime

from app01.models import Question

# 连接到 MongoDB
connect("MongoDB")


def test_create_question():
    # 构造要创建的题目数据
    question_data = {
        "is_visible": True,
        "subject": {
            "subject_id": 1,
            "subject_name": "英语",
            "question_type": {
                "question_type_id": 110,
                "question_type_name": "完形填空"
            },
            "chapter": 1,
            "section": 2,
            "chapter_section_question_id": 3
        },
        "tags": [
            {"tag_id": 303, "tag_name": "111"},
            {"tag_id": 302, "tag_name": "编程提高"}
        ],
        "score": 5,
        "material": [
            {"Material_": r"阅读下面短文，从每题所给的A、B、C、D四个选项中选出可以填入空白处的最佳选项。"},
            {"Material_": r"My 9-year-old niece Lily is a bit fat and she doesn't do well at school. Because of "
                          r"these, she is often made fun of at home, thus developing some \underline{\hspace{"
                          r"1cm}1\hspace{1cm}}  in adults, who in turn usually don't put high\underline{\hspace{"
                          r"1cm}2\hspace{1cm}}  on her."}
        ],
        "stems": [
            {
                "question_number": 1,
                "options": [
                    {
                        "question_number": 1,
                        "specific_options": [
                            {
                                "option": "A",
                                "text": "distrust",
                                "is_correct": True,

                            },
                            {
                                "option": "B",
                                "text": "honor",
                                "is_correct": False,
                            },
                            {
                                 "option": "C",
                                "text": "tension",
                                "is_correct": False,
                            },
                            {
                                "option": "D",
                                "text": "loss",
                                "is_correct": False,
                            }

                        ],
                    }
                ],
                "score": 5,
                "answer": "11111",
                "explanation": "1111！启动！！！"
            },
            {
                "question_number": 2,
                "score": 5,
                "options": [
                    {
                        "question_number": 1,
                        "specific_options": [
                            {
                                "option": "A",
                                "text": "positions",
                                "is_correct": True,

                            },
                            {
                                "option": "B",
                                "text": "hopes",
                                "is_correct": False,
                            },
                            {
                                "option": "C",
                                "text": "response",
                                "is_correct": False,
                            },
                            {
                                "option": "D",
                                "text": "energy",
                                "is_correct": False,
                            }

                        ],
                    }
                ],
                "answer": "11111",
                "explanation": "1111！启动！！！"
            }
        ],
        "difficulty_level": "中等",
        "source": "2023南通海安实验中学高一下月考"
    }

    # 创建 Question 实例
    question_instance = Question(**question_data)

    # 保存到 MongoDB
    question_instance.save()

test_create_question()