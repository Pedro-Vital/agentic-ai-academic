#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime

from coder.crew import Coder

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

assignment = """
Create a Python script that:

1. Generates a dataset of 50 random people with:
   - age (18-65)
   - salary (30000-120000)

2. Store the data in a pandas DataFrame.

3. Compute:
   - average age
   - average salary
   - correlation between age and salary

4. Save the dataset to 'output/data.csv'

5. Save a summary report to 'output/report.txt'

6. Print the summary to the console.
"""

def run():
    """
    Run the crew.
    """
    inputs = {
        'assignment': assignment,
    }
    
    result = Coder().crew().kickoff(inputs=inputs)
    print(result.raw)



