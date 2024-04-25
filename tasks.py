from crewai import Task
from textwrap import dedent


class LegalTasks():

    def task1(self, agent, Provided_Case):
        return Task(description=dedent(f"""Search for a legal cases and thier judgments from the Supreme Court of India that is similar to a provided case and write detailed discription. The Provided Case: {Provided_Case}."""),
            expected_output="write detailed discription",
            agent=agent)

    def task2(self, agent, Provided_Case):
        return Task(description=dedent(f"""Analyse Provided legal case and check this case comes under which Indian law article/articles. The Provided Case: {Provided_Case}.
          """),
            expected_output="Write detailed Insights",
            agent=agent)

    def task3(self, agent):
        return Task(description=dedent(f"""Analyse Provided Case and Using given Detailed discription and given detailed Insights of provided case, develop a strategy to win this case in Indian Supreme Court/high court/district court.
          """),
            expected_output="Write best detailed winning strategy with referencing indian laws, articles and old judgements of indian supreme courtand High court.",
            agent=agent)

