import re

def is_ats_compliant(resume, job_description):
    # A list of keywords that are commonly used by ATS systems
    ats_keywords = ["skill", "experience", "education", "certification", "qualification"]
    # list of keywords from job description
    job_keywords = re.findall(r'\b\w+\b', job_description)
    matched_keywords = []
    unmatched_keywords = []
    # Use regular expressions to search for the keywords in the resume
    for keyword in ats_keywords:
        if re.search(keyword, resume, re.IGNORECASE):
            for job_keyword in job_keywords:
                if re.search(job_keyword, resume, re.IGNORECASE):
                    matched_keywords.append(job_keyword)
                else:
                    unmatched_keywords.append(job_keyword)
    if matched_keywords:
        match_percentage = (len(matched_keywords) / len(job_keywords)) * 100
        return matched_keywords, unmatched_keywords, match_percentage
    else:
        return None, None, None

# Read the resume and job description from files
with open("resume.txt", "r") as resume_file:
    resume = resume_file.read()

with open("job_description.txt", "r") as job_description_file:
    job_description = job_description_file.read()

matched_keywords, unmatched_keywords, match_percentage = is_ats_compliant(resume, job_description)
if matched_keywords:
    print("Matched keywords: ", matched_keywords)
    print("Unmatched keywords: ", unmatched_keywords)
    print("Match Percentage: ", match_percentage)
else:
    print("This resume is not ATS compliant with the job description.")
