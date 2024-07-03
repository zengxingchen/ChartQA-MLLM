
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create data
data = {
    'Month': ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"],
    'Industry A': [450, 480, 460, 470, 490, 510, 530, 520, 500, 510, 530, 550],
    'Industry B': [550, 530, 510, 495, 510, 500, 520, 540, 530, 520, 510, 500],
    'Industry C': [350, 370, 390, 380, 360, 340, 330, 310, 300, 290, 270, 260]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame
df_melted = df.melt('Month', var_name='Industry', value_name='CO2 Emissions')

# Create the line plot
plt.figure(figsize=(14, 8))
sns.lineplot(data=df_melted, x='Month', y='CO2 Emissions', hue='Industry',
             palette=['#1F77B4', '#FF7F0E', '#2CA02C'])

# Add annotations for the start and end of each line
for industry in ['Industry A', 'Industry B', 'Industry C']:
    plt.text(x=df['Month'][0], y=df[industry][0], s=f"{df[industry][0]} (Start)",
             color='black', ha='center', va='bottom')
    plt.text(x=df['Month'].iloc[-1], y=df[industry].iloc[-1],
             s=f"{df[industry].iloc[-1]} (End)", color='black', ha='center', va='bottom')

plt.title('Monthly CO2 Emissions of Different Industries (tons)', pad=20)
plt.xlabel('Month')
plt.ylabel('CO2 Emissions (tons)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()