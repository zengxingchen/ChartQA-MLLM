
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data: Student performance in different subjects
data = {
    'City': [
        'London','Berlin','Paris','Madrid','Rome',
        'Amsterdam','Brussels','Vienna','Oslo',
        'Stockholm','Copenhagen','Lisbon','Prague',
        'Warsaw','Athens','Helsinki','Dublin'
    ],
    'Math Score': [
        78, 82, 75, 90, 85,
        76, 80, 79, 88,
        92, 85, 74, 81,
        83, 77, 90, 86
    ],
    'Reading Score': [
        85, 88, 80, 92, 87,
        84, 81, 83, 90,
        95, 86, 78, 84,
        82, 79, 91, 88
    ]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Set the width and height of the plot
plt.figure(figsize=(14, 10))

# Create Seaborn scatterplot
sns.scatterplot(
    x='Math Score', y='Reading Score',
    hue='City', palette=[
        '#FF6347', '#4682B4', '#3CB371', '#FFD700', '#FFA07A',
        '#20B2AA', '#778899', '#DA70D6', '#C71585', '#FF4500',
        '#2E8B57', '#DAA520', '#CD853F', '#5F9EA0', '#9ACD32',
        '#1E90FF', '#BDB76B'
    ],
    data=df,
    s=100  # Marker size
)

# Add labels and title
plt.xlabel('Math Score')
plt.ylabel('Reading Score')
plt.title('Student Performance in Different Subjects')

# Display plot
plt.show()