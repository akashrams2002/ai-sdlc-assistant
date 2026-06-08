import streamlit as st

from src.orchestrator.orchestrator import Orchestrator


st.set_page_config(
    page_title="AI SDLC Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI SDLC Assistant")

st.markdown(
    "Generate Requirements, Design, Tasks and Code from a Project Idea."
)

project_idea = st.text_input(
    "Enter Project Idea",
    placeholder="Example: Online Food Delivery App"
)

if st.button("🚀 Generate"):

    with st.spinner("Generating SDLC Artifacts..."):

        orchestrator = Orchestrator()

        result = orchestrator.execute(
            project_idea
        )

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Requirements",
            "Design",
            "Tasks",
            "Code"
        ]
    )

    with tab1:

        for req in result["requirements"]:
            st.write(req)

    with tab2:

        for item in result["design"]:
            st.write(item)

    with tab3:

        for task in result["tasks"]:
            st.write(task)

    with tab4:

        if result["code"]:

            for code in result["code"]:
                st.code(
                    code,
                    language="python"
                )

        else:

            st.info(
                "No code generated for the current task list."
            )

    st.success(
        "Documentation generated successfully!"
    )

    requirements_text = "\n".join(
        result["requirements"]
    )

    design_text = "\n".join(
        result["design"]
    )

    tasks_text = "\n".join(
        result["tasks"]
    )

    st.subheader("Download Generated Artifacts")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.download_button(
            "📥 Requirements",
            requirements_text,
            file_name="requirements.md",
            mime="text/markdown"
        )

    with col2:

        st.download_button(
            "📥 Design",
            design_text,
            file_name="design.md",
            mime="text/markdown"
        )

    with col3:

        st.download_button(
            "📥 Tasks",
            tasks_text,
            file_name="tasks.md",
            mime="text/markdown"
        )