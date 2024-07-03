
import matplotlib.pyplot as plt

# Data for plotting
categories = ["Marketing", "Research", "Production", "HR", "Sales", "IT", 
              "Customer Service", "Logistics", "Finance", "Legal", "PR", "Administration"]
values = [35000, 45000, 80000, 25000, 75000, 62000, 33000, 54000, 47000, 38000, 29000, 31000]

fig, ax = plt.subplots(figsize=(10, 12))

# Create a vertical bar chart with custom colors and bar widths
bars = ax.bar(categories, values, width=0.5,
              color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b',
                     '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e'])

# Set the chart title and labels
ax.set_title('Departmental Budgets (in $)', fontsize=18)
ax.set_xlabel('Departments', fontsize=14)
ax.set_ylabel('Budget (in $)', fontsize=14)

# Customize the ticks on both axes
ax.xaxis.set_tick_params(labelsize=12, rotation=45)
ax.yaxis.set_tick_params(labelsize=12)

# Add value labels to each bar
for bar in bars:
    height = bar.get_height()
    label_y_pos = height + 1000  # Some padding to the top
    ax.text(bar.get_x() + bar.get_width()/2, label_y_pos, f'${height}',
            va='center', ha='center', fontsize=12, rotation=90)

plt.tight_layout()
plt.show()