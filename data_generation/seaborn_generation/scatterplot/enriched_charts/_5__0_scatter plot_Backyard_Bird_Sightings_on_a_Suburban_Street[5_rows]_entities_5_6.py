
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the data
data = {
    'Height_cm': [150, 151, 152, 153, 155, 157, 158, 160, 162, 164, 165, 167, 168, 170, 172, 174, 175, 177, 178, 180, 182, 183, 185, 187, 188, 190, 192, 193, 195, 197, 198, 200],
    'Weight_kg': [45, 47, 48, 50, 51, 53, 54, 56, 58, 60, 62, 64, 65, 68, 70, 72, 73, 74, 75, 78, 80, 82, 85, 88, 89, 92, 95, 96, 99, 101, 103, 106]
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Create the scatterplot with custom figure size (width & height)
plt.figure(figsize=(14, 8))

# Plot the scatterplot with a specific color scheme
sns.scatterplot(x='Height_cm', y='Weight_kg', data=df, color="#FF5733")

# Set title and labels for axes
plt.title('Height vs Weight: A Health Perspective', fontsize=16, pad=20)
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')

# Show the plot
plt.show()