# recommender.py

# Simple career mapping based on keywords
career_map = {
    "python": ["Data Scientist", "ML Engineer", "Backend Developer"],
    "java": ["Android Developer", "Software Engineer"],
    "excel": ["Data Analyst", "Business Analyst"],
    "communication": ["HR Manager", "Public Relations"],
    "creative": ["UI/UX Designer", "Content Creator"],
    "ai": ["AI Engineer", "Research Scientist"],
    "machine learning": ["ML Engineer", "Data Scientist"],
    "web": ["Frontend Developer", "Full Stack Developer"],
}

def recommend_careers(text):
    text = text.lower()
    recommended = set()
    for keyword, careers in career_map.items():
        if keyword in text:
            recommended.update(careers)
    return list(recommended) if recommended else ["Career Counselor", "Generalist"]
