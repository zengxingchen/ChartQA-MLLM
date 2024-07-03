
import seaborn as sns
import matplotlib.pyplot as plt

# Your provided data
data = [
    {'Year': 2017, 'Espresso': 12000, 'Lattes': 18000, 'Cappuccinos': 9500, 'Americanos': 11000},
    {'Year': 2018, 'Espresso': 12500, 'Lattes': 19000, 'Cappuccinos': 10000, 'Americanos': 11500},
    {'Year': 2019, 'Espresso': 13000, 'Lattes': 20000, 'Cappuccinos': 10500, 'Americanos': 12000},
    {'Year': 2020, 'Espresso': 13500, 'Lattes': 20500, 'Cappuccinos': 11000, 'Americanos': 12500}
]

# Convert to DataFrame
import pandas as pd
df = pd.DataFrame(data)

# We need to transform this DataFrame into a 'long-form' or 'tidy' structure.
df = df.set_index('Year')
df = df.stack().reset_index()
df.columns = ['Year', 'Coffee_Type', 'Sales']

# Sort the DataFrame based on the 'Coffee_Type' to make sure the fill works correctly
df = df.sort_values(by='Coffee_Type')

# Create the area plot
sns.set(style="whitegrid")

# Establish the colors for the stack
palette = sns.color_palette("husl", 5)

# Now, we create the area plot using Matplotlib's `fill_between`
fig, ax = plt.subplots(figsize=(10, 6))

# Starting point for the cumulative sum
prev_values = df['Year'].map(df.groupby('Year')['Sales'].sum()).values / 2
cum_values = prev_values.copy()

# Loop through each coffee type and build the layers of the area chart
for i, coffee_type in enumerate(df['Coffee_Type'].unique()):
    coffee_data = df[df['Coffee_Type'] == coffee_type]
    values = coffee_data['Sales'].values
    ax.fill_between(coffee_data['Year'], cum_values - prev_values, cum_values - prev_values + values, label=coffee_type, color=palette[i])
    cum_values += values - prev_values

# Customizing the plot's aesthetics
ax.set_title("Sales of Coffee Types Over Years")
ax.set_ylabel("Number of Sales")
ax.set_xlabel("Year")
ax.legend(title='Coffee Type')

# Display the plot
plt.tight_layout()
plt.show()