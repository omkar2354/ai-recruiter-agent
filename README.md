# 🚀 AI Recruiter Agent

An intelligent **AI-powered Recruiter System** that automatically finds, evaluates, and ranks candidates based on job requirements using **GitHub data + LLM (Groq)**.

---

## 🎯 Project Goal

Build a smart system that:

* Takes a Job Description (JD)
* Finds candidates from GitHub
* Extracts their skills
* Scores them using rule-based + AI
* Ranks top candidates

---

## 🧠 How It Works

```
Job Skills Input
        ↓
GitHub API (Fetch Users)
        ↓
Profile Data (Bio, Location)
        ↓
Skill Extraction (NLP)
        ↓
Rule-Based Scoring
        ↓
AI Scoring (Groq LLM)
        ↓
Final Score (Hybrid)
        ↓
Ranking (Top Candidates)
```

---

## ⚙️ Tech Stack

* 🐍 Python 3.12.8
* 🌐 GitHub REST API
* 🤖 Groq (LLM - AI Scoring)
* 📦 requests
* 🔐 python-dotenv

---

## 📁 Project Structure

```
Recruiter_Agent/
│── main.py              # Main execution file
│── utils.py             # Core logic functions
│── config.py            # API key config
│── requirements.txt     # Dependencies
│── .env                 # API keys (not uploaded)
```

---

## 🔥 Features

* ✅ Real-time GitHub user search
* ✅ Skill extraction from bio
* ✅ Rule-based scoring system
* ✅ AI-powered semantic scoring
* ✅ Hybrid scoring (Rule + AI)
* ✅ Candidate ranking system
* ✅ Handles missing/dirty data

---

## 🧪 Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/repo-name.git
cd repo-name
```

---

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Add API Key

Create `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

### 5. Run the project

```
python main.py
```

---

## 📊 Sample Output

```
🏆 Top Candidates:

Name: Developer123
Skills: ['python', 'ai']
Location: India
Score: 78.5
----------------------------------------
```

---

## 🧠 Key Concepts Used

* API Integration
* JSON Handling
* NLP (Skill Extraction)
* Scoring Algorithms
* LLM Integration (Groq)
* Data Cleaning
* Ranking Systems

---

## 💡 Real-World Applications

* Recruitment automation systems
* Resume screening tools (ATS)
* Talent ranking platforms
* AI hiring assistants

---

## ⚠️ Limitations

* GitHub data can be incomplete
* Skill extraction is keyword-based
* Location data is unstructured
* AI scoring depends on API response

---

## 🚀 Future Improvements

* 🔹 Resume parsing (PDF upload)
* 🔹 Streamlit web UI
* 🔹 Better skill extraction (NLP models)
* 🔹 Database integration
* 🔹 Multi-platform support (LinkedIn, job portals)

---

## 🧑‍💻 Author

**Omkar Chougule**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share with others!
