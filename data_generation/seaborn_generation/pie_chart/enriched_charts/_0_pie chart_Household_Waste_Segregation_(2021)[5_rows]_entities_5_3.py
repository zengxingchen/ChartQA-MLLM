
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data preparation
data = {
    'Category': [
        'Education', 'Healthcare', 'Infrastructure', 'Research', 'Defense',
        'Environment', 'Social Welfare', 'Arts and Culture', 'Science and Technology', 'Agriculture'
    ],
    'Value': [
        15000, 25000, 20000, 12000, 18000,
        10000, 16000, 5000, 21000, 9000
    ]
}

df = pd.DataFrame(data)

# Colors for each category
colors = [
    '#FF6347', '#FFD700', '#4682B4', '#6A5ACD', '#20B2AA',
    '#32CD32', '#DA70D6', '#FF4500', '#1E90FF', '#9ACD32'
]

# Visualizing data using seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(10, 10))
plt.title('Budget Allocation by Category for 2023')
plt.pie(df['Value'], labels=df['Category'], colors=colors, autopct='%1.1f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Show plot (commented out because we might not want to show it in certain environments, like a script)
# plt.show()