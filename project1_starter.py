import ast
from functions import combineDailyActive

# Declare variables first before initializing them to each line in input.txt
var1 = []
var2 = []
var3 = []
var4 = []
var5 = 0
dailyActive = []
available_times = []

# Open the input.txt file
with open(
    "input.txt") as file:  # Initialize each line in input.txt to var1-var5
  x = 1
  testCaseCount = 1
  for line in file:
    if line == "\n":
      x = 1
      continue
    exec(f'var{x} = line')