
import matplotlib.pyplot as plt

# Data
quarters = ['Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021', 
            'Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022']
research = [80, 85, 90, 95, 100, 105, 110, 115]
development = [60, 65, 70, 75, 80, 85, 90, 95]
marketing = [70, 75, 80, 85, 90, 95, 100, 105]
sales = [90, 95, 100, 105, 110, 115, 120, 125]

# Colors
colors_research = '#e41a1c'
colors_development = '#377eb8'
colors_marketing = '#4daf4a'
colors_sales = '#ff7f00'

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))  # Change the figure size

bar_width = 0.35  # Change the width of the bars

ax.bar(quarters, research, bar_width, label='Research', color=colors_research)
ax.bar(quarters, development, bar_width, bottom=research, label='Development', color=colors_development)
ax.bar(quarters, marketing, bar_width, bottom=[i+j for i,j in zip(research, development)], label='Marketing', color=colors_marketing)
ax.bar(quarters, sales, bar_width, bottom=[i+j+k for i,j,k in zip(research, development, marketing)], label='Sales', color=colors_sales)

ax.set_ylabel('Budget (Million USD)')
ax.set_title('Departmental Budget Allocation Over Two Years')
ax.set_xlabel('Quarters')
ax.legend()

plt.tight_layout()
plt.show()