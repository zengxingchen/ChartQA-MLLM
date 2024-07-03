
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
science_score = [75, 72, 78, 74, 80, 77, 79, 76, 82, 78, 81, 77]

# Changes to data to enrich visualization
science_score[2] += 3  # March
science_score[-4] -= 2  # September

# Modify color scheme with color codes, change figure size, change trend by adjusting the scores
plt.figure(figsize=(16, 10))
plt.plot(months, science_score, color='#e74c3c', marker='o', linestyle='-')

# Adding labels with annotations
for i, (month, score) in enumerate(zip(months, science_score)):
    plt.annotate(f'{score}', (month, score), textcoords="offset points", xytext=(0,10), ha='center')

# Adding title and labels
plt.title('Monthly Science Scores in 2023')
plt.xlabel('Month')
plt.ylabel('Science Score')

# Invert Y-axis
plt.gca().invert_yaxis()

# Display chart
plt.show()