# 翻译
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
                "question_type_id": 104,
                "question_type_name": "翻译"
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
                "text": r"许多科学家改变了我们的生活，改变了我们产生影响世界。\\Many scientists have changed our lives and \underline{\hspace{2cm}} \underline{\hspace{2cm}} \underline{\hspace{2cm}}       the world.",
                "score": 1,
                "answer": "11111",
                "explanation": "1111！启动！！！"
            },
            {
                "question_number": 2,
                "text": r"约翰·纳什，一位数学家，他对做出巨大的贡献博弈论。\\John Nash, a mathematician who \underline{\hspace{2cm}} \underline{\hspace{2cm}} \underline{\hspace{2cm}} \underline{\hspace{2cm}}  game theory.",
                "score": 1,
                "answer": "22222",
                "explanation": "2222！启动！！！"
            },
            {
                "question_number": 3,
                "text": r"面对这样的机遇和挑战，我们必须加快步伐加速调整\\Facing such opportunities and challenges, one must \underline{\hspace{2cm}}",
                "score": 1,
                "answer": "33333",
                "explanation": "3333！启动！！！"
            },
            {
                "question_number": 4,
                "text": r"这么多年过去了，我们终于有了回报还清我们所有的债务。\\After all these years, we've at last \underline{\hspace{2cm}} \underline{\hspace{2cm}}\underline{\hspace{2cm}} \underline{\hspace{2cm}} \underline{\hspace{1cm}}.",
                "score": 1,
                "answer": "44444",
                "explanation": "4444！启动！！！"
            },
            {
                "question_number": 5,
                "text": r"菲尔不得不借鉴凭借完成比赛的内在力量。\\Phil \underline{\hspace{2cm}} \underline{\hspace{2cm}} \underline{\hspace{2cm}} \underline{\hspace{2cm}}  inner strength to complete race.   ",
                "score": 1,
                "answer": "55555",
                "explanation": "5555！启动！！！"

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