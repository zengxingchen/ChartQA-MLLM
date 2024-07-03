
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Table data as provided
data = [
    {'Month': 'January', 'Children (0-12)': 200, 'Teens (13-18)': 150, 'Adults (19-64)': 300, 'Seniors (65+)': 200},
    {'Month': 'February', 'Children (0-12)': 180, 'Teens (13-18)': 130, 'Adults (19-64)': 320, 'Seniors (65+)': 210},
    {'Month': 'March', 'Children (0-12)': 210, 'Teens (13-18)': 160, 'Adults (19-64)': 310, 'Seniors (65+)': 220},
    {'Month': 'April', 'Children (0-12)': 190, 'Teens (13-18)': 140, 'Adults (19-64)': 330, 'Seniors (65+)': 230},
    {'Month': 'May', 'Children (0-12)': 220, 'Teens (13-18)': 170, 'Adults (19-64)': 340, 'Seniors (65+)': 240},
    {'Month': 'June', 'Children (0-12)': 230, 'Teens (13-18)': 180, 'Adults (19-64)': 350, 'Seniors (65+)': 250},
    {'Month': 'July', 'Children (0-12)': 240, 'Teens (13-18)': 190, 'Adults (19-64)': 360, 'Seniors (65+)': 260},
    {'Month': 'August', 'Children (0-12)': 250, 'Teens (13-18)': 200, 'Adults (19-64)': 370, 'Seniors (65+)': 270},
    {'Month': 'September', 'Children (0-12)': 220, 'Teens (13-18)': 185, 'Adults (19-64)': 355, 'Seniors (65+)': 265},
    {'Month': 'October', 'Children (0-12)': 210, 'Teens (13-18)': 180, 'Adults (19-64)': 340, 'Seniors (65+)': 255},
    {'Month': 'November', 'Children (0-12)': 200, 'Teens (13-18)': 175, 'Adults (19-64)': 325, 'Seniors (65+)': 245},
    {'Month': 'December', 'Children (0-12)': 230, 'Teens (13-18)': 190, 'Adults (19-64)': 350, 'Seniors (65+)': 250}
]

# Transforming data into a DataFrame
df = pd.DataFrame(data)
# Ensure the 'Month' column is of type 'category'
df['Month'] = pd.Categorical(df['Month'], 
                             categories=['January', 'February', 'March', 'April', 'May', 'June', 
                                         'July', 'August', 'September', 'October', 'November', 'December'], 
                             ordered=True)

# The cumulative sum for stacking
df_cumsum = df.set_index('Month').cumsum(axis=1)

# Plotting
plt.figure(figsize=(10, 6))

# Colormap for the areas
colors = plt.get_cmap('Set1')

# Plot the areas
for i, column in enumerate(df.columns[1:]):
    plt.fill_between(df.index, df_cumsum[column], label=column, color=colors(i), alpha=0.5)

# Adding beautifying elements
plt.title('Monthly Demographic Distribution')
plt.xlabel('Month')
plt.ylabel('Number of People')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.legend(loc='upper left')
plt.tight_layout()  # Adjust for a nice fit

# Displaying the plot
plt.show()