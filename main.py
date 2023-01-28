#!/usr/bin/env python3
import re

prepositions = ["at", "by", "in", "of", "on", "to", "with"]
pronouns = ["I", "you", "he", "she", "it", "we", "they"]
helping_verbs=["am","is","are","was","were","be","being","been","have","has","had","do","does","did","can","could","may","might","must","shall","should","will","would","ought","their","help","based","hold","when","make","more","which","use","this"]
conjunctions=["and","or","also","because","so","yet","unless","until","before","after","while","once","since","whenever","where","as","both","either","neither","nor","if","all","for","end","a","us","if","all","from","able","today","good","our","life"]
other_words =["that","use","speak","here","home","love","its","power","said","great","needs","what","an","put","your"]

def remove_prepositions_pronouns(list_with_prepositions_pronouns):
    remove_list = prepositions+pronouns+helping_verbs+conjunctions+other_words
    #return [word for word in list_with_prepositions_pronouns if word.lower() not in prepositions and word.lower() not in pronouns and word.lower() not in helping_verbs and word.lower() not in conjunctions]
    return [word for word in list_with_prepositions_pronouns if word.lower() not in remove_list]

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
        matched_keywords =remove_prepositions_pronouns([*set(matched_keywords)])
        unmatched_keywords =  remove_prepositions_pronouns([*set(unmatched_keywords)])
        job_keywords =  remove_prepositions_pronouns([*set(job_keywords)])
        match_percentage = (len(matched_keywords) / len(job_keywords)) * 100
        return matched_keywords, unmatched_keywords, match_percentage
    else:
        return None, None, None

def match_count(matched_keywords):
    with open("job_description.txt", "r") as job_description_file:
        job_description = job_description_file.readlines()
    
    no_match = 0
    one_match = 0
    two_match = 0
    more_than_two = 0
    match_list=[[],[],[],[]]
    # loop through the lines in the file
    for line in job_description:
        if(line == '\n' or line == ""):
            continue
        matches = 0
        # loop through the keywords
        for keyword in matched_keywords:
            # check if the keyword is in the line
            if keyword in line:
                matches += 1
        # check how many keywords are matched in the line
        if matches == 0:
            no_match += 1
            match_list[0].append(line)
        elif matches == 1:
            if(line in match_list[0]):
                match_list[0].remove(line)
            match_list[1].append(line)
            one_match += 1
        elif matches == 2:
            if(line in match_list[1]):
                match_list[1].remove(line)
            match_list[2].append(line)
            two_match += 1
        else:
            if(line in match_list[2]):
                match_list[2].remove(line)
            match_list[3].append(line)
            more_than_two += 1
            #print("Line matching more than 2 keywords:", line)

    # print the results
    print("\n\nLines not matching any keyword:", no_match , "\n",match_list[0])
    print("\n\nLines matching exactly one keyword:", one_match, "\n",match_list[1])
    print("\n\nLines matching exactly two keywords:", two_match, "\n",match_list[2])
    print("\n\nLines matching more than two keywords:", more_than_two, "\n",match_list[3])

    #print(match_list)


def main():
    # Read the resume and job description from files
    with open("resume.txt", "r") as resume_file:
        resume = resume_file.read()

    with open("job_description.txt", "r") as job_description_file:
        job_description = job_description_file.read()

    matched_keywords, unmatched_keywords, match_percentage = is_ats_compliant(resume, job_description)
    if matched_keywords:
        print("Matched keywords: ", matched_keywords)
        print("\n\n")
        print("Unmatched keywords: ", unmatched_keywords)
        print("\n\n")
        print("Match Percentage: ", match_percentage)
    else:
        print("This resume is not ATS compliant with the job description.")
    
    match_count(matched_keywords)

if __name__ == "__main__":
    main()
