import os
import requests

url = "https://leetcode.com/graphql"

payload = "{\"query\":\"query getDailyProblem {\\n\\tactiveDailyCodingChallengeQuestion {\\n\\t\\tdate\\n\\t\\tlink\\n\\t\\tquestion {\\n\\t\\t\\tquestionId\\n\\t\\t\\tquestionFrontendId\\n\\t\\t\\ttitle\\n\\t\\t\\tcontent\\n\\t\\t\\tdifficulty\\n\\t\\t\\texampleTestcases\\n\\t\\t\\tcodeSnippets {\\n\\t\\t\\t\\tlang\\n\\t\\t\\t\\tlangSlug\\n\\t\\t\\t\\tcode\\n\\t\\t\\t}\\n\\t\\t\\thints\\n\\t\\t}\\n\\t}\\n}\\n\",\"operationName\":\"getDailyProblem\"}"
headers = {
    "cookie": "csrftoken=R9HLriOs2cznMU05QFMLATNf1AXNrEQCXQNxzFI6xW8fSxheGf7X3bMy5eZyM60i; __cf_bm=2HExO3q8oYLg9nQ_OmOoqlIaO3NlH7JhFPW4CETdJz4-1723080506-1.0.1.1-.7m9k7YK67lNKGwzxPlkWYxAAuEN5ZLoBFUigcrx3uQa1rP3ix2BwO7vgCcnd2LgO1kx4pYeqIhhZZF4fcxDUQ",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, data=payload, headers=headers)

print("Pull response:", response)

question_response = response.json()['data']['activeDailyCodingChallengeQuestion']

link = question_response['link']
question_json = question_response['question']
full_title = f"{question_json['questionFrontendId']}. {question_json['title']}"

print("Full title:", full_title)

html_output = f"""<title>{full_title}</title><body><h1><a href="https://leetcode.com{link}">{question_json['title']}</a></h1>{
question_json['content']}{"".join([f"<br><details><summary>Hint {i + 1}</summary>{hint}</details>" for i, hint in enumerate(question_json['hints'])])}</body>"""

folder_path = f"./Python/unsolved/{full_title}"
if not os.path.exists(folder_path):
    os.mkdir(folder_path)
    print(f"Folder {folder_path} created")

    with open(f"{folder_path}/description.html", "w") as f:
        f.write(html_output)

    print("Description file created")

    python_script_output = next(x['code'] for x in question_json['codeSnippets'] if x['lang'] == 'Python3')

    with open(f"{folder_path}/solution.py", "w") as f:
        f.write(python_script_output)

    print("Script file created")
else:
    print("Folder already exists!")
