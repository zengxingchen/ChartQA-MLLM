
import matplotlib.pyplot as plt

# Data
sports = ["Soccer", "Basketball", "Tennis", "Swimming", "Baseball", "Running", "Cycling", "Golf", "Boxing", "Skiing",
          "Gymnastics", "Volleyball", "Cricket", "Table Tennis", "Badminton", "Surfing", "Karate", "Wrestling",
          "Skateboarding", "Rock Climbing"]
popularity = [90, 85, 70, 75, 65, 95, 80, 60, 68, 72, 78, 88, 77, 83, 92, 64, 84, 82, 79, 63]

# Create horizontal bar chart
plt.figure(figsize=(12, 14))  # Width, Height of the chart
plt.barh(sports, popularity, color=['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD', '#8C564B', '#E377C2', 
                                   '#7F7F7F', '#BCBD22', '#17BECF', '#393B79', '#637939', '#8C6D31', '#843C39', 
                                   '#7B4173', '#6B6ECF', '#9C9EDE', '#A55194', '#CE6DBD', '#DE9ED6'], 
        height=0.5)  # Height of the bars

# Set the title and labels
plt.title('Popularity of Different Sports', pad=20)
plt.xlabel('Popularity Score')
plt.ylabel('Sport')

# Set y-axis limit
plt.xlim(60, 100)

# Show the plot
plt.tight_layout()
plt.show()