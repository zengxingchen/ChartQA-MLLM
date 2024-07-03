
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Event': ['Olympics', 'Olympics', 'Olympics', 'Olympics', 'Olympics',
              'FIFA World Cup', 'FIFA World Cup', 'FIFA World Cup', 'FIFA World Cup', 'FIFA World Cup',
              'Wimbledon', 'Wimbledon', 'Wimbledon', 'Wimbledon', 'Wimbledon',
              'Super Bowl', 'Super Bowl', 'Super Bowl', 'Super Bowl', 'Super Bowl',
              'Tour de France', 'Tour de France', 'Tour de France', 'Tour de France', 'Tour de France'],
    'Year': [2000, 2004, 2008, 2012, 2016,
             2002, 2006, 2010, 2014, 2018,
             2000, 2005, 2010, 2015, 2020,
             2000, 2005, 2010, 2015, 2020,
             2000, 2005, 2010, 2015, 2020],
    'Participants': [10651, 11099, 10942, 10568, 11238,
                     736, 736, 736, 736, 736,
                     128, 128, 128, 128, 128,
                     100, 100, 100, 100, 100,
                     189, 189, 198, 198, 176],
    'Viewership': [3400000000, 3700000000, 3900000000, 4200000000, 3500000000,
                   1400000000, 1500000000, 1600000000, 1700000000, 1800000000,
                   30000000, 35000000, 40000000, 42000000, 38000000,
                   88000000, 89000000, 91000000, 114000000, 102000000,
                   20000000, 25000000, 28000000, 30000000, 26000000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 7))
bubble = sns.scatterplot(data=df, x="Year", y="Participants", size="Viewership", 
                         hue="Event", sizes=(20, 2000), 
                         palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"])

bubble.set_title('Major Sports Events Participation and Viewership Over Years', y=1.03)
bubble.set_xlabel('Year')
bubble.set_ylabel('Number of Participants')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.grid(True)
plt.show()