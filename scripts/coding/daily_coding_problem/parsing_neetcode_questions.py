from bs4 import BeautifulSoup
import json
from pathlib import Path
import os
from scripts.coding.daily_coding_problem import get_data_dir
from scripts.coding.daily_coding_problem.schemas import NeetCodeProblem
from scripts.utils.os import get_curr_dir

html_file_path = get_data_dir() / "neetcode-150-questions.html"

# Load and parse the HTML file
with open(html_file_path, "r") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")

# Extract problems
problems = []
categories = soup.find_all(
    "p", style="text-align: center; margin-top: 2em; margin-bottom: 0.6em"
)
tables = soup.find_all("tbody")

for category, table in zip(categories, tables):
    category_name = category.text.strip()
    rows = table.find_all("tr")

    for row in rows:
        problem_name = row.find("a", class_="table-text").text.strip()
        neet_code_link = (
            "https://neetcode.io" + row.find("a", class_="table-text")["href"]
        )
        leet_code_link = row.find("a", {"data-tooltip": "External Link"})["href"]
        difficulty = row.find("b").text.strip()

        # Create the NeetCodeProblem instance
        problem = NeetCodeProblem(
            name=problem_name,
            category=category_name,
            difficulty=difficulty,
            leet_code_link=leet_code_link,
            neet_code_link=neet_code_link,
        )

        problems.append(problem.model_dump())

problems_json = json.dumps(problems)

output_file_path = get_data_dir() / "neetcode-problems.json"
with open(output_file_path, "w") as f:
    f.write(problems_json)

print(f"Successfully extracted {len(problems)} problems to {output_file_path}")
