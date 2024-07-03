
import matplotlib.pyplot as plt
import seaborn as sns
import squarify

# Your provided data
data = [
    {'Mode': 'Subway', 'Percent_of_Commuters': 30, 'City': 'New York'},
    {'Mode': 'Bus', 'Percent_of_Commuters': 25, 'City': 'New York'},
    {'Mode': 'Bicycle', 'Percent_of_Commuters': 5, 'City': 'New York'},
    {'Mode': 'Car', 'Percent_of_Commuters': 35, 'City': 'New York'},
    {'Mode': 'Walking', 'Percent_of_Commuters': 5, 'City': 'New York'}
]

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Use seaborn style settings to make the plot look nicer
sns.set(style="whitegrid")

# Create figure and axis for matplotlib
fig, ax = plt.subplots(1, figsize=(12, 6))

# Create color palette
cmap = sns.color_palette("coolwarm", len(data))
colors = [cmap[i] for i in range(len(data))]

# Use squarify to plot treemap
# sizes will be the Percent_of_Commuters
sizes = df['Percent_of_Commuters'].values
labels = df.apply(lambda x: f"{x['Mode']}\n({x['Percent_of_Commuters']}%)", axis=1)
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.7, ax=ax)

# Remove axis
ax.axis('off')

# Add a title
plt.title(f"Percent of Commuters by Mode in {data[0]['City']}", fontsize=16)

# Display the plot
plt.show()