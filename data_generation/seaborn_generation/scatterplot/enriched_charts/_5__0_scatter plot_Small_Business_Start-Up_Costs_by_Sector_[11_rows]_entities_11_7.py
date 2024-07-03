
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt 

# Data points
data = {
    'University': ['Harvard', 'Stanford', 'MIT', 'Caltech', 'Princeton', 'Yale', 'Columbia', 'UChicago', 'UPenn', 'Brown', 
                   'Cornell', 'Duke', 'Northwestern', 'Johns_Hopkins', 'Dartmouth', 'Vanderbilt', 'Rice', 'Notre_Dame', 
                   'WashU', 'Georgetown'],
    'Average_Study_Hours': [24.5, 22.1, 25.0, 26.3, 23.7, 21.5, 24.2, 23.0, 22.8, 20.9, 24.0, 23.3, 21.7, 22.3, 20.5, 
                            21.8, 23.1, 22.6, 22.9, 21.4],
    'Average_GPA': [3.8, 3.7, 3.9, 3.85, 3.82, 3.75, 3.76, 3.73, 3.78, 3.7, 3.74, 3.77, 3.72, 3.79, 3.68, 3.71, 3.76, 
                    3.74, 3.75, 3.7]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set up the matplotlib figure
plt.figure(figsize=(14, 10))

# Draw a seaborn scatter plot
sb.scatterplot(data=df, x="Average_Study_Hours", y="Average_GPA", palette=['#FF4500', '#1E90FF'], s=100)

# Additional customizations
plt.title('Average Study Hours and GPA of Students in U.S. Universities')
plt.xlabel('Average Study Hours')
plt.ylabel('Average GPA')
plt.grid(True)

# Show the plot
plt.show()