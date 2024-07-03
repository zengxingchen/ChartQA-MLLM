
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Object": ["Proxima Centauri", "Barnard's Star", "Wolf 359", "Lalande 21185", "Sirius", "Luyten 726-8", "Ross 154", "Ross 248", "Epsilon Eridani", "Lacaille 9352", "Ross 128", "EZ Aquarii"],
    "Distance from Earth (light years)": [4.24, 5.96, 7.78, 8.29, 8.6, 8.73, 9.69, 10.32, 10.52, 10.74, 11.03, 11.26]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
fig, ax = plt.subplots(figsize=(14, 10))

# Area chart
ax.fill_between(df['Object'], df['Distance from Earth (light years)'], color='#ff7f0e', alpha=0.7)

# Titles and labels
ax.set_title('Distances of Nearby Stars from Earth', fontsize=20, pad=30)
ax.set_xlabel('Astronomical Object', fontsize=16)
ax.set_ylabel('Distance from Earth (light years)', fontsize=16)

# Annotations
for i, txt in enumerate(df['Distance from Earth (light years)']):
    ax.annotate(txt, (df['Object'][i], df['Distance from Earth (light years)'][i]), textcoords="offset points", xytext=(0,5), ha='center')

# Display the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()