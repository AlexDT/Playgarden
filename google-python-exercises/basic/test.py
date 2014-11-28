lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# Add your function below!
students = [lloyd, alice, tyler]

def average(lst):
  count = 0
  sum_lst = 0
  for i in lst:
    count += 1
    sum_lst += float(i)
  return (sum_lst / count)

def get_average(stud):
  avg_homework = average(stud["homework"])
  avg_quizzes = average(stud["quizzes"])
  avg_tests = average(stud["tests"])
  return (avg_homework * 0.10 + avg_quizzes * 0.30 + avg_tests

   * 0.60)

for name in students:
  print name["name"]
  print get_average(name)
  print "\n"

# ------------

import os

for fn in os.listdir("."):
  if fn == "alex.txt":
    os.rename(fn, "alice.txt")