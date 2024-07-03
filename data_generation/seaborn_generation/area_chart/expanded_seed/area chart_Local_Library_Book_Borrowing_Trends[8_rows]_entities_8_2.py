
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Given data
data = [
    {'Month': 'January', 'Number of Books Borrowed': 1200},
    {'Month': 'February', 'Number of Books Borrowed': 1100},
    {'Month': 'March', 'Number of Books Borrowed': 1250},
    {'Month': 'April', 'Number of Books Borrowed': 1300},
    {'Month': 'May', 'Number of Books Borrowed': 1400},
    {'Month': 'June', 'Number of Books Borrowed': 1150},
    {'Month': 'July', 'Number of Books Borrowed': 950},
    {'Month': 'August', 'Number of Books Borrowed': 1050}
]

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)
# Ensure the Month column is of type category and ordered correctly since it represents time.
df['Month'] = pd.Categorical(df['Month'], 
                             categories=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August'], 
                             ordered=True)

# Plotting
sns.set_theme(style="whitegrid")  # Set the seaborn theme

# Create the lineplot
fig, ax = plt.subplots()
sns.lineplot(x='Month', y='Number of Books Borrowed', data=df, ax=ax, color="skyblue", lw=2)

# Fill the area under the line
plt.fill_between(df['Month'], df['Number of Books Borrowed'], color="skyblue", alpha=0.3)

# Customize the ticks and labels
ax.set_xticklabels(df['Month'], rotation=45)
ax.set_title("Number of Books Borrowed per Month")
ax.set_ylabel("Number of Books Borrowed")
ax.set_xlabel("Month")

# Show the plot
plt.tight_layout()
plt.show()