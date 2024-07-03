
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Event': ['Business_Conference', 'Startup_Pitch', 'Workshop', 'Networking_Event', 'Product_Launch', 
              'Investor_Meeting', 'Panel_Discussion', 'Trade_Show', 'Seminar', 'Hackathon', 'Team_Building', 
              'Webinar', 'Training_Session', 'Roundtable', 'Annual_Meeting'],
    'Participants': [250, 180, 220, 150, 300, 170, 200, 280, 230, 190, 140, 160, 210, 130, 290]
}

df = pd.DataFrame(data)

f, ax = plt.subplots(figsize=(10, 8))

palette = ['#4c72b0', '#55a868', '#c44e52', '#8172b3', '#ccb974', '#64b5cd', 
           '#e377c2', '#bcbd22', '#17becf', '#ff7f0e', '#aec7e8', '#ffbb78', 
           '#98df8a', '#ff9896', '#c5b0d5']

sns.barplot(x='Participants', y='Event', data=df,
            palette=palette, orient='h', ax=ax, dodge=False)

ax.set(xlim=(0, 350), xlabel="Number of Participants", ylabel="Event")
ax.set_title('Number of Participants by Event Type', pad=20)

for container in ax.containers:
    ax.bar_label(container, label_type='edge', padding=3)

plt.tight_layout()
plt.show()