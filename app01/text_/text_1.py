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
                "question_type_id": 101,
                "question_type_name": "测试题"
            },
            "chapter": 1,
            "section": 2,
            "chapter_section_question_id": 3
        },
        "tags": [
            {"tag_id": 301, "tag_name": "编程基础"},
            {"tag_id": 302, "tag_name": "编程提高"}
        ],
        "score": 5,
        "material": [
            {
                "Material_": "\\textbf{这是加粗的文字} \\textit{这是斜体的文字}，下面是一个公式\( \lim_{{x \\to 0}} \\frac{{\sin(x)}}{x} \\ )"
            }
        ],
        "images": {
            "has_image": True,+
            "image_id": 1,
            "file_name": "image1.jpg",
            "file_path": "/images/user1/",
            "create_time": datetime.utcnow(),
            "creator_id": 1
        },
        "stems": [
            {
                "question_number": 1,
                "text": "这是问题1",
                "score": 5,
                "images": [
                    {
                        "has_image": True,
                        "image_id": 1,
                        "file_name": "image1.jpg",
                        "file_path": "/images/user1/",
                        "create_time": datetime.utcnow(),
                        "creator_id": 1
                    }
                ],
                "options": [
                    {
                        "question_number": 1,
                        "specific_options": [
                            {
                                "option": "A",
                                "text": "C++",
                                "is_correct": True,
                                "images": [
                                    {
                                        "has_image": True,
                                        "image_id": 1,
                                        "file_name": "image1.jpg",
                                        "file_path": "/images/user1/",
                                        "create_time": datetime.utcnow(),
                                        "creator_id": 1
                                    }
                                ]
                            },
                            {
                                "option": "B",
                                "text": "B++",
                                "is_correct": False,
                            }
                        ],
                    }
                ],
                "answer": "A",
                "explanation": "C++！启动！！！"
            }
        ],
        "difficulty_level": "中等",
        "source": "如果没有来源，则可以为空"
    }

    # 创建 Question 实例
    question_instance = Question(**question_data)

    # 保存到 MongoDB
    question_instance.save()

test_create_question()