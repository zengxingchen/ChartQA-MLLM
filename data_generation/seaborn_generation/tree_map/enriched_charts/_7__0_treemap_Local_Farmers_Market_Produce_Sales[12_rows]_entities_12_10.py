
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import squarify

# Define the data
data = {
    'Company': [
        'Apple', 'Microsoft', 'Saudi Aramco', 'Alphabet', 
        'Amazon', 'Tesla', 'Berkshire Hathaway', 'Meta', 
        'TSMC', 'NVIDIA', 'Visa', 'JP Morgan', 
        'Samsung', 'Johnson & Johnson', 'Walmart'
    ],
    'Market Capitalization (Billion USD)': [
        2520, 2090, 2050, 1520, 1400, 900, 640, 600, 550, 
        500, 450, 440, 430, 410, 400
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a color palette
colors = [
    '#FF6347', '#FFD700', '#FF4500', '#FF1493',
    '#00FF00', '#ADFF2F', '#20B2AA', '#87CEFA',
    '#6A5ACD', '#FF00FF', '#FFA07A', '#7FFF00',
    '#BA55D3', '#00CED1', '#1E90FF'
]

# Define size of the figure
plt.figure(figsize=(18, 10))

# Plot the treemap with the specified colors and data
squarify.plot(sizes=df['Market Capitalization (Billion USD)'], label=df['Company'], color=colors, alpha=0.8)

plt.title('Market Capitalization of Top Tech Companies (in Billion USD)', fontsize=22, pad=20)
plt.axis('off')
plt.show()