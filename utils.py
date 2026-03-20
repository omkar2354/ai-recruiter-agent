import requests
from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def search_github_users(query):
    url = f"https://api.github.com/search/users?q={query}&per_page=5"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['items']
    return []


def get_user_details(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    return {}


def extract_skills(bio):
    if not bio:
        return []

    skills_list = ["python", "java", "machine learning", "ai", "data", "react", "node"]

    found_skills = []
    bio_lower = bio.lower()

    for skill in skills_list:
        if skill in bio_lower:
            found_skills.append(skill)

    return found_skills


def match_location(candidate_location, target_location):
    if not candidate_location:
        return False

    candidate_location = candidate_location.lower()

    return (
        target_location.lower() in candidate_location
        or "india" in candidate_location
        or "saudi" in candidate_location
    )


def calculate_fit_score(candidate_skills, jd_skills, bio, location, target_location):
    score = 0

    # Skill Match (70)
    match_count = len(set(candidate_skills) & set(jd_skills))
    skill_score = (match_count / len(jd_skills)) * 70 if jd_skills else 0
    score += skill_score

    # Bio Quality (20)
    if bio and len(bio) > 30:
        score += 20
    elif bio:
        score += 10

    # Location Match (10)
    if match_location(location, target_location):
        score += 10

    return round(score, 2)

def ai_score_candidate(bio, jd_skills):
    if not bio:
        return 0

    prompt = f"""
    Job requires: {jd_skills}
    Candidate bio: {bio}

    Give score from 0 to 100.
    Only return a number.
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )

        text = response.choices[0].message.content.strip()
        print("AI RESPONSE:", text)

        import re
        match = re.search(r"\d+", text)

        return float(match.group()) if match else 0

    except Exception as e:
        print("ERROR:", e)
        return 0
