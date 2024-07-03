
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt 

# Data points
data = {
    'Sport': ['Soccer', 'Basketball', 'Tennis', 'Swimming', 'Athletics', 'Cycling', 'Gymnastics', 'Rowing', 'Boxing', 
              'Weightlifting', 'Wrestling', 'Skiing', 'Snowboarding', 'Hockey', 'Rugby', 'Martial_Arts', 'Fencing', 
              'Golf', 'Cricket', 'Baseball', 'Volleyball', 'Badminton', 'Table_Tennis', 'Surfing', 'Skateboarding', 
              'Rock_Climbing', 'Horse_Riding', 'Sailing', 'Archery', 'Diving'],
    'Average_Training_Hours': [18, 20, 15, 22, 17, 19, 24, 21, 23, 16, 18, 14, 15, 20, 21, 22, 13, 12, 16, 19, 18, 14, 13, 20, 
                               15, 16, 18, 19, 12, 21],
    'Average_Performance_Score': [88, 85, 87, 90, 86, 89, 92, 91, 93, 84, 88, 82, 83, 87, 86, 90, 80, 78, 85, 88, 86, 81, 79, 
                                  84, 83, 85, 87, 86, 77, 89]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set up the matplotlib figure
plt.figure(figsize=(16, 12))

# Draw a seaborn scatter plot
sb.scatterplot(data=df, x="Average_Training_Hours", y="Average_Performance_Score", palette=['#FF6347', '#4682B4'], s=100)

# Additional customizations
plt.title('Average Training Hours and Performance Scores of Athletes', pad=20)
plt.xlabel('Average Training Hours')
plt.ylabel('Average Performance Score')
plt.grid(True)

# Show the plot
plt.show()