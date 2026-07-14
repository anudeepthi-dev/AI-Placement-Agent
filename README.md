# 🎯 AI Placement Preparation Agent

An AI-powered application that helps students prepare for placements by analyzing their skills, identifying skill gaps, creating preparation plans, and providing career guidance.

## 🚀 Features

✅ Student Profile Analysis  
✅ Skill Gap Analysis  
✅ Placement Readiness Score  
✅ Personalized 4-Week Preparation Plan  
✅ Learning Resource Recommendations  
✅ Aptitude Preparation Tips  
✅ Coding Preparation Guidance  
✅ Resume Improvement Suggestions  
✅ Mock Interview Questions  
✅ Suitable Company Suggestions  
✅ Downloadable Placement Report  
✅ Preparation Progress Tracker  

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini AI
- python-dotenv

## 📂 Project Structure

```text
AI-Placement-Agent
│
├── app.py
├── test.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

## ⚙️ Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## 🔑 API Key Setup

Create a file named:

```text
.env
```

Add your Gemini API key:

```text
GOOGLE_API_KEY=your_api_key_here
```

**Note:** Never share your real API key or upload the `.env` file to GitHub.

## ▶️ Run Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 🎯 How It Works

1. Enter student details such as name, branch, CGPA, skills, strengths, and weaknesses.
2. Click the **Analyze My Profile** button.
3. Gemini AI analyzes the student profile.
4. The application generates:
   - Placement readiness score
   - Skill gap analysis
   - 4-week preparation plan
   - Learning resources
   - Coding and aptitude tips
   - Mock interview questions
   - Company suggestions
5. Download the generated placement report.

## 🔮 Future Enhancements

- Resume analysis using AI
- Database integration for storing student profiles
- AI mock interview chatbot
- Placement analytics dashboard
- Personalized career recommendations

## 👩‍💻 Developer

Developed by Anudeepthi

Internship Project 2026

## 📜 License

This project is created for educational and internship purposes.