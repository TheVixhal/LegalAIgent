from crewai import Crew
from agents import LegalAgents
from tasks import LegalTasks
import streamlit as st
import datetime

st.set_page_config(page_icon=":bar_chart:", layout="wide")


def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )


class LegalCrew:

    def __init__(self, Provided_Case):
        self.Provided_Case = Provided_Case
        self.output_placeholder = st.empty()

    def run(self):
        agents = LegalAgents()
        tasks = LegalTasks()

        researcher = agents.legal_researcher()
        analyst = agents.legal_analyst()
        strategiest = agents.legal_strategist()

        task1 = tasks.task1(
            researcher,
            self.Provided_Case
        )

        task2 = tasks.task2(
            analyst,
            self.Provided_Case
        )

        task3 = tasks.task3(
            strategiest
        )

        crew = Crew(
            agents=[
                researcher, analyst, strategiest
            ],
            tasks=[task1, task2, task3],
            verbose=True
        )

        result = crew.kickoff()
        self.output_placeholder.markdown(result)

        return result


if __name__ == "__main__":
    icon("LegalAIgent")

    st.subheader("LegalAI",
                 divider="rainbow", anchor=False)

    import datetime

    today = datetime.datetime.now().date()
    next_year = today.year + 1
    jan_16_next_year = datetime.date(next_year, 1, 10)

    with st.sidebar:
        st.header("👇 Enter your Case details")
        with st.form("my_form"):
            Provided_Case = st.text_input(
                "Your Case Details...", placeholder="Your Case Details...")
            


            submitted = st.form_submit_button("Submit")

        st.divider()

        st.header(" Developer: Vishal Baraiya ")
        # Credits to Vishal Baraiya for the code
        st.sidebar.markdown(
            """
        Credits to **Vishal Baraiya** 
        for creating **LegalAIgent** 🚀
        """,
            unsafe_allow_html=True
        )

        st.sidebar.info("Click here to visit GitHub repo", icon="👇")
        st.sidebar.markdown(
            """
        <a href="" target="_blank">
            
        </a>
        """,
            unsafe_allow_html=True
        )


if submitted:
    with st.status("🤖 **Agents at work...**", state="running", expanded=True) as status:
        with st.container(height=500, border=False):
            legal_crew = LegalCrew(Provided_Case)
            result = legal_crew.run()
        status.update(label="✅ Legal Case Strategy Ready!",
                      state="complete", expanded=False)

    st.subheader("Here is your Strategy", anchor=False, divider="rainbow")
    st.markdown(result)
