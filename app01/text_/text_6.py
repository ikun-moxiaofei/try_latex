# 单句语法填空
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
                "question_type_id": 106,
                "question_type_name": "单句语法填空"
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
        "stems": [
            {
                "question_number": 1,
                "text": r"The teacher said in class yesterday that future 3D food printers could make \underline{\makebox[2cm]{}} (process) food healthier. ",
                "score": 1,
                "answer": "11111",
                "explanation": "1111！启动！！！"
            },
            {
                "question_number": 2,
                "text": r"As is reported, when the environmentally friendly shoes wear out, customers can return them at no cost to a company that uses the \underline{\makebox[2cm]{}} (recycle) materials to make other products. ",
                "score": 1,
                "answer": "22222",
                "explanation": "2222！启动！！！"
            },
            {
                "question_number": 3,
                "text": r"There's absolutely no regulation of cigarettes to make sure that they don't include \underline{\makebox[2cm]{}} (poison) substance.",
                "score": 1,
                "answer": "33333",
                "explanation": "3333！启动！！！"
            },
            {
                "question_number": 4,
                "text": r"Sports stars like those in CBA contribute to the national \underline{\makebox[2cm]{}} (economic) by benefiting the sports industry as well as the advertising industry.",
                "score": 1,
                "answer": "44444",
                "explanation": "4444！启动！！！"
            },
            {
                "question_number": 5,
                "text": r"Huawei company has its base in Shenzhen, with its \underline{\makebox[2cm]{}} (branch) all over the world",
                "score": 1,
                "answer": "55555",
                "explanation": "5555！启动！！！"

            }
        ],
        "difficulty_level": "中等",
    }

    # 创建 Question 实例
    question_instance = Question(**question_data)

    # 保存到 MongoDB
    question_instance.save()

test_create_question()