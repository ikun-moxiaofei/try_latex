from mongoengine import connect
from app01.models import Problem, Choice

import mistune  # 一个用于将Markdown转换为HTML的库
def markdown_to_latex(markup):
    # 使用mistune将Markdown转换为HTML
    html_content = mistune.markdown(markup)

    # 将HTML转换为LaTeX（这只是一个简化的示例）
    latex_content = html_content.replace('<strong>', '\\textbf{').replace('</strong>', '}') \
        .replace('<em>', '\\textit{').replace('</em>', '}') \
        .replace('<p>', '').replace('</p>', '').replace(r'\\', r'\\\\')

    # 将双反斜杠替换为单个反斜杠
    latex_content = latex_content.replace('\\\\', '\\')

    print(latex_content)

    return latex_content
