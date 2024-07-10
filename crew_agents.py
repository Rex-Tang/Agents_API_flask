# 假设上述的 Agent, Task, Crew 类和 Ollama 类已经定义好并且可以使用
from langchain.llms import Ollama
from crewai import Agent, Task, Crew
import os
class AIAssistant:
    def __init__(self, model_name, task1_user, task2_user):
        # 初始化模型，模型名称作为构造函数的参数
        self.llm = Ollama(model=model_name)
        
        # 定义具有角色和目标的代理
        self.researcher = Agent(
            role='AI算法工程师',
            goal='揭示AI和数据科学的最前沿发展',
            backstory="""...（省略了部分内容）""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm  # 使用类的实例变量 llm
        )
        self.writer = Agent(
            role='技术内容策略师',
            goal='撰写关于技术进步的引人入胜的内容',
            backstory="""...（省略了部分内容）""",
            verbose=True,
            allow_delegation=True,
            llm=self.llm  # 使用类的实例变量 llm
        )

        # 为你的代理创建任务
        self.task1 = Task(
            description=task1_user,
            agent=self.researcher,
            expected_output="最后生成一篇3段的博客，需要是中文的"
        )
        self.task2 = Task(
            description=task2_user,
            agent=self.writer,
            expected_output="至少3段的完整博客文章，语言是中文"
        )

        # 实例化你的团队并采用顺序处理
        self.crew = Crew(
            agents=[self.researcher, self.writer],
            tasks=[self.task1, self.task2],
            verbose=2
        )

    def kickoff(self):
        # 让你的团队开始工作
        return self.crew.kickoff()

