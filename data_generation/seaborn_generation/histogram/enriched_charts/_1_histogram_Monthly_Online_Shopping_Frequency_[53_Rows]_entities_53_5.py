
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the dataset
data = {
    'age': [
        23,25,29,22,34,35,40,24,30,28,27,31,33,36,41,43,38,37,39,45,47,50,49,46,44,42,
        48,52,54,55,53,51,56,58,60,59,57,61,65,63,64,62,66,68,70,69,67,71,73,75,74,72,
        76,78,80,79,77,82,84,83,81,85,87,86,89,88,90,92,94,93,91,95,97,96,98,99,100,97,
        95,92,90,88,86,84,82,80,78,76,74,72,70,68,66,64,62,60,58,56,54,52,50,48,46,44,
        42,40,38,37,35,34,32,31,29,27,25,23,21,19,18,20,22,24,26,28,30,32,33,36,39,41,
        43
    ]
}
df = pd.DataFrame(data)

# Set the style and the figure size
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))

# Create the histogram chart
sns.histplot(
    data=df, 
    x="age", 
    binwidth=2, 
    kde=False, 
    color="#003f5c"
)

# Adjusting further aesthetics of the plot
plt.title("Distribution of Participants' Ages in a Marathon")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.xlim(15, 105)  # Assuming our range of interest in ages is from 15 to 105
plt.xticks(range(15, 106, 5))  # Setting the x-axis ticks to be every 5 years

# Display the plot
plt.show()