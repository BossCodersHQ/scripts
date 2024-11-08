"""Script for producing a CSV file of problems to solve everyday."""

import csv
from enum import Enum
from scripts.coding.daily_coding_problem import get_data_dir
from scripts.coding.daily_coding_problem.schemas import DifficultyLevel, NeetCodeProblem
from scripts.utils.os import get_curr_dir
import json
from collections import deque
from random import shuffle

def load_problems(file_path: str) -> list[NeetCodeProblem]:
    """Load problems from a JSON file."""
    with open(file_path, "r") as file:
        problems_json = json.load(file)
    problems = [NeetCodeProblem(**problem) for problem in problems_json]
    print(f"Successfully loaded {len(problems)} problems from {file_path}")
    return problems


def get_curr_problem_level(day: int, days_for_each_difficulty_level:int, num_difficulty_levels: int) -> DifficultyLevel:
    """Get the current difficulty level based on the day."""
    return list(DifficultyLevel)[(day // days_for_each_difficulty_level) % num_difficulty_levels]


# Load problems
problem_file_path = get_data_dir() / "neetcode-problems.json"
problems: list[NeetCodeProblem] = load_problems(problem_file_path)

# Generate interleaved practice sequence from easy to hard, across topics
days: list[NeetCodeProblem] = []
total_days = len(problems)
num_difficulty_levels = len(DifficultyLevel)

# Create dict of problems by category & difficulty level
problems_dict: dict[str,dict[DifficultyLevel, NeetCodeProblem]] = {}
for problem in problems:
    problems_dict.setdefault(problem.category, {}).setdefault(problem.difficulty, deque()).appendleft(problem)

days_for_each_problem = 3


for day in range(total_days):

    # Determine the current difficulty level (easy, medium, hard)
    current_level = get_curr_problem_level(day=day, days_for_each_difficulty_level=days_for_each_problem, num_difficulty_levels=num_difficulty_levels)

    # Shuffle the categories to randomize the order of problems
    categories = list(problems_dict.keys())
    shuffle(categories)

    # Go through each category and try to add a problem of the current difficulty
    for category, difficulties in problems_dict.items():
        # Only proceed if there are problems left at the current difficulty level for this category
        if current_level in difficulties and difficulties[current_level]:
            print(f"Day {day+1}/{total_days}")
            days.append(difficulties[current_level].pop())
            break  # Move to the next day after adding one problem


# Save to CSV file
csv_file_path = get_data_dir() / "neetcode_150_schedule.csv"
with open(csv_file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Day", "Question Name", "Leet Code Link", "Neet Code Link", "Difficulty", "Category"])
    for day, problem in enumerate(days, start=1):
        writer.writerow([day, problem.name, problem.leet_code_link, problem.neet_code_link, problem.difficulty.value, problem.category])
