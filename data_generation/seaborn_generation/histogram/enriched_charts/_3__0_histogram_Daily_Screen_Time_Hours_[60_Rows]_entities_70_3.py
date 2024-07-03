
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Height (cm)": [160, 172, 168, 165, 170, 158, 174, 162, 167, 176, 
                    169, 155, 163, 180, 177, 166, 161, 175, 164, 178, 
                    159, 173, 157, 171, 179, 156, 182, 154, 181, 153, 
                    152, 183, 150, 151, 184, 149, 185, 186, 187, 148, 
                    147, 188, 189, 146, 190, 191, 145, 144, 143, 192, 
                    142, 193]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 6))

sns.histplot(data=df, y="Height (cm)", color="#8A2BE2", binwidth=1, orientation='vertical')

plt.title('Distribution of Heights Among Individuals')
plt.ylabel('Frequency')
plt.xlabel('Height (cm)')
plt.grid(True)

plt.show()