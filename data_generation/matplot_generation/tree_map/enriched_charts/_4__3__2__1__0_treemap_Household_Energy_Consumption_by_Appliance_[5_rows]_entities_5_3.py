
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    "City": ["New York", "New York", "New York", "New York", "New York", 
             "San Francisco", "San Francisco", "San Francisco", "San Francisco", "San Francisco",
             "Seattle", "Seattle", "Seattle", "Seattle", "Seattle", 
             "Austin", "Austin", "Austin", "Austin", "Austin", 
             "Boston", "Boston", "Boston", "Boston", "Boston", 
             "Chicago", "Chicago", "Chicago", "Chicago", "Chicago", 
             "Miami", "Miami", "Miami", "Miami", "Miami", 
             "Los Angeles", "Los Angeles", "Los Angeles", "Los Angeles", "Los Angeles"],
    "Category": ["Movies", "Music", "Theater", "Art", "Dance", 
                 "Movies", "Music", "Theater", "Art", "Dance", 
                 "Movies", "Music", "Theater", "Art", "Dance", 
                 "Movies", "Music", "Theater", "Art", "Dance", 
                 "Movies", "Music", "Theater", "Art", "Dance", 
                 "Movies", "Music", "Theater", "Art", "Dance", 
                 "Movies", "Music", "Theater", "Art", "Dance", 
                 "Movies", "Music", "Theater", "Art", "Dance"],
    "Number of Mentions": [450, 370, 250, 310, 210, 
                           400, 360, 270, 320, 220, 
                           380, 340, 260, 330, 210, 
                           390, 330, 280, 300, 230, 
                           370, 320, 290, 310, 200, 
                           360, 310, 280, 300, 220, 
                           350, 300, 270, 290, 210, 
                           420, 380, 300, 340, 230]
}

df = pd.DataFrame(data)

grouped_data = df.groupby("Category").sum().reset_index()

colors = ["#4E79A7", "#F28E2B", "#E15759", "#76B7B2", "#59A14F", 
          "#EDC948", "#B07AA1", "#FF9DA7", "#9C755F", "#BAB0AC"]

plt.figure(figsize=(22, 18))
squarify.plot(sizes=grouped_data['Number of Mentions'], label=grouped_data['Category'], alpha=0.8, color=colors)
plt.title('Mentions of Entertainment & Leisure Activities in Major Cities', fontsize=22, pad=40)
plt.axis('off')
plt.show()