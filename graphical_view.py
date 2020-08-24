#creates pie chart for verdicts and tags
from matplotlib import pyplot as plt
from user_problem_submission import search

verdict, tags = search()

fig = plt.figure(figsize=(8,8))
plt.pie([float(v) for v in verdict.values()], labels=[k for k in verdict.keys()])
plt.show()
plt.pie([float(v) for v in tags.values()], labels=[k for k in tags.keys()])
plt.show()
