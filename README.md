# Text Analyzer

## Overview
Text Analyzer is a Python application developed for the CS 006: Algorithms and Complexity course. It demonstrates practical use of different algorithmic paradigms to perform text analysis tasks.

### Student Outcomes
- **SO (1):** Analyze computing problems and identify algorithmic solutions.
- **SO (6):** Apply computer science theory and software development fundamentals.

## Features
1. **Count Word Occurrences (Brute Force)**
2. **Common Words (Divide & Conquer)**
3. **Longest Common Subsequence (Dynamic Programming)**

## Project Instructions
This project fulfills the CS 006 final project requirements:
- Group of 3–4 members
- Implement at least 3 algorithms:
  - Brute Force Algorithm
  - Divide and Conquer Algorithm
  - Dynamic Programming
  - (Optionally more: Greedy, Backtracking, Randomized, String Algorithms, etc.)
- Prepare a PowerPoint presentation and documentation
- Submit PPT and documentation under a folder named with your team name

## Getting Started
### Prerequisites
- Python 3.7+
- Install dependencies:

```
pip install pyfiglet
```

### Usage

```bash
python main.py
```

Follow the on-screen menu to select an operation and provide input texts.

## Project Structure
```
text-analyzer/
├── brute_force.py      # Brute-force substring search
├── compare_dc.py       # Divide & conquer common-word finder
├── lcs_dp.py           # Dynamic programming LCS implementation
├── utils.py            # Text cleaning and tokenization utilities
├── main.py             # Entry point with menu interface
└── README.md           # Project documentation
```

## Components
- **Title:** Text Analyzer
- **Introduction:** A tool to explore algorithmic approaches to text processing.
- **Objectives:** 
  - Demonstrate algorithm design paradigms
  - Provide a clear, interactive text analysis tool
- **Analysis:** Each module highlights strengths and trade-offs of its algorithmic approach.
