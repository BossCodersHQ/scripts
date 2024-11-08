"""Script for producing a CSV file of problems to solve every day."""

import csv
import json
from collections import deque
from enum import Enum
from random import shuffle

from scripts.coding.daily_coding_problem import get_output_dir
from scripts.coding.daily_coding_problem.schemas import DifficultyLevel, NeetCodeProblem


def load_problems(file_path: str) -> list[NeetCodeProblem]:
    """Load problems from a JSON file."""
    with open(file_path, "r") as file:
        problems_json = json.load(file)
    problems = [NeetCodeProblem(**problem) for problem in problems_json]
    print(f"Successfully loaded {len(problems)} problems from {file_path}")
    return problems


def get_curr_problem_level(
    day: int, days_for_each_difficulty_level: int, num_difficulty_levels: int
) -> DifficultyLevel:
    """Get the current difficulty level based on the day."""
    return list(DifficultyLevel)[
        (day // days_for_each_difficulty_level) % num_difficulty_levels
    ]


# Load problems
problem_file_path = get_output_dir() / "neetcode-problems.json"
problems: list[NeetCodeProblem] = load_problems(problem_file_path)

# Generate interleaved practice sequence from easy to hard, across topics
days: list[NeetCodeProblem] = []
total_days = len(problems)
num_difficulty_levels = len(DifficultyLevel)

# Create dict of problems by category & difficulty level
problems_dict: dict[str, dict[DifficultyLevel, deque[NeetCodeProblem]]] = {}
for problem in problems:
    problems_dict.setdefault(problem.category, {}).setdefault(
        problem.difficulty, deque()
    ).appendleft(problem)

# Days allotted to each problem level
days_for_each_problem = 3

# Loop through each day and assign a problem
for day in range(total_days):
    # Determine the current difficulty level (easy, medium, hard)
    current_level = get_curr_problem_level(
        day=day,
        days_for_each_difficulty_level=days_for_each_problem,
        num_difficulty_levels=num_difficulty_levels,
    )

    # Shuffle categories to randomize the order of problems
    categories = list(problems_dict.keys())
    shuffle(categories)

    # Track if a problem was assigned for the current day
    assigned_problem = False

    # Attempt to add a problem for the current difficulty level
    for category in categories:
        difficulties = problems_dict[category]

        # Check if a problem is available at the current level, otherwise skip
        if current_level in difficulties and difficulties[current_level]:
            days.append(difficulties[current_level].pop())
            assigned_problem = True
            break

    # Fallback to other difficulty levels if no problem was found at the current level
    if not assigned_problem:
        for level in DifficultyLevel:
            if level != current_level:  # Skip the already-attempted current level
                for category in categories:
                    if (
                        level in problems_dict[category]
                        and problems_dict[category][level]
                    ):
                        days.append(problems_dict[category][level].pop())
                        assigned_problem = True
                        break
                if assigned_problem:
                    break

# Save to CSV file
csv_file_path = get_output_dir() / "neetcode_150_schedule.csv"
with open(csv_file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(
        [
            "Day",
            "Question Name",
            "Leet Code Link",
            "Neet Code Link",
            "Difficulty",
            "Category",
        ]
    )
    for day_index, problem in enumerate(days, start=1):
        writer.writerow(
            [
                day_index,
                problem.name,
                problem.leet_code_link,
                problem.neet_code_link,
                problem.difficulty.value,
                problem.category,
            ]
        )

print(f"Schedule saved to {csv_file_path}")
