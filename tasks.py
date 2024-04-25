from crewai import Task
from textwrap import dedent

class LegalTasks:

    def task1(self, agent, Provided_Case):
        return Task(
            description=dedent(f"""
             Search for legal cases and their judgments from the Supreme Court of India that are similar to the provided case. 
             The agent must provide a detailed summary of the cases and judgments found, including any relevant legal precedents and key insights. 
             The provided case is: {Provided_Case}.
             """),
            expected_output="Detailed summary of similar legal cases and their judgments from the Supreme Court of India, including legal precedents and key insights relevant to the provided case.",
            agent=agent
        )

    def task2(self, agent, Provided_Case):
        return Task(
            description=dedent(f"""
             Analyze the provided legal case and identify the Indian law articles under which this case falls. 
             The agent should assess the case and specify the relevant sections of Indian law. 
             The provided case is: {Provided_Case}.
            """),
            expected_output="Detailed analysis of the provided legal case, including the specific Indian law articles applicable to the case and an explanation of how the case falls under these laws.",
            agent=agent
        )

    def task3(self, agent):
        return Task(
            description=dedent(f"""
             Using the detailed description and insights from the provided case, develop a legal strategy to win this case in the Indian Supreme Court, High Court, or district court. 
             The strategy should reference relevant Indian laws, articles, and past judgments from the Indian Supreme Court and High Courts.
             """),
            expected_output="Comprehensive legal strategy to win the case, including references to Indian laws, articles, and past judgments from the Indian Supreme Court and High Courts, along with specific tactics and arguments that could be used in court.",
            agent=agent
        )
