
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Grade Level": ["Elementary", "Middle School", "High School", "Undergraduate", "Graduate", "Postgraduate"],
    "Average Study Hours per Week": [10.2, 12.8, 15.6, 18.4, 20.5, 22.7]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 8))
sns.set_theme(style="whitegrid")
ax = sns.barplot(
    x="Average Study Hours per Week",
    y="Grade Level",
    data=df,
    palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"],
    dodge=False,
    orient="h"
)

for bar in ax.patches:
    bar.set_height(0.7)

ax.set_xlabel("Average Study Hours per Week")
ax.set_title("Average Study Hours per Week by Grade Level")

plt.show()