
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
future_tech_interest_score = [45, 50, 55, 60, 65, 70, 75, 74, 69, 63, 55, 48]

# Changes to data to enrich visualization
future_tech_interest_score[6] += 2  # July
future_tech_interest_score[-1] -= 3  # December

# Modify color scheme with color codes, change figure size, change trend by adjusting the scores
plt.figure(figsize=(12, 7))
plt.plot(months, [score - 10 if i % 2 == 0 else score + 10 for i, score in enumerate(future_tech_interest_score)], 
         color='#ff5733', marker='o')  # Adjusted trend with color code

# Adding labels with annotations
for i, (month, score) in enumerate(zip(months, future_tech_interest_score)):
    adjusted_score = score - 10 if i % 2 == 0 else score + 10
    plt.annotate(f'{score}', (month, adjusted_score), textcoords="offset points", xytext=(0,10), ha='center')

# Adding title and labels
plt.title('Monthly Interest Scores in Future Technologies')
plt.xlabel('Month')
plt.ylabel('Interest Score')

# Display chart
plt.show()