
import matplotlib.pyplot as plt

# Data
years = ['2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028']
company_a_sales = [450, 470, 480, 500, 520, 540, 560, 580, 600, 620, 640]
company_b_sales = [300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500]
company_c_sales = [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]

# Colors
colors_a = ['#3498DB', '#2ECC71', '#9B59B6', '#E74C3C', '#F1C40F', '#34495E', '#1ABC9C', '#E67E22', '#7D3C98', '#5DADE2', '#AF7AC5']
colors_b = ['#1F618D', '#27AE60', '#8E44AD', '#C0392B', '#D4AC0D', '#2C3E50', '#148F77', '#CA6F1E', '#512E5F', '#2874A6', '#9B59B6']
colors_c = ['#2874A6', '#1F618D', '#2ECC71', '#D4AC0D', '#F1C40F', '#2C3E50', '#1ABC9C', '#E67E22', '#E74C3C', '#3498DB', '#7D3C98']

# Plot
fig, ax = plt.subplots(figsize=(14, 10))

bar_width = 0.6

bars_a = plt.bar(years, company_a_sales, color=colors_a, edgecolor='white', width=bar_width, label='Company A')
bars_b = plt.bar(years, company_b_sales, bottom=company_a_sales, color=colors_b, edgecolor='white', width=bar_width, label='Company B')
bars_c = plt.bar(years, company_c_sales, bottom=[i+j for i,j in zip(company_a_sales, company_b_sales)], color=colors_c, edgecolor='white', width=bar_width, label='Company C')

# Adding labels and title
plt.ylabel('Revenue (in thousands)')
plt.title('Annual Revenue Comparison between Company A, B, and C', pad=20)

# Adding numerical labels
for bar in bars_a:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2.0, height / 2, '%d' % int(height), ha='center', va='center', color='white', fontsize=8)
for bar in bars_b:
    height = bar.get_height() + bar.get_y()
    ax.text(bar.get_x() + bar.get_width() / 2.0, height - bar.get_height() / 2, '%d' % int(height - bar.get_y()), ha='center', va='center', color='white', fontsize=8)
for bar in bars_c:
    height = bar.get_height() + bar.get_y()
    ax.text(bar.get_x() + bar.get_width() / 2.0, height - bar.get_height() / 2, '%d' % int(height - bar.get_y()), ha='center', va='center', color='white', fontsize=8)

# Customizing the axes
plt.ylim(0, 1500)

# Adding legend
plt.legend(loc='upper left')

# Display the plot
plt.show()