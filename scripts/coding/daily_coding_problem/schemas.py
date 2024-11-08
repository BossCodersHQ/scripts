from enum import Enum
from pydantic import BaseModel
from typing import Literal


class DifficultyLevel(str, Enum):
    """Difficulty levels for coding problems."""
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"


class BaseProblem(BaseModel):
    """Base class for coding problems."""
    name: str
    category: str
    difficulty: DifficultyLevel


class LeetCodeProblem(BaseProblem):
    """Class for LeetCode problems."""
    leet_code_link: str


class NeetCodeProblem(LeetCodeProblem):
    """Class for NeetCode problems."""
    neet_code_link: str

if __name__ == "__main__":
    print(DifficultyLevel(2))
