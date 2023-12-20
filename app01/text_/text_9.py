# 阅读理解
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
                "question_type_id": 109,
                "question_type_name": "阅读理解"
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
            {"Material_": r"阅读下面短文，从每题所给的A、B、C、D四个选项中选出最佳选项。"},
            {"Material_": r"这是一篇阅读文章We're looking for amazing English teachers to join us in Beijing, Shanghai, Shenzhen, "
                          r"Guangzhou, and many other cities across China. Teach adults, children or at our online "
                          r"schools. You will receive a great salary, competitive benefits and meet people from all "
                          r"over the world. Learn more about how our jobs can get you started on an "
                          r"once-in-a-lifetime(千载难逢的) ESL teaching career."}
        ],
        "stems": [
            {
                "question_number": 1,
                "text": r"This passage is written for the purpose of",
                "options": [
                    {
                        "question_number": 1,
                        "specific_options": [
                            {
                                "option": "A",
                                "text": "calling in some teachers for English First",
                                "is_correct": True,

                            },
                            {
                                "option": "B",
                                "text": "introducing an English teaching program",
                                "is_correct": False,
                            },
                            {
                                 "option": "C",
                                "text": "encouraging people to travel in America",
                                "is_correct": False,
                            },
                            {
                                "option": "D",
                                "text": "getting teachers to teach in European countries",
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
                "text": r"Where will the teachers to be hired work?",
                "score": 5,
                "options": [
                    {
                        "question_number": 1,
                        "specific_options": [
                            {
                                "option": "A",
                                "text": "calling in some teachers for English First",
                                "is_correct": True,

                            },
                            {
                                "option": "B",
                                "text": "introducing an English teaching program",
                                "is_correct": False,
                            },
                            {
                                "option": "C",
                                "text": "encouraging people to travel in America",
                                "is_correct": False,
                            },
                            {
                                "option": "D",
                                "text": "getting teachers to teach in European countries",
                                "is_correct": False,
                            }

                        ],
                    }
                ],
                "answer": "11111",
                "explanation": "1111！启动！！！"
            },
            {
                "question_number": 3,
                "text": r"{\textbf{1.}} \underline{\hspace{1cm}\hspace{1cm}}",
                "score": 5,
                "answer": "11111",
                "explanation": "1111！启动！！！"
            },

        ],
        "difficulty_level": "中等",
        "source": "2023南通海安实验中学高一下月考"
    }

    # 创建 Question 实例
    question_instance = Question(**question_data)

    # 保存到 MongoDB
    question_instance.save()

test_create_question()