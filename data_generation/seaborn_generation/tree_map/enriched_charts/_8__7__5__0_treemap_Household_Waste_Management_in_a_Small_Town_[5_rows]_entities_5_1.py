
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data Frame
data = {
    "Year": ['2019', '2019', '2019', '2019', '2019', '2019', '2019',
             '2020', '2020', '2020', '2020', '2020', '2020', '2020',
             '2021', '2021', '2021', '2021', '2021', '2021', '2021',
             '2022', '2022', '2022', '2022', '2022', '2022', '2022'],
    "Topic": ['Bioethics', 'Environmental Ethics', 'Ethical Theory', 'Medical Ethics', 'Professional Ethics', 'Social Ethics', 'Political Ethics',
              'Bioethics', 'Environmental Ethics', 'Ethical Theory', 'Medical Ethics', 'Professional Ethics', 'Social Ethics', 'Political Ethics',
              'Bioethics', 'Environmental Ethics', 'Ethical Theory', 'Medical Ethics', 'Professional Ethics', 'Social Ethics', 'Political Ethics',
              'Bioethics', 'Environmental Ethics', 'Ethical Theory', 'Medical Ethics', 'Professional Ethics', 'Social Ethics', 'Political Ethics'],
    "Papers": [25.5, 18.0, 22.3, 15.7, 13.4, 17.2, 14.1,
               27.3, 20.1, 24.8, 17.5, 15.2, 19.3, 16.0,
               30.2, 22.4, 27.1, 19.0, 17.0, 21.5, 18.3,
               32.6, 24.5, 29.7, 21.2, 18.8, 23.9, 20.4]
}
df = pd.DataFrame(data)

# Settings
plt.figure(figsize=(16, 10))
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A5', '#33FFF1', '#FF8C33', '#8C33FF']

# Treemap plot
squarify.plot(sizes=df["Papers"], label=df["Topic"], color=colors, alpha=0.8)
plt.title("Publication Statistics on Ethical Topics (2019-2022)", fontsize=20, color='#333333', y=1.05)
plt.axis('off')
plt.show()