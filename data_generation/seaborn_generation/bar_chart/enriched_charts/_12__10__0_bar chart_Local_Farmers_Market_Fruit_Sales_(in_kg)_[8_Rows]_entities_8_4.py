
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Topic": ["Algebra", "Geometry", "Calculus", "Statistics", "Trigonometry", 
              "Probability", "Linear Algebra", "Discrete Math", "Number Theory", 
              "Abstract Algebra", "Complex Analysis", "Differential Equations"],
    "Amount": [45, 30, 25, 20, 15, 10, 5, 8, 12, 9, 6, 7]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 12))
sns.set_theme(style="whitegrid")
ax = sns.barplot(
    x="Amount",
    y="Topic",
    data=df,
    palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", 
             "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", 
             "#aec7e8", "#ffbb78"],
    dodge=False)

for bar in ax.patches:
    bar.set_height(0.6)

ax.set_xlabel("Number of Students Enrolled")
ax.set_title("Enrollment in Different Mathematics Topics")

plt.show()