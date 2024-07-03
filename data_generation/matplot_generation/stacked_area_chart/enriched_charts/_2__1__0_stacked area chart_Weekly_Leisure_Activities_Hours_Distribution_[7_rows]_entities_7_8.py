
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Rock': [2, 3, 1, 2, 3, 2, 3],
    'Pop': [3, 2, 2, 3, 2, 2, 3],
    'Jazz': [1, 2, 3, 2, 1, 3, 2],
    'Classical': [1, 2, 1, 2, 3, 1, 2],
    'HipHop': [2, 1, 2, 2, 2, 3, 1],
    'Other': [2, 3, 1, 2, 1, 2, 2]
}
df = pd.DataFrame(data)
df.set_index('Day', inplace=True)

plt.figure(figsize=(16, 10))
plt.stackplot(df.index, df['Rock'], df['Pop'], df['Jazz'], df['Classical'], df['HipHop'], df['Other'], 
              colors=['#FF4500', '#1E90FF', '#32CD32', '#FFD700', '#800080', '#FF1493'])

plt.xlabel('Day of the Week')
plt.ylabel('Hours')
plt.title('Weekly Music Listening Habits', fontsize=16, pad=20)

for i, day in enumerate(df.index):
    plt.text(i, df.loc[day].sum() - 0.5, f"{df.loc[day].sum()}h", ha='center', fontsize=10)

plt.legend(['Rock', 'Pop', 'Jazz', 'Classical', 'HipHop', 'Other'], loc='upper left')
plt.tight_layout()

plt.show()