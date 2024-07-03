
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data provided
data = [
    {'Age Group': '0-12 years', 'Book Borrowing': '40%', 'Reference Materials': '20%', 'Study Room Usage': '10%', 'Computer Access': '5%', 'Events Attendance': '25%'},
    {'Age Group': '13-18 years', 'Book Borrowing': '35%', 'Reference Materials': '15%', 'Study Room Usage': '20%', 'Computer Access': '10%', 'Events Attendance': '20%'},
    {'Age Group': '19-25 years', 'Book Borrowing': '25%', 'Reference Materials': '15%', 'Study Room Usage': '25%', 'Computer Access': '20%', 'Events Attendance': '15%'},
    {'Age Group': '26-40 years', 'Book Borrowing': '20%', 'Reference Materials': '20%', 'Study Room Usage': '30%', 'Computer Access': '15%', 'Events Attendance': '15%'},
    {'Age Group': '41-55 years', 'Book Borrowing': '15%', 'Reference Materials': '30%', 'Study Room Usage': '15%', 'Computer Access': '20%', 'Events Attendance': '20%'},
    {'Age Group': '56-70 years', 'Book Borrowing': '10%', 'Reference Materials': '35%', 'Study Room Usage': '10%', 'Computer Access': '25%', 'Events Attendance': '20%'},
    {'Age Group': '71+ years', 'Book Borrowing': '5%', 'Reference Materials': '40%', 'Study Room Usage': '5%', 'Computer Access': '30%', 'Events Attendance': '20%'}
]

# Convert the data to a Pandas DataFrame and remove the '%' sign
df = pd.DataFrame(data)
df = df.set_index('Age Group')
df = df.applymap(lambda x: int(x.replace('%', '')))

# Calculate the cumulative sum of the proportions to stack them
cumulative_sum = df.cumsum(axis=1)

# Define the colors for the different categories
colors = sns.color_palette('pastel')[0:5]

# Plotting
fig, ax = plt.subplots(figsize=(10, 7))

# Initialize the bottom at zero for the start of the stacking process
bottom = None

# Loop through the columns to stack them
for column, color in zip(df.columns, colors):
    ax.bar(df.index, df[column], bottom=bottom, label=column, color=color)
    bottom = cumulative_sum[column]

# Add the legend
ax.legend(title='Services', bbox_to_anchor=(1.05, 1), loc='upper left')

# Customize the axes and title
ax.set_ylabel('Percentage')
ax.set_xlabel('Age Group')
ax.set_title('Library Service Usage by Age Group')

# Display the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()