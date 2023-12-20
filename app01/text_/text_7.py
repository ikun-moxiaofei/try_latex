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
                "question_type_id": 107,
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
            {"Material_": r"阅读下面材料，根据其内容和所给段落开头语续写两段，使之构成一篇完整的短文。"},
            {"Material_": "Little Tom lived with his poor grandmother Donna in a "
                                   r"village. Every day, Tom sold potatoes grown by Donna in a market.One day, an old foreigner "
                                   r"aroused Tom's curiosity. He frequently visited Tom's stall(摊位) but didn't buy. The next day, "
                                   r"the man passed from one vendor(小贩) to the next, waving a bag around. But he didn't visit Tom's "
                                   r"stall that day. Out of curiosity, Tom asked a vendor nearby to temporarily look after his stall. "
                                   r"Then, he followed the foreigner.The man went back to his broken-down house near the market and "
                                   r"took several old medals from his bag. “Wow!” Tom said. “I won them in my own country,"
                                   r"” the man said proudly, then asking why Tom came here. Tom explained, “I'm wondering why you "
                                   r"didn't visit my stall today.” “Oh, I don't need potatoes. I need firewood, so I walked around the "
                                   r"market looking for someone who would buy these medals and give me money in exchange,” he lied.Tom "
                                   r"left and brought back many potatoes from his stall, saying, “If you don't have money, "
                                   r"you can't buy food. Keep my grandma's potatoes.” But the man insisted he had enough food. Tom "
                                   r"went back, upset; he could see the man was hungry and weak.The third day, the man reached the "
                                   r"market, selling medals again. He valued them, which were his honors. But after a disaster, "
                                   r"now he had to sell them to survive. He looked weaker. Tom packed some potatoes, walking towards "
                                   r"him again. From his conversations with vendors, Tom found him trying to sell medals for food! But "
                                   r"no one believed his medals were true.Disappointed, the man sat alone by the roadside. Tom "
                                   r"approached him, saying, “I saw it! Why didn't you let me help you?” Almost crying, he said, "
                                   r"“I'm sorry, but I was too embarrassed to ask for your help. Now could you give me your potatoes "
                                   r"in exchange for the medals?”\noindent注意：\textcolor{cyan1}{\textbf{1.}} 续写词数应为150左右；\textcolor{"
                                   r"cyan1}{\textbf{2.}} 请按如下格式作答。"}],
        "stems": [
            {
                "question_number": 1,
                "text": r"“Sure,” Tom said while nodding his head.\noindent\underline{\hspace{"
                        r"\textwidth}}\\\underline{\hspace{\textwidth}}\\\underline{\hspace{\textwidth}}\\\underline{"
                        r"\hspace{\textwidth}}"
                ,
                "score": 5,
                "answer": "11111",
                "explanation": "1111！启动！！！"
            },
            {
                "question_number": 2,
                "text": r"But Tom, the medals are valuable to the man. We should give them back,” added "
                        r"Donna.\underline{\hspace{\textwidth}}\\\underline{\hspace{\textwidth}}\\\underline{\hspace{"
                        r"\textwidth}}\\\underline{\hspace{\textwidth}}",
                "score": 5,
                "answer": "11111",
                "explanation": "1111！启动！！！"
            },
        ],
        "difficulty_level": "中等",
        "source": "2023南通一中高一阶段检测"
    }

    # 创建 Question 实例
    question_instance = Question(**question_data)

    # 保存到 MongoDB
    question_instance.save()

test_create_question()
