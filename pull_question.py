import os
import requests
import pandoc
import sys
from icecream import ic

print("sys.argv", sys.argv, len(sys.argv))


def html_to_md(structured_html):
    html_ = pandoc.read(structured_html, None, 'html')
    # ic(html_)
    # tmp = pandoc.read(html_,None,'html')
    return pandoc.write(html_, None, 'markdown')


def create_structure(_question_response):
    link = _question_response['link']
    question_json = _question_response['question']
    full_title = f"{question_json['questionFrontendId']}. {question_json['title']}"
    print("Full title:", full_title)
    html_output = f"""<body><h1><a href="https://leetcode.com{link}">{question_json['title']}</a></h1>{
    question_json['content']}{"".join([f"<br><details><summary>Hint {i + 1}</summary>{hint}</details>" for i, hint in enumerate(question_json['hints'])])}</body>"""
    # html_output = f"""<title>{full_title}</title><body><h1><a href="https://leetcode.com{link}">{question_json['title']}</a></h1>{
    # question_json['content']}{"".join([f"<br><details><summary>Hint {i + 1}</summary>{hint}</details>" for i, hint in enumerate(question_json['hints'])])}</body>"""

    md_output = html_to_md(html_output)
    folder_path = f"./Python/unsolved/{full_title}"
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"Folder {folder_path} created")

        with open(f"{folder_path}/description.md", "w") as f:
            f.write(md_output)

        print("Description file created")

        python_script_output = next(x['code'] for x in question_json['codeSnippets'] if x['lang'] == 'Python3')

        with open(f"{folder_path}/solution.py", "w") as f:
            f.write(python_script_output)

        print("Script file created")
    else:
        print("Folder already exists!")


question_response = ""


def fetch_daily():
    url = "https://leetcode.com/graphql"
    payload = "{\"query\":\"query getDailyProblem {\\n\\tactiveDailyCodingChallengeQuestion {\\n\\t\\tdate\\n\\t\\tlink\\n\\t\\tquestion {\\n\\t\\t\\tquestionId\\n\\t\\t\\tquestionFrontendId\\n\\t\\t\\ttitle\\n\\t\\t\\tcontent\\n\\t\\t\\tdifficulty\\n\\t\\t\\texampleTestcases\\n\\t\\t\\tcodeSnippets {\\n\\t\\t\\t\\tlang\\n\\t\\t\\t\\tlangSlug\\n\\t\\t\\t\\tcode\\n\\t\\t\\t}\\n\\t\\t\\thints\\n\\t\\t}\\n\\t}\\n}\\n\",\"operationName\":\"getDailyProblem\"}"
    headers = {
        "cookie": "csrftoken=R9HLriOs2cznMU05QFMLATNf1AXNrEQCXQNxzFI6xW8fSxheGf7X3bMy5eZyM60i; __cf_bm=2HExO3q8oYLg9nQ_OmOoqlIaO3NlH7JhFPW4CETdJz4-1723080506-1.0.1.1-.7m9k7YK67lNKGwzxPlkWYxAAuEN5ZLoBFUigcrx3uQa1rP3ix2BwO7vgCcnd2LgO1kx4pYeqIhhZZF4fcxDUQ",
        "Content-Type": "application/json"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print("Pull response:", response)
    return response.json()['data']['activeDailyCodingChallengeQuestion']


def get_leetcode_problem_slug_text_by_number(question_number):
    # Fetch all problems from LeetCode's API
    response = requests.get("https://leetcode.com/api/problems/all/")
    data = response.json()

    # Search for the question by frontend ID
    for problem in data["stat_status_pairs"]:
        if problem["stat"]["frontend_question_id"] == question_number:
            return problem["stat"]["question__title_slug"]
            # return {
            #     "question_id": problem["stat"]["question_id"],
            #     "frontend_id": problem["stat"]["frontend_question_id"],
            #     "title": problem["stat"]["question__title"],
            #     "title_slug": problem["stat"]["question__title_slug"],
            #     "difficulty": problem["difficulty"]["level"],  # 1: Easy, 2: Medium, 3: Hard
            #     "is_paid": problem["paid_only"]
            # }
    return None  # Question not found


def get_problem_details(title_slug):
    url = "https://leetcode.com/graphql"

    payload = "{\"query\":\"query questionData($titleSlug: String!) {\\n\\t\\n  question(titleSlug: $titleSlug) {\\n    questionId\\n    questionFrontendId\\n\\t\\ttitle\\n\\t\\tcontent\\n\\t\\tdifficulty\\n\\t\\texampleTestcases\\n\\t\\tcodeSnippets {\\n\\t\\t\\tlang\\n\\t\\t\\tlangSlug\\n\\t\\t\\tcode\\n\\t\\t}\\n\\t\\thints\\n  }\\n\\t\\n}\",\"variables\":{\"titleSlug\":\"4sum-ii\"},\"operationName\":\"questionData\"}"
    headers = {
        "cookie": "csrftoken=R9HLriOs2cznMU05QFMLATNf1AXNrEQCXQNxzFI6xW8fSxheGf7X3bMy5eZyM60i",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    # print(response.text)
    return response.json()['data']['question']


if len(sys.argv) == 1:
    print("Fetching daily problem")
    question_response = fetch_daily()
if len(sys.argv) == 2:
    print("Fetching problem", int(sys.argv[1]))

    # Example: Fetch problem #454 (4Sum II)
    problem_slug_text = get_leetcode_problem_slug_text_by_number(int(sys.argv[1]))
    print("problem_slug_text", problem_slug_text)
    question_response = dict()
    question_inside = get_problem_details(problem_slug_text)
    # ic(question_inside, question_inside.keys())
    # question_inside['title']=question_inside['question']['title']

    question_response['question'] = question_inside
    question_response['link'] = f"/problems/{problem_slug_text}/"
    # question_response['question']['questionFrontendId'] = sys.argv[1]
    # question_response['question'] = f"/problems/{problem_slug_text}/"

    # exit()
    # fetch_all_response = fetch_all()
    # ic(fetch_all_response)

create_structure(_question_response=question_response)

# TODO use pandoc to transform html to markdown
