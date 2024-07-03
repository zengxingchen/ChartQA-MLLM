
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
happiness_score = [55, 58, 62, 60, 66, 70, 68, 64, 61, 67, 69, 65]

# Changes to data to enrich visualization
happiness_score[4] += 2  # May
happiness_score[-3] -= 2  # October

# Modify color scheme with color codes, change figure size, change trend by adjusting the scores
plt.figure(figsize=(14, 8))
plt.plot(months, [score - 5 if i % 2 == 0 else score + 5 for i, score in enumerate(happiness_score)], 
         color='#3498db', marker='o', linestyle='--')  # Adjusted trend with color code

# Adding labels with annotations
for i, (month, score) in enumerate(zip(months, happiness_score)):
    adjusted_score = score - 5 if i % 2 == 0 else score + 5
    plt.annotate(f'{score}', (month, adjusted_score), textcoords="offset points", xytext=(0,10), ha='center')

# Adding title and labels
plt.title('Monthly Happiness Scores in 2023')
plt.xlabel('Month')
plt.ylabel('Happiness Score')

# Display chart
plt.show()