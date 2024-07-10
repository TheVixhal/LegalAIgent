from crewai import Agent
from langchain_groq import ChatGroq
from langchain.tools import DuckDuckGoSearchRun
import streamlit as st

search_tool = DuckDuckGoSearchRun()
llm = ChatGroq(model="mixtral-8x7b-32768", verbose=True, temperature=0.6, groq_api_key="paste your groq api key")

def streamlit_callback(step_output):
    st.markdown("---")
    for step in step_output:
        if isinstance(step, tuple) and len(step) == 2:
            action, observation = step
            if isinstance(action, dict):
                st.markdown(f"# Action")
                st.markdown(f"**Tool:** {action.get('tool', '')}")
                st.markdown(f"**Tool Input:** {action.get('tool_input', '')}")
                st.markdown(f"**Log:** {action.get('log', '')}")
                st.markdown(f"**Action:** {action.get('action', '')}")
            elif isinstance(action, str):
                st.markdown(f"**Action:** {action}")

            st.markdown(f"**Observation:** {str(observation)}")

class LegalAgents:

    def legal_researcher(self):
        return Agent(
            role='Senior Research Lawyer',
            goal='Conduct comprehensive legal research on cases and judgments from the Supreme Court of India similar to a provided legal case.',
            backstory="""You are an experienced senior research lawyer with deep expertise in Indian law. 
             Your proficiency lies in identifying cases similar to a provided case and presenting detailed analyses of judgments and legal precedents.""",
            tools=[search_tool],
            llm=llm,
            verbose=True,
            step_callback=streamlit_callback,
        )

    def legal_analyst(self):
        return Agent(
            role='Legal Case Analyst',
            goal='Analyze a provided legal case to determine which Indian laws and articles apply.',
            backstory="""As a skilled legal case analyst, you excel in examining complex legal cases and identifying relevant Indian laws and articles. 
             Your insightful analysis helps provide clarity on the legal implications of a case.""",
            tools=[search_tool],
            llm=llm,
            verbose=True,
            step_callback=streamlit_callback,
        )

    def legal_strategist(self):
        return Agent(
            role='Legal Case Strategist',
            goal='Develop a winning strategy for a provided case in the Indian Supreme Court, High Court, or district court using given insights and research.',
            backstory="""You are a distinguished legal case strategist known for your ability to create winning strategies for complex legal cases.
             Your approach combines insights from research, legal precedents, and the applicable laws to craft compelling arguments and strategies.""",
            tools=[search_tool],
            llm=llm,
            verbose=True,
            step_callback=streamlit_callback,
        )
