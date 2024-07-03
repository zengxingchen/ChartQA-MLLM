
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Convert the table data into a pandas DataFrame
data = [{'Brand': 'Apple', 'Market Share (%)': 30.0},
        {'Brand': 'Samsung', 'Market Share (%)': 25.0},
        {'Brand': 'Xiaomi', 'Market Share (%)': 10.0},
        {'Brand': 'Huawei', 'Market Share (%)': 8.0},
        {'Brand': 'OnePlus', 'Market Share (%)': 5.0},
        {'Brand': 'Google Pixel', 'Market Share (%)': 3.0},
        {'Brand': 'Motorola', 'Market Share (%)': 4.0},
        {'Brand': 'Nokia', 'Market Share (%)': 2.0},
        {'Brand': 'Sony', 'Market Share (%)': 1.0},
        {'Brand': 'LG', 'Market Share (%)': 1.0},
        {'Brand': 'HTC', 'Market Share (%)': 0.5},
        {'Brand': 'Others', 'Market Share (%)': 10.5}]

df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Create a color palette to diversify the bars' colors
palette = sns.color_palette("hsv", len(df))

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(10, 6))

# Plot the market share for each brand using a barplot
sns.barplot(x="Market Share (%)", y="Brand", data=df,
            label="Total", palette=palette)

# Add a legend and informative axis label
ax.set(xlim=(0, 35), ylabel="",
       xlabel="Market Share (%)")
plt.title('Smartphone Brand Market Share (%)')
sns.despine(left=True, bottom=True)

# Show the plot
plt.show()