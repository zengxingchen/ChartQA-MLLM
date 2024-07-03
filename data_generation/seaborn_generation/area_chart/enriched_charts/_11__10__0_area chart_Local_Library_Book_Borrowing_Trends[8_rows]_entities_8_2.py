
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the table data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=31, freq='D'),
    'Sales': [200, 210, 220, 230, 225, 240, 235, 250, 260, 255, 
              265, 270, 275, 280, 290, 295, 300, 310, 320, 330, 
              340, 350, 345, 355, 360, 370, 380, 390, 400, 410, 420]
}

df = pd.DataFrame(data)

# Set the size of the chart
plt.figure(figsize=(16, 8))

# Create an area chart
sns.lineplot(data=df, x='Date', y='Sales', color='#1f77b4', lw=2)
plt.fill_between(df['Date'], 0, df['Sales'], color='#1f77b4', alpha=0.3)

# Add title and labels
plt.title('Daily Sales for January 2023', fontsize=18, pad=20)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Sales (Units)', fontsize=14)

# Assign text label on the chart
plt.text(x=df['Date'][21], y=df['Sales'][21], s="Highest Sales", color='#d62728', va='bottom', ha='right')

# Enhance the x-axis date format
plt.xticks(rotation=45)

# Display the chart
plt.tight_layout()
plt.show()