import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# ----------------------------
# Load API Key
# ----------------------------
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Placement Preparation Agent",
    page_icon="🎯",
    layout="wide"
)

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("🎯 AI Placement Agent")
st.sidebar.image(
    "https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg",
    width=150
)
st.sidebar.write("Your Personal Placement Preparation Assistant")

st.sidebar.markdown("---")

st.sidebar.subheader("Project Features")
st.sidebar.write("✅ Skill Gap Analysis")
st.sidebar.write("✅ Placement Readiness Score")
st.sidebar.write("✅ 4-Week Study Plan")
st.sidebar.write("✅ Learning Resources")
st.sidebar.write("✅ Mock Interview Questions")
st.sidebar.write("✅ Resume Tips")
st.sidebar.write("✅ Company Suggestions")

st.sidebar.markdown("---")
st.sidebar.success("Built using Streamlit + Gemini AI")

# ----------------------------
# Main Title
# ----------------------------
st.title("🎯 AI Placement Preparation Agent")

st.markdown(
    """
This AI agent analyzes your profile and generates a personalized placement preparation plan.

Fill in your details below and click **Analyze**.
"""
)

# ----------------------------
# Student Details
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("👤 Student Name")
    branch = st.text_input("🎓 Branch")
    cgpa = st.number_input("📘 CGPA", 0.0, 10.0, 8.0)

with col2:
    year = st.selectbox(
        "📅 Year",
        ["1st Year", "2nd Year", "3rd Year", "4th Year"]
    )

    career_goal = st.text_input("💼 Career Goal")

skills = st.text_area(
    "💻 Skills",
    placeholder="Example: Python, Java, SQL, HTML, CSS"
)
resume = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type=["pdf"]
)


strengths = st.text_area(
    "💪 Strengths",
    placeholder="Example: Problem Solving, Communication"
)

weaknesses = st.text_area(
    "📉 Weaknesses",
    placeholder="Example: Aptitude, DSA"
)

st.markdown("---")

analyze = st.button("🚀 Analyze My Profile")
if analyze:

    prompt = f"""
You are an expert Placement Preparation Mentor.

Student Details

Name: {name}
Branch: {branch}
CGPA: {cgpa}
Year: {year}
Skills: {skills}
Strengths: {strengths}
Weaknesses: {weaknesses}
Career Goal: {career_goal}

Generate a professional placement report with the following headings:

1. Student Profile Summary

2. Placement Readiness Score (Out of 100)

3. Skill Gap Analysis

4. Four Week Preparation Plan

Week 1
Week 2
Week 3
Week 4

5. Best Learning Resources

6. Aptitude Preparation Tips

7. Coding Preparation Tips

8. Resume Improvement Tips

9. Top 10 Mock Interview Questions

10. Best Companies Suitable for this Student

11. Final Suggestions
"""

    try:

        with st.spinner("🔍 AI is analyzing your profile..."):

            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=prompt
            )

        st.success("✅ Analysis Completed Successfully!")
        st.progress(100)

        st.metric(
           label="Placement Readiness",
           value="85/100",
           delta="+10"
        )

        st.markdown("## 📄 AI Placement Report")

        st.write(response.text)
        st.markdown("## 📚 Recommended Learning Platforms")

        st.markdown("""
         - 🔹 LeetCode - https://leetcode.com
         - 🔹 GeeksforGeeks - https://www.geeksforgeeks.org
         - 🔹 HackerRank - https://www.hackerrank.com
         - 🔹 Smart Interviews - https://smartinterviews.in
         - 🔹 Coursera - https://www.coursera.org
         """)
        st.download_button(
        label="📥 Download Placement Report",
        data=response.text,
        file_name="placement_report.txt",
        mime="text/plain"
        )

    except Exception as e:
       st.error("❌ Error occurred")
       st.write(e)

# ----------------------------
# Progress Tracker
# ----------------------------

st.markdown("---")

st.subheader("📈 Placement Preparation Progress")

progress = st.slider(
    "How much have you completed?",
    0,
    100,
    50
)

st.progress(progress)


# ----------------------------
# Footer
# ----------------------------

st.caption(
    "🎯 AI Placement Preparation Agent | Developed by Anudeepthi | Internship Project 2026"
)