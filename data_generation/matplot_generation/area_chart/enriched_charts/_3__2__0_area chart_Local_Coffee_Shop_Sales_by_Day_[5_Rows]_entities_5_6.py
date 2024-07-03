
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'AvgStepCount': [8000, 8200, 8500, 8300, 8700, 9000, 9200, 9100, 8900, 8800, 8500, 8300]
}
df = pd.DataFrame(data)

# Convert 'Month' to categorical type with proper order
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Create the area chart
plt.figure(figsize=(16, 10))
plt.plot(df['Month'], df['AvgStepCount'], lw=2, color='#1f77b4')

# Filling the area under the line
plt.fill_between(x=df['Month'], y1=df['AvgStepCount'], color='#aec7e8', alpha=0.6)

# Annotate the chart with text labels
for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['AvgStepCount'][i]+100, str(df['AvgStepCount'][i])+' steps', horizontalalignment='center')

# Customize the axes
plt.xlabel('Month')
plt.ylabel('Average Step Count')
plt.title('Monthly Average Step Count', pad=20)

# Show the final plot
plt.show()