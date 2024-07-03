
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Category': ['Fiction', 'Non-Fiction', 'Mystery', 'Science Fiction', 'Fantasy', 'Biography',
                 'History', 'Poetry', 'Children\'s Books', 'Romance', 'Comics', 'Self-Help',
                 'Cookbooks', 'Travel', 'Education', 'Health & Fitness', 'Art', 'Business',
                 'Technology', 'Philosophy'],
    'Books': [320, 280, 150, 200, 180, 100, 160, 90, 140, 110, 170, 130, 120, 80, 200, 140, 90, 180, 160, 70],
    'Authors': [150, 120, 60, 90, 75, 50, 65, 40, 55, 50, 60, 45, 50, 35, 70, 50, 40, 65, 60, 30],
    'Publishers': [25, 20, 10, 15, 12, 8, 9, 5, 7, 10, 12, 9, 6, 4, 8, 6, 5, 10, 9, 4],
    'Market_Value': [400, 350, 250, 300, 270, 220, 240, 200, 230, 210, 260, 220, 210, 190, 250, 220, 200, 270, 250, 180]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 9))

sns.scatterplot(data=df, x="Books", y="Authors", size="Market_Value", sizes=(100, 1000),
                hue="Market_Value", palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
                                             "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",
                                             "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
                                             "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"])

plt.title("Literature Categories: Books, Authors, and Market Value", fontsize=18, pad=20)
plt.xlabel("Number of Books", fontsize=14)
plt.ylabel("Number of Authors", fontsize=14)

plt.legend(title="Market Value (in millions USD)", loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

plt.show()