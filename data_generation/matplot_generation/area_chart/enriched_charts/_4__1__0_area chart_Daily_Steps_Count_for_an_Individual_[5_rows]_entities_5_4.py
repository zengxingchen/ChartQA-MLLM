
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Date': [
        '01-01-2024', '02-01-2024', '03-01-2024', '04-01-2024', '05-01-2024', 
        '06-01-2024', '07-01-2024', '08-01-2024', '09-01-2024', '10-01-2024', 
        '11-01-2024', '12-01-2024', '13-01-2024', '14-01-2024', '15-01-2024', 
        '16-01-2024', '17-01-2024', '18-01-2024', '19-01-2024', '20-01-2024', 
        '21-01-2024', '22-01-2024', '23-01-2024', '24-01-2024', '25-01-2024', 
        '26-01-2024', '27-01-2024', '28-01-2024', '29-01-2024', '30-01-2024', 
        '31-01-2024'
    ],
    'Visitors': [
        150, 180, 200, 220, 210, 230, 250, 260, 280, 300, 320, 340, 350, 370, 
        390, 410, 420, 440, 460, 480, 500, 520, 540, 550, 560, 580, 600, 620, 
        640, 660, 680
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(12, 6))
plt.fill_between(df['Date'], df['Visitors'], color='#ff6347', alpha=0.6)

# Title and labels
plt.title('Daily Visitors in January 2024', fontsize=16, loc='left')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Number of Visitors', fontsize=12)

# Annotations
plt.annotate('Visitor Surge', xy=('21-01-2024', 500), xytext=('15-01-2024', 600),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, color='black')

# Adjustments
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()