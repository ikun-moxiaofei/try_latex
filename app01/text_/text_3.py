# 选词填空
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
                "question_type_id": 103,
                "question_type_name": "选词填空"
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
            {"Material_": r"get rid of; protest against; tend to; result in; draw your attention to; take part in; do harm to; give rise to; in defence of; make a profit"}
        ],
        "stems": [
            {
                "question_number": 1,
                "text": r"Three-quarters of the country's people \underline{\hspace{2cm}} a march against racial discrimination in the USA last year.",
                "score": 1,
                "answer": "11111",
                "explanation": "1111！启动！！！"
            },
            {
                "question_number": 2,
                "text": r"Do you think that work without rest \underline{\hspace{2cm}} your health in the future?}",
                "score": 1,
                "answer": "22222",
                "explanation": "2222！启动！！！"
            },
            {
                "question_number": 3,
                "text": r"They fought to the last ditch \underline{\hspace{2cm}} freedom and of the interests of the people.",
                "score": 1,
                "answer": "33333",
                "explanation": "3333！启动！！！"
            },
            {
                "question_number": 4,
                "text": r"Go outdoors and play team games with your friends as physical exercise is an effective way \underline{\hspace{2cm}} your depression.",
                "score": 1,
                "answer": "44444",
                "explanation": "4444！启动！！！"
            },
            {
                "question_number": 5,
                "text": r"I am writing this letter \underline{\hspace{2cm}} the matter in the hope that the present situation will be much improved.",
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