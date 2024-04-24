import os
from crewai import Agent
import streamlit as st
from langchain_groq import ChatGroq
from langchain.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()

llm = ChatGroq(model="mixtral-8x7b-32768",
                             verbose = True,
                             temperature = 0.6,
                             groq_api_key="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")

def streamlit_callback(step_output):
    # This function will be called after each step of the agent's execution
    st.markdown("---")
    for step in step_output:
        if isinstance(step, tuple) and len(step) == 2:
            action, observation = step
            if isinstance(action, dict) and "tool" in action and "tool_input" in action and "log" in action:
                st.markdown(f"# Action")
                st.markdown(f"**Tool:** {action['tool']}")
                st.markdown(f"**Tool Input** {action['tool_input']}")
                st.markdown(f"**Log:** {action['log']}")
                st.markdown(f"**Action:** {action['Action']}")
                st.markdown(
                    f"**Action Input:** ```json\n{action['tool_input']}\n```")
            elif isinstance(action, str):
                st.markdown(f"**Action:** {action}")
            else:
                st.markdown(f"**Action:** {str(action)}")

            st.markdown(f"**Observation**")
            if isinstance(observation, str):
                observation_lines = observation.split('\n')
                for line in observation_lines:
                    if line.startswith('Title: '):
                        st.markdown(f"**Title:** {line[7:]}")
                    elif line.startswith('Link: '):
                        st.markdown(f"**Link:** {line[6:]}")
                    elif line.startswith('Snippet: '):
                        st.markdown(f"**Snippet:** {line[9:]}")
                    elif line.startswith('-'):
                        st.markdown(line)
                    else:
                        st.markdown(line)
            else:
                st.markdown(str(observation))
        else:
            st.markdown(step)

class LegalAgents():

    def legal_researcher(self):
        return Agent(
            role='Senior Researcher Indian Lawyer',
            goal='Search for a legal cases and its judgments from the Supreme Court of India that are similar type of provided case and write detailed discription',
            backstory="""You work at a leading Indian Law Firm.
             Your expertise lies in searching same legal cases that are similar to provided case.
             You have a knack for dissecting complex data and presenting actionable insights.""",
            tools=[
                search_tool
            ],
            llm = llm,
            verbose=True,
            step_callback=streamlit_callback,
        )

    def legal_analyst(self):
        return Agent(
            role='Legal Case Analyst',
            goal='Analyse the provided legal case and check this case comes under in which Indian laws article/articles',
            backstory="""You are a renowned legal case analyst, known for your insightful and engaging analysis.
             You can analyse very complicated legal cases also.""",
            tools=[
                search_tool
            ],
            llm = llm,
            verbose=True,
            step_callback=streamlit_callback,
        )

    def legal_strategiest(self):
        return Agent(
            role='Legal Case Strategiest',
            goal="""Analyse Provided Case and Using the insight provided, develop a strategy to win this case in Indian Supreme Court""",
            backstory="""You are a renowned legal case strategiest, known for your insightful and engaging strategies.
             You can analyse very complicated legal cases and make winning strategies.""",
            tools=[
                search_tool
            ],
            llm = llm,
            verbose=True,
            step_callback=streamlit_callback,
        )