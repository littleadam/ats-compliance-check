import re
prepositions = ["at", "by", "in", "of", "on", "to", "with"]
pronouns = ["I", "you", "he", "she", "it", "we", "they"]

# Sample list
list_with_prepositions_pronouns = ["This", "is", "a", "sentence", "with", "some", "prepositions", "and","pronouns", "in", "it"]

# Function to remove prepositions and pronouns
def remove_prepositions_pronouns(list_with_prepositions_pronouns):
    return [word for word in list_with_prepositions_pronouns if word.lower() not in prepositions and word.lower() not in pronouns]

# Call the function
list_without_prepositions_pronouns = remove_prepositions_pronouns(list_with_prepositions_pronouns)

# Print the result
print(list_without_prepositions_pronouns)

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
