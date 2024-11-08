# Daily Coding Problem Practice Schedule Generator

This module provides scripts to parse and generate a daily practice schedule for NeetCode problems. The workflow involves two main scripts:

1. `parsing_neetcode_questions.py`: Parses the NeetCode questions from an HTML file and generates a JSON file.
2. `generate_problems_csv.py`: Generates a CSV file with a daily practice schedule based on the parsed questions.

It also involves the following assets:

- `neetcode_questions.html`: HTML file containing the NeetCode questions scraped using developer tools and a shoddy regex😁😅.
- `email-template.html`: HTML template for the daily practice schedule email.

## Workflow

### Step 1: Parse NeetCode Questions

First, use the `parsing_neetcode_questions.py` script to parse the NeetCode questions from the HTML file and generate a JSON file.

### Step 2: Generate Daily Practice Schedule

Next, use the `generate_problems_csv.py` script to generate a CSV file with a daily practice schedule.

## Question Ordering Strategy

The question order is designed to maximize learning retention by leveraging interleaved practice, as recommended in the book *Make It Stick*. Rather than practicing problems in a blocked, topic-by-topic format, this method introduces variety by “darting” between topics daily, encouraging a deeper understanding and stronger recall of concepts over time.

### Daily Practice Schedule Generation

1. **Difficulty Progression**: Each month progresses from easy to hard questions to build a strong foundation before tackling complex problems.
2. **Randomized Categories**: Topics are shuffled daily to avoid repeating the same topic on consecutive days, enhancing adaptive learning.
3. **Difficulty Fallbacks**: If no questions are available at the scheduled difficulty level, the system automatically falls back to the nearest difficulty, ensuring continuity.

This interleaved, adaptive approach is shown to be more effective for long-term retention compared to traditional blocked practice, as highlighted in *Make It Stick*.
