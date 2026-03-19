from utils import search_github_users, get_user_details, extract_skills, calculate_fit_score, match_location
from utils import ai_score_candidate

if __name__ == "__main__":
    
    # Job Description Skills
    jd_skills = ["python", "machine learning", "ai"]
    target_location = "Hyderabad"   # or "Riyadh"

    users = search_github_users("python developer")
    
    candidates = []

    for user in users:
        username = user['login']
        
        details = get_user_details(username)
        bio = details.get("bio") or ""
        location = details.get("location") or ""

        skills = extract_skills(bio)

        # Skip if no skills found
        if not skills:
            continue

        # Rule-based score
        score = calculate_fit_score(skills, jd_skills, bio, location, target_location)

        # AI score
        ai_score = ai_score_candidate(bio, jd_skills)

        # Combine both
        final_score = (score * 0.7) + (ai_score * 0.3)

        candidates.append({
            "name": username,
            "skills": skills,
            "location": location,
            "score": round(final_score, 2)
})

    # Sort candidates by score (highest first)
    ranked_candidates = sorted(candidates, key=lambda x: x['score'], reverse=True)

    print("\n🏆 Top Candidates:\n")

    for candidate in ranked_candidates:
        print(f"Name: {candidate['name']}")
        print(f"Skills: {candidate['skills']}")
        print(f"Location: {candidate['location']}")
        print(f"Score: {candidate['score']}")
        print("-" * 40)