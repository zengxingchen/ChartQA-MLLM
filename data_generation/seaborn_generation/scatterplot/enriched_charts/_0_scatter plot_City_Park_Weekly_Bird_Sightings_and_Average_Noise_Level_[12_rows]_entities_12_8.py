
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    "State": ["California", "Texas", "Florida", "New York", "Pennsylvania", "Illinois", "Ohio", 
              "Georgia", "North Carolina", "Michigan", "New Jersey", "Virginia", "Washington", 
              "Arizona", "Massachusetts", "Tennessee", "Indiana", "Missouri", "Maryland", 
              "Wisconsin", "Colorado", "Minnesota", "South Carolina", "Alabama", "Louisiana",
              "Kentucky", "Oregon", "Oklahoma", "Connecticut", "Iowa", "Mississippi", "Arkansas", 
              "Kansas", "Utah", "Nevada", "New Mexico", "West Virginia", "Nebraska", "Idaho", 
              "Hawaii", "Maine", "New Hampshire", "Rhode Island", "Montana", "Delaware", "South Dakota", 
              "North Dakota", "Alaska", "Vermont", "Wyoming"],
    "Population_Density": [251.42, 108.50, 378.16, 420.08, 286.54, 231.16, 282.90, 
                           186.10, 211.36, 175.40, 1210.10, 214.30, 114.62, 64.95, 
                           892.00, 165.50, 186.84, 89.91, 626.70, 106.13, 55.05, 
                           71.59, 164.05, 97.11, 107.59, 113.95, 44.09, 57.65, 
                           741.40, 55.48, 63.50, 57.88, 35.90, 38.63, 26.80, 
                           17.20, 75.13, 24.90, 20.70, 219.94, 43.10, 149.80, 
                           1020.50, 7.10, 493.50, 11.40, 10.90, 1.30, 67.90, 6.00],
    "Median_Income": [71228, 59570, 53267, 64894, 59195, 63575, 55638, 56183, 52752, 54938, 
                      79363, 71535, 70116, 56581, 77385, 52392, 54933, 53578, 80776, 59305, 
                      68774, 70317, 52041, 48486, 46897, 48390, 60125, 50051, 76342, 58570, 
                      43529, 45726, 56951, 65358, 58038, 46748, 43469, 59670, 52225, 77765, 
                      55602, 74057, 63232, 52559, 64805, 56894, 61843, 73181, 57513, 61584]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create the scatterplot
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Population_Density', y='Median_Income', data=df,
                palette=sns.color_palette(["#FF6347", "#4682B4"]),
                sizes=(20, 200), size='Population_Density', marker='o',
                edgecolor='black', alpha=0.75)

# Additional customizations for topic change
plt.title('State-wise Population Density vs Median Income in the USA')
plt.xlabel('Population Density (per square mile)')
plt.ylabel('Median Household Income (USD)')

# Show the plot
plt.show()