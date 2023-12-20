# 作文
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
                "question_type_id": 105,
                "question_type_name": "写作"
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
            {"Material_":r"假如你是李华。你的新西兰笔友Jackie很喜欢中国古诗词，尤其喜欢李白的诗歌，想更多的了解李白和他的诗歌。请你给他写封邮件介绍相关情况。内容包括：{\textbf{1.}} "
                     r"李白和他的诗歌简介；{\textbf{2.}} 就如何欣赏诗歌提一两个建议。\noindent注意：{\textbf{1.}} 写作词数应为80左右；{\textbf{2.}} "
                     r"请按如下格式作答。"}
        ],
        "stems": [
            {
                "question_number": 1,
                "text": r"\noindentDear Jackie,\noindent\underline{\hspace{\textwidth}}\\\underline{\hspace{"
                        r"\textwidth}}\\\underline{\hspace{\textwidth}}\\\underline{\hspace{\textwidth}}\\\underline{"
                        r"\hspace{\textwidth}}\\\underline{\hspace{\textwidth}}\begin{flushright}Yours,Li Hua\end{"
                        r"flushright}",
                "score": 5,
                "answer": "11111",
                "explanation": "1111！启动！！！"
            },
        ],
        "difficulty_level": "中等",
        "source": "2023南通如皋市高一下期末"
    }

    # 创建 Question 实例
    question_instance = Question(**question_data)

    # 保存到 MongoDB
    question_instance.save()

test_create_question()