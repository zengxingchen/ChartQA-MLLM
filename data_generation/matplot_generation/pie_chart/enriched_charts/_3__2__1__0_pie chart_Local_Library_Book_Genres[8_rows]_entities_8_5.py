
import matplotlib.pyplot as plt

# Data points
age_groups = [
    '0-9', '10-19', '20-29', '30-39', '40-49',
    '50-59', '60-69', '70-79', '80+'
]

percentage = [
    9.0, 14.0, 21.0, 17.0, 13.0,
    11.0, 7.0, 5.0, 3.0
]

# Colors for each section
colors = [
    '#ff6347', '#4682b4', '#32cd32', '#ffa07a', '#9370db',
    '#ee82ee', '#98fb98', '#afeeee', '#ffd700'
]

# Resize the chart
plt.figure(figsize=(12, 8))

# Create the pie chart
plt.pie(percentage, labels=age_groups, colors=colors, autopct='%1.1f%%', startangle=140)

# Set the title
plt.title('Health & Psychology: Age Distribution of Survey Respondents in 2023', fontsize=16, pad=20)

# Display the chart
plt.show()