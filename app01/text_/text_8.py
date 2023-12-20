# 读后续写
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
                "question_type_id": 108,
                "question_type_name": "读后续写"
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
            {"Material_": r"阅读下面短文，从短文后的选项中选出可以填入空白处的最佳选项。选项中有两项为多余选项。"},
            {"Material_": r"Filling Ip on InformationPeople now have access to more information than ever before "
                         r"thanks to the Internet. While there are clearly benefits to it, there are also unexpected "
                         r"effects. One in particular is information overload, commonly referred to as “infobesity”. "
                         r"\TimuQixuanwuTihao{1}Infobesity can be caused by many factors. For example, information "
                         r"from various sources can lead to infobesity. A search on a particular topic can bring "
                         r"hundreds of websites with a lot of information, and you may feel very upset due to the "
                         r"amount of information accessible. \TimuQixuanwuTihao{2} Smart devices provide a person "
                         r"with information on the go, merely to stay updated. This often gets misused. As a result, "
                         r"people will load themselves with too much information. \TimuQixuanwuTihao{3} They indicate "
                         r"that an over-exposure to information can cause people's behavioural changes. It makes a "
                         r"person tired mentally and physically, directly leading to stress where the person is too "
                         r"tired to carry on any activity. In addition, infobesity is the enemy of good decisions. "
                         r"People can probably be at a loss in the face of many possibilities. \TimuQixuanwuTihao{"
                         r"4}So, what can be done to reduce the effects of this condition? While there is no easy "
                         r"answer, one obvious step is to limit our sources of information. Sort the information we "
                         r"receive as important and unimportant, and try to only focus on things that really matter "
                         r"to us and on just one thing at a time. \TimuQixuanwuTihao{5} And who knows?Too much of "
                         r"anything is bad. This applies not only to the food one consumes, but also to the "
                         r"information that one receives. By taking a certain action, infobesity can be controlled at "
                         r"the first stage itself."},
            {"Material_": r"{\textbf{A.}} Experts have shown some major effects of infobesity.{\textbf{B.}} This "
                          r"would give us more room to absorb information from sources.{\textbf{C.}} Being constantly "
                          r"connected to technology can also result in infobesity.{\textbf{D.}} It involves a "
                          r"situation where there's too much information on a given topic.{\textbf{E.}} We are sure "
                          r"about how certain types of information help us get where we want to go.{\textbf{F.}} "
                          r"Since technology has got us into this mess, perhaps it will also present solutions in "
                          r"future.{\textbf{G.}} One example is that, for online shoppers, a purchase can be "
                          r"difficult with so many choices accessible."}
        ],
        "stems": [
            {
                "question_number": 1,
                "text": r"{\textbf{1.}} \underline{\hspace{1cm}\hspace{1cm}}",
                "score": 5,
                "answer": "11111",
                "explanation": "1111！启动！！！"
            },
            {
                "question_number": 2,
                "text": r"{\textbf{1.}} \underline{\hspace{1cm}\hspace{1cm}}",
                "score": 5,
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
            {
                "question_number": 4,
                "text": r"{\textbf{1.}} \underline{\hspace{1cm}\hspace{1cm}}",
                "score": 5,
                "answer": "11111",
                "explanation": "1111！启动！！！"
            },
            {
                "question_number": 5,
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