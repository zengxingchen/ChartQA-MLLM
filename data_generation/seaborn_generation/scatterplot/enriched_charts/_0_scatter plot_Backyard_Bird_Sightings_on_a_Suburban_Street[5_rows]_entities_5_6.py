
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the data
data = {
    'Height_cm': [150, 152, 155, 158, 160, 162, 165, 168, 170, 172, 175, 178, 180, 183, 185, 188, 190, 193, 195, 198, 200],
    'Weight_kg': [45, 48, 50, 54, 56, 58, 62, 65, 68, 70, 73, 75, 78, 82, 85, 89, 92, 96, 99, 103, 106]
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Create the scatterplot with custom figure size (width & height)
plt.figure(figsize=(12, 6))

# Plot the scatterplot with a specific color scheme
sns.scatterplot(x='Height_cm', y='Weight_kg', data=df, color="#3498db")

# Set title and labels for axes
plt.title('Relationship Between Height and Weight of Individuals')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')

# Show the plot
plt.show()