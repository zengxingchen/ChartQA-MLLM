
import matplotlib.pyplot as plt

# Data
quarters = ['Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021', 
            'Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022']
company_a_revenue = [120, 135, 140, 155, 160, 165, 170, 180]
company_b_revenue = [150, 160, 165, 170, 180, 190, 195, 200]
company_c_revenue = [130, 145, 150, 160, 170, 175, 180, 190]

# Colors
colors_a = '#1f77b4'
colors_b = '#ff7f0e'
colors_c = '#2ca02c'

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))  # Change the figure size

bar_width = 0.5  # Change the width of the bars
bar_spacing = 0.15  # Change the spacing between the bars

y_positions = range(len(quarters))
bar_positions_a = [pos - bar_width / 2 - bar_spacing / 2 for pos in y_positions]
bar_positions_b = y_positions
bar_positions_c = [pos + bar_width / 2 + bar_spacing / 2 for pos in y_positions]

ax.barh(bar_positions_a, company_a_revenue, bar_width, label='Company A', color=colors_a)
ax.barh(bar_positions_b, company_b_revenue, bar_width, left=company_a_revenue, label='Company B', color=colors_b)
ax.barh(bar_positions_c, company_c_revenue, bar_width, left=[x + y for x, y in zip(company_a_revenue, company_b_revenue)], label='Company C', color=colors_c)

ax.set_xlabel('Revenue (Million USD)')
ax.set_title('Quarterly Revenue of Tech Companies Over Two Years')
ax.set_yticks(y_positions)
ax.set_yticklabels(quarters)
ax.legend()

plt.tight_layout()
plt.show()