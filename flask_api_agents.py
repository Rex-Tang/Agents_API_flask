# from flask import Flask, request, jsonify
# from your_script import create_crew_and_kickoff  # 假设你的脚本保存在your_script.py中
from crewai_agents import AIAssistant
from flask import Flask, request, render_template_string
model = 'glm4:9b-chat-q2_K'

# @app.route('/ask', methods=['POST'])
# def ask_question():
#     data = request.json
#     question = data.get('question')
#     task1_user, task2_user = str(question).split('|').split('｜')
#     ai_assistant = AIAssistant(model_name=model_name, task1_user,task2_user)
#     result = ai_assistant.kickoff()
    
#     # 根据问题创建任务和代理，这里需要根据实际情况调整
#     # 例如，你可以为每个问题创建一个临时的Agent和Task
#     # 然后调用crew.kickoff()来获取结果

#     # 假设 create_crew_and_kickoff 是一个函数，它接受问题并返回答案
#     result = create_crew_and_kickoff(question)
    
#     # 将结果转换为JSON格式并返回
#     return jsonify(result)

# if __name__ == '__main__':
#     app.run(debug=True)
    


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['input_text']
        # 这里调用你的逻辑处理函数，例如 result = some_function(user_input)
        # 假设 some_function 返回处理结果
        # result = some_function(user_input)
#         result = "处理中..."  # 占位符，实际应为函数调用结果
        task1_user, task2_user = str(user_input).split('|').split('｜')
        ai_assistant = AIAssistant(model_name=model_name, task1_user,task2_user)
        result = ai_assistant.kickoff()
        return render_template_string(TEMPLATE, user_input=user_input, result=result)
    return render_template_string(TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10086, debug=True)

# HTML 模板
TEMPLATE = '''
<html>
<body>
    <h1>输入问题</h1>
    <form method="post">
        <input type="text" name="input_text" placeholder="请输入问题" />
        <input type="submit" value="提交" />
    </form>
    {% if user_input %}
        <h2>你的问题:</h2>
        <p>{{ user_input }}</p>
        {% if result %}
            <h2>答案:</h2>
            <p>{{ result }}</p>
        {% endif %}
    {% endif %}
</body>
</html>
'''