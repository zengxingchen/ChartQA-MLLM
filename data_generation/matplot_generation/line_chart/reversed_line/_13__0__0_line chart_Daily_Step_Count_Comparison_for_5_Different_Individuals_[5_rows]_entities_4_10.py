
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
investment_growth = [65, 70, 60, 55, 50, 45, 48, 50, 55, 58, 62, 60]

# Modify data points for richer visualization
investment_growth[2] += 5  # March
investment_growth[9] -= 4  # October

# Color scheme with specific color codes
plt.figure(figsize=(14, 8))
plt.plot(months, [score - 5 if i % 2 == 0 else score + 5 for i, score in enumerate(investment_growth)], 
         color='#3498db', marker='o')  # Adjusted trend with color code

# Adding labels with annotations
for i, (month, score) in enumerate(zip(months, investment_growth)):
    adjusted_score = score - 5 if i % 2 == 0 else score + 5
    plt.annotate(f'{score}', (month, adjusted_score), textcoords="offset points", xytext=(0,10), ha='center')

# Adding title and labels
plt.title('Monthly Investment Growth (%) in 2023')
plt.xlabel('Month')
plt.ylabel('Investment Growth (%)')

# Display chart
plt.gca().invert_yaxis()  # Invert y-axis
plt.show()