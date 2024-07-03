
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Fruit": ["Apple", "Banana", "Orange", "Strawberry", "Pineapple", 
              "Mango", "Blueberry", "Grapes", "Watermelon", "Kiwi",
              "Papaya", "Lemon", "Guava", "Peach", "Plum",
              "Cherry", "Pomegranate", "Cranberry", "Raspberry", "Blackberry"],
    "VitaminCContent": [4.6, 8.7, 53.2, 59.1, 47.8, 
                        36.4, 9.7, 10.8, 8.1, 92.7, 
                        60.9, 53.0, 228.3, 6.6, 9.5, 
                        7.0, 10.2, 14.0, 26.2, 21.0],
    "SugarContent": [10.4, 12.2, 9.0, 4.9, 10.0, 
                     14.8, 9.7, 16.3, 6.2, 9.0, 
                     5.9, 2.5, 5.4, 8.4, 9.9, 
                     12.8, 13.7, 4.3, 4.4, 4.9]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))

scatter_plot = sns.scatterplot(x="VitaminCContent", y="SugarContent", data=df, s=120,
                               palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", 
                                        "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",
                                        "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", 
                                        "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"],
                               hue="Fruit", legend=False)

scatter_plot.set_title("Vitamin C and Sugar Content in Various Fruits", fontsize=18)
scatter_plot.set_xlabel("Vitamin C Content (mg per 100g)", fontsize=14)
scatter_plot.set_ylabel("Sugar Content (g per 100g)", fontsize=14)

plt.show()