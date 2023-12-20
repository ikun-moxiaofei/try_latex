# 词性转换
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
                "question_type_id": 102,
                "question_type_name": "词性转换"
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
        "images": {
            "has_image": False,
        },
        "stems": [
            {
                "question_number": 1,
                # 这个地方用\\返回时会返回\\\\
                "text": r"long \\hspace{2pt} \\textit{adj.} $\\rightarrow$ \\underline{\hspace{2cm}} \\hspace{2pt} \\textit{n.} $\\rightarrow$ \\underline{\\hspace{2cm}} \\hspace{2pt} \\textit{vt.}",
                "score": 1,
                "answer": "11111",
                "explanation": "1111！启动！！！"
            },
            {
                "question_number": 2,
                "text": r" broad \hspace{2pt} \textit{adj.} $\rightarrow$ \underline{\hspace{2cm}} \hspace{2pt} \textit{vt.}",
                "score": 1,
                "answer": "22222",
                "explanation": "2222！启动！！！"
            },
            {
                "question_number": 3,
                "text": r"illustrate \hspace{2pt} \textit{vt.} $\rightarrow$ \underline{\hspace{2cm}} \hspace{2pt} \textit{n.} $\rightarrow$ \underline{\hspace{2cm}} \hspace{2pt} \textit{adj.}",
                "score": 1,
                "answer": "33333",
                "explanation": "3333！启动！！！"
            },
            {
                "question_number": 4,
                "text": r"agriculture \hspace{2pt} \textit{n.} $\rightarrow$ \underline{\hspace{2cm}} \hspace{2pt} \textit{adj.} $\rightarrow$ \underline{\hspace{2cm}} \hspace{2pt} \textit{adv.}",
                "score": 1,
                "answer": "44444",
                "explanation": "4444！启动！！！"
            },
            {
                "question_number": 5,
                "text": r"refer \hspace{2pt} \textit{vi.} $\rightarrow$ \underline{\hspace{2cm}} \hspace{2pt} \textit{n.}",
                "score": 1,
                "answer": "55555",
                "explanation": "5555！启动！！！"

            }
        ],
        # "options": [
        #     {
        #         "question_number": 1,
        #         "specific_options": [
        #             {
        #                 "option": "A",
        #                 "text": "C++",
        #                 "is_correct": True,
        #                 "images": [
        #                     {
        #                         "has_image": True,
        #                         "image_id": 1,
        #                         "file_name": "image1.jpg",
        #                         "file_path": "/images/user1/",
        #                         "create_time": datetime.utcnow(),
        #                         "creator_id": 1
        #                     }
        #                 ]
        #             },
        #             {
        #                 "option": "B",
        #                 "text": "B++",
        #                 "is_correct": False,
        #             }
        #         ]
        #     }
        # ],
        "difficulty_level": "中等",
        "source": "如果没有来源，则可以为空"
    }

    # 创建 Question 实例
    question_instance = Question(**question_data)

    # 保存到 MongoDB
    question_instance.save()

test_create_question()