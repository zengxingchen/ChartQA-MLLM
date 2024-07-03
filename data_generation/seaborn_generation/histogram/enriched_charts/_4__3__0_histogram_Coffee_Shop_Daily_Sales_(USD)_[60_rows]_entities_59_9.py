
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Heart_Rate': [
        60, 62, 65, 67, 70, 70, 72, 75, 75, 77, 80, 80, 80, 82, 85, 85, 87, 90, 
        90, 90, 92, 95, 95, 95, 97, 100, 100, 102, 105, 105, 107, 110, 110, 112, 
        115, 115, 117, 120, 122, 125, 125, 127, 130, 132, 135, 137, 140
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 6))
sns.histplot(data=df, y='Heart_Rate', binwidth=5, color='#3498db')

plt.title('Distribution of Heart Rates in Fitness Sessions')
plt.xlabel('Frequency')
plt.ylabel('Heart Rate (BPM)')

plt.show()