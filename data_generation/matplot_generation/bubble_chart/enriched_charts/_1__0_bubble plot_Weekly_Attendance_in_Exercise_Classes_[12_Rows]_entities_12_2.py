
import matplotlib.pyplot as plt
import pandas as pd

# Step 1: Define the table data as pandas DataFrame
data = {
    "Age Group": ["13-18", "13-18", "13-18", "19-25", "19-25", "19-25", 
                  "26-35", "26-35", "26-35", "36-45", "36-45", "36-45",
                  "46-55", "46-55", "46-55", "56+", "56+", "56+"],
    "Hours per week": [5, 7, 4, 6, 8, 5, 7, 10, 6, 5, 7, 4, 4, 5, 3, 3, 4, 2],
    "Number of Participants": [300000, 450000, 200000, 500000, 600000, 300000, 
                               400000, 550000, 350000, 250000, 300000, 200000,
                               150000, 200000, 100000, 80000, 100000, 50000],
    "Hobby": ["Reading", "Video Games", "Music", "Reading", 
              "Video Games", "Music", "Reading", "Video Games", 
              "Music", "Reading", "Video Games", "Music", 
              "Reading", "Video Games", "Music", "Reading", 
              "Video Games", "Music"]
}
df = pd.DataFrame(data)

# Step 2: Prepare the color mapping
hobby_colors = {
    'Reading': '#FF5733',
    'Video Games': '#33FF57',
    'Music': '#3357FF'
}

# Step 3: Generate the bubble chart
plt.figure(figsize=(16, 10))  # Change width and height reasonably
for hobby in df['Hobby'].unique():
    subset = df[df['Hobby'] == hobby]
    plt.scatter(
        subset['Age Group'], 
        subset['Hours per week'], 
        s=subset['Number of Participants']/1000,  # Bubble sizes
        alpha=0.6,
        color=hobby_colors[hobby],
        label=hobby
    )

# Step 4: Chart formatting and topic/headline changes
plt.title('Weekly Hours Spent on Various Hobbies by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Hours per Week')
plt.legend(title='Hobby')
plt.grid(True)
plt.show()