# Week 1: Operations Analyzer

A beginner-friendly Python project that demonstrates core programming concepts through operational performance analysis of fuel depots.

## Project Overview

This is my first Python assignment in the Data Analytics and AI program. The project analyzes operational performance by comparing actual output against target output for fuel depot operations. I developed this in Jupyter Notebook to calculate efficiency percentages and automatically classify each depot's operational status as **Normal**, **Warning**, or **Critical** based on performance thresholds.

The assignment showcases how Python functions, data structures, and control flow can be combined to build a reusable reporting system—a foundational skill in data analysis and operational intelligence.

## Objectives

I implemented this project to achieve the following learning goals:

- **Calculate operational efficiency** using the formula: `(Actual Output / Target Output) × 100`
- **Classify operational status** into three categories based on efficiency thresholds
- **Store depot information** using Python dictionaries to organize structured data
- **Process multiple records** using loops to automate report generation
- **Generate formatted output** with visual indicators for quick status scanning
- **Build reusable functions** that can be applied to any depot dataset

## Python Concepts Demonstrated

This project demonstrates the following fundamental Python concepts:

- **Functions** – Encapsulating logic into reusable `calculate_efficiency()` and `get_operational_status()` functions
- **Dictionaries** – Structuring depot data with nested key-value pairs for organized storage
- **Loops** – Using `for` loops to iterate through multiple depots and apply calculations
- **Conditional Statements** – Using `if/elif/else` to classify performance into status categories
- **Formatted Output** – Creating readable reports with f-strings and emoji indicators
- **Basic KPI Calculations** – Computing efficiency percentages and comparing against thresholds

## Project Structure

```
week1-operations-analyzer/
├── week1_ops_analyzer.ipynb
└── README.md
```

## How the Program Works

The program follows a logical sequence:

### 1. Define Operational Data
I created a dictionary called `depots` that stores actual and target output for three fuel depots (Nairobi, Nakuru, and Mombasa). Each depot is a key with a nested dictionary containing `actual_output` and `target_output` values.

```python
depots = {
    "Nairobi Depot": {
        "actual_output": 800,
        "target_output": 1000
    },
    "Nakuru Depot": {
        "actual_output": 400,
        "target_output": 1000
    },
    "Mombasa Depot": {
        "actual_output": 950,
        "target_output": 1000
    }
}
```

### 2. Calculate Efficiency
The `calculate_efficiency()` function computes how well each depot performed:

```
Efficiency = (Actual Output / Target Output) × 100
```

The result is rounded to 2 decimal places for clean reporting. The function also handles edge cases (e.g., zero target output) to prevent crashes.

### 3. Determine Operational Status
The `get_operational_status()` function classifies efficiency into three performance bands:

- **< 70%** → "critical" (urgent attention needed)
- **70–89%** → "warning" (below target, monitor closely)
- **≥ 90%** → "normal" (performing as expected)

### 4. Process Each Depot
A `for` loop iterates through the depots dictionary, extracts the actual and target values, calculates efficiency, and determines status for each depot.

### 5. Generate Formatted Report
For each depot, the program prints a clean, visually-organized report with emojis as status indicators:
- 🟢 Green circle for "normal"
- 🟡 Yellow circle for "warning"
- 🔴 Red circle for "critical"

## Example Output

Running the program produces the following output:

```
🏭 Depot = Nairobi Depot
  📦 Actual Output  = 800
  🎯 Target Output  = 1000
  ⚡ Efficiency     = 80.0%
  🟡 Status         = warning

🏭 Depot = Nakuru Depot
  📦 Actual Output  = 400
  🎯 Target Output  = 1000
  ⚡ Efficiency     = 40.0%
  🔴 Status         = critical

🏭 Depot = Mombasa Depot
  📦 Actual Output  = 950
  🎯 Target Output  = 1000
  ⚡ Efficiency     = 95.0%
  🟢 Status         = normal
```

This output provides instant visual feedback on each depot's performance, making it easy to identify which facilities need attention.

## Learning Outcomes

Through developing this project, I learned:

- **Function design** – How to break complex problems into smaller, reusable functions
- **Data structuring** – How to organize related information using dictionaries and nested data structures
- **Control flow** – How loops and conditionals work together to process data and make decisions
- **Code reusability** – How writing functions once allows them to be applied to datasets of any size
- **Operational reporting** – How to transform raw data into human-readable, actionable insights
- **Edge case handling** – How to anticipate and prevent errors (e.g., division by zero)

This assignment demonstrates that Python can be used to automate routine analysis tasks and produce professional reports—skills directly applicable to real-world data analysis and business intelligence roles.

---

**Assignment Context:** Week 1 of the Data Analytics and AI program (DICEE)  
**Language:** Python 3  
**Environment:** Jupyter Notebook

