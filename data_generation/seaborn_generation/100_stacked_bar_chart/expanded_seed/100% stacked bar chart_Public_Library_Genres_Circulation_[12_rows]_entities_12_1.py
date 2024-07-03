
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Given data
data = [
    {'Month': 'January', 'Fiction (%)': 30, 'Non-Fiction (%)': 20, "Children's Books (%)": 25, 'Young Adult (%)': 15, 'Periodicals (%)': 5, 'E-Books (%)': 5},
    {'Month': 'February', 'Fiction (%)': 25, 'Non-Fiction (%)': 25, "Children's Books (%)": 25, 'Young Adult (%)': 15, 'Periodicals (%)': 5, 'E-Books (%)': 5},
    {'Month': 'March', 'Fiction (%)': 35, 'Non-Fiction (%)': 15, "Children's Books (%)": 20, 'Young Adult (%)': 20, 'Periodicals (%)': 5, 'E-Books (%)': 5},
    # ... (add the rest of the months here)
    {'Month': 'December', 'Fiction (%)': 30, 'Non-Fiction (%)': 20, "Children's Books (%)": 25, 'Young Adult (%)': 15, 'Periodicals (%)': 5, 'E-Books (%)': 5}
]

# Create a DataFrame
df = pd.DataFrame(data)

# Set the 'Month' column as index
df.set_index('Month', inplace=True)

# Normalize the data to get the percentage of each category for each month
df_normalized = df.div(df.sum(axis=1), axis=0)

# Define the bottom position for each stack
bottom = pd.Series([0]*df_normalized.shape[0], index=df_normalized.index)

# Color palette for consistency
palette = sns.color_palette("husl", len(df.columns))

# Plot bar chart
plt.figure(figsize=(10, 6))  # Set the figure size

for i, col in enumerate(df.columns):
    sns.barplot(x=df_normalized.index, y=df_normalized[col], label=col, color=palette[i], bottom=bottom)
    bottom += df_normalized[col]

# Decorate the plot
plt.xticks(rotation=45)
plt.ylabel('Percentage')
plt.title('Percentage Distribution of Book Sales by Category')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # Place legend outside the plot

plt.tight_layout()
plt.show()