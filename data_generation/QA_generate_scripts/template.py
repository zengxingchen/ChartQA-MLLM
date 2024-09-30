import json
def get_template(chart_type):
    if chart_type == "100_stacked_bar_chart":
        return [
            '''
```json
[
    {
        "from": "human",
        "type_of_question": "Data Retrieval",
        "value": "What was the percentage of Books sold in 1990?."
    },
    {
        "from": "gpt",
        "value": "Looking at the chart, the percentage of Books sold in 1990 can be found by locating the bar representing Books for the year 1990. The Books segment is the second section of the stacked bar and is colored in red. According to the visual encoding, the percentage for Books in 1990 is 20%.",
        "label": "20%"
    },
    {
        "from": "human",
        "type_of_question": "Find Extremum",
        "value": "In which year was the percentage of fiction sold the highest?"
    },
    {
        "from": "gpt",
        "value": "To determine the year when the percentage of fiction sold was the highest, we need to look at the yellow segments of the stacked bars across all the years. The highest yellow segment is in 1992, where the percentage is 32%. Therefore, the year with the highest percentage of fiction sold is 1992.",
        "label": "1992"
    },
    {
        "from": "human",
        "type_of_question": "Make Comparisons",
        "value": "Compare the percentage of cars sold between 2015 and 2023."
    },
    {
        "from": "gpt",
        "value": "To compare the percentage of cars sold between 2015 and 2023, we examine the orange segments in the stacked bars for those years. In 2015, the percentage for cars is 10%, while in 2023, it is 15%. Therefore, the percentage of cars sold increased from 10% in 2015 to 15% in 2023.",
        "label": "Increase"
    }
]
```
'''
        ]
    elif chart_type == "area_chart":
        return [
'''
```json
[
    {
        "from": "human",
        "type_of_question": "Data Retrieval",
        "value": "What is the number of phone users in the year 2020?"
    },
    {
        "from": "gpt",
        "value": "Based on the chart, the number of phone users in the year 2020 is 32 million.",
        "label": "32"
    },
    {
        "from": "human",
        "type_of_question": "Find Extremum",
        "value": "In which year was the number of phone users the highest?"
    },
    {
        "from": "gpt",
        "value": "To find the highest number of phone users, examine the y-axis values and identify the maximum data point in the series. The highest number of phone users recorded is in the year 2024, with 24 million users.",
        "label": "24"
    },
    {
        "from": "human",
        "type_of_question": "Determine Range",
        "value": "What is the range of global phone users from 1990 to 2022?"
    },
    {
        "from": "gpt",
        "value":  "The range of global phone users can be determined by subtracting the number of users in 1990 (12 million) from the number of users in 2022 (412 million). Therefore, the range is 412 - 12 = 400 million.",
        "label": "400"
    },
    {
        "from": "human",
        "type_of_question": "Find Correlations/Trends",
        "value": "What trend do you observe in the number of global phone users from 1990 to 2022?"
    },
    {
        "from": "gpt",
        "value": "The chart shows a clear increasing trend in the number of global phone users from 1990 to 2022. The number of users consistently rises each year, indicating steady growth in global phone adoption over this period.",
        "label": "increasing"
    },
    {
        "from": "human",
        "type_of_question": "Make Comparisons",
        "value": "How does the number of phone phone users in 2011 compare to that in 1991?",
    },
    {
        "from": "gpt",
        "value": "In 1991, there were 42 million global phone users. By 2011, this number had increased to 204 million. Therefore, the number of global phone users in 2011 was significantly higher than in 1991, showing an increasing users.",
        "label": "higher"
    }
]
```
'''

        ]
    elif chart_type == "bar_chart":
        return [
'''
```json
[
    {
        "from": "human",
        "type_of_question": "Data Retrieval",
        "value": "What is the Air Quality Index for London as shown in the chart?"
    },
    {
        "from": "gpt",
        "value": "To find the Air Quality Index (AQI) for London,the bar reaches up to 40 on the index.Therefore, the Air Quality Index for London is 40.",
        "label": "40"
    },
    {
        "from": "human",
        "type_of_question": "Find Extremum",
        "value": "Which city has the highest Air Quality Index according to the chart?"
    },
    {
        "from": "gpt",
        "value": "To identify the city with the highest Air Quality Index from the chart, we need to
                compare the heights of all the bars. Each bar represents the AQI for a city.
                Observing the heights of the bars, the tallest bar corresponds to Paris. The
                height reaches up to 240 on the index scale, indicating that Paris has the
                highest Air Quality Index.",
        "label": "Paris"
    },
    {
        "from": "human",
        "type_of_question": "Determine Range",
        "value": "What is the range of the Air Quality Index values presented in the chart?"
    },
    {
        "from": "gpt",
        "value": "To determine the range of the Air Quality Index values in the chart, identify the smallest and largest AQI values shown. The smallest bar height corresponds to Tokyo
            with an index of 45, and the tallest bar corresponds to Shanghai with an index of
            180. The range of the Air Quality Index values is therefore from 45 to 180.",
        "label": "45-180"
    },
    {
        "from": "human",
        "type_of_question": "Make Comparisons",
        "value": "How does the value of 'Quantum Computing' compare to 'Blockchain'?"
    },
    {
        "from": "gpt",
        "value": "In the chart, 'Quantum Computing' has a value of 120, while 'Blockchain' has a value of 160. Comparing these two values, 'Blockchain' has a higher value than 'Quantum Computing'.",
        "label": "Blockchain higher"
    }
]
```
'''
        ]
    elif chart_type == "bubble_chart":
        return [
            '''
```json
[
    {
        "from": "human",
        "type_of_question": "Data Retrieval",
        "value": "What is the size of the bubble at (X=5, Y=10)?"
    },
    {
        "from": "gpt",
        "value": "To find the size of the bubble at (X=5, Y=10), we locate the bubble at this position on the bubble chart. The size of this bubble is 20 units.",
        "label": "20 units"
    },
    {
        "from": "human",
        "type_of_question": "Find Extremum",
        "value": "Which bubble is the largest?"
    },
    {
        "from": "gpt",
        "value": "To identify the largest bubble, we look for the bubble with the greatest size on the chart. The largest bubble is at (X=7, Y=14) with a size of 30 units.",
        "label": "30 units"
    },
    {
        "from": "human",
        "type_of_question": "Determine Range",
        "value": "What is the range of X-values?"
    },
    {
        "from": "gpt",
        "value": "To determine the range of X-values, we look at the minimum and maximum X-values on the bubble chart. The X-values range from 1 to 10.",
        "label": "1 to 10"
    },
    {
        "from": "human",
        "type_of_question": "Characterize Distribution",
        "value": "How are the bubbles distributed across the X and Y axes?"
    },
    {
        "from": "gpt",
        "value": "The bubbles are scattered across the X and Y axes, with a higher concentration of larger bubbles around the middle range of X (4 to 7) and Y (8 to 12). There are fewer bubbles and smaller sizes at the extremes of both axes.",
        "label": "Concentrated in the middle"
    },
    {
        "from": "human",
        "type_of_question": "Find Anomalies",
        "value": "Are there any bubbles that stand out as anomalies?"
    },
    {
        "from": "gpt",
        "value": "To find anomalies, we look for bubbles that are significantly larger or positioned differently from the rest. There is one bubble at (X=2, Y=18) that stands out as an anomaly due to its unusually large size compared to other bubbles with similar X-values.",
        "label": "Anomaly"
    },
    {
        "from": "human",
        "type_of_question": "Find Clusters",
        "value": "Are there any clusters of bubbles?"
    },
    {
        "from": "gpt",
        "value": "To identify clusters, we look for groups of bubbles that are close together. There are two main clusters: one around (X=3, Y=7) and another around (X=6, Y=10), where bubbles are densely packed.",
        "label": "Two clusters"
    },
    {
        "from": "human",
        "type_of_question": "Find Correlations/Trends",
        "value": "Is there a trend or correlation between the X and Y values?"
    },
    {
        "from": "gpt",
        "value": "By examining the bubble chart, we can observe that as the X-values increase, the Y-values also tend to increase, indicating a positive correlation between X and Y. The size of the bubbles also generally increases with higher X and Y values.",
        "label": "Positive correlation"
    },
    {
        "from": "human",
        "type_of_question": "Make Comparisons",
        "value": "How do the bubbles at (X=3, Y=7) and (X=9, Y=13) compare?"
    },
    {
        "from": "gpt",
        "value": "To compare the bubbles at (X=3, Y=7) and (X=9, Y=13), we look at their respective sizes and positions on the bubble chart. The bubble at (X=3, Y=7) has a size of 15 units, while the bubble at (X=9, Y=13) has a size of 25 units. Therefore, the bubble at (X=9, Y=13) is larger.",
        "label": "Bubble at (X=9, Y=13) is larger"
    }
]
```
'''

        ]
    elif chart_type == "histogram":
        return [
            '''
```json
[
    {
        "from": "human",
        "type_of_question": "Data Retrieval",
        "value": "What is the frequency of the bin that ranges from 10 to 20?"
    },
    {
        "from": "gpt",
        "value": "To find the frequency of the bin that ranges from 10 to 20, we look at the height of the bar representing this range on the histogram. The frequency of this bin is 15.",
        "label": "15"
    },
    {
        "from": "human",
        "type_of_question": "Find Extremum",
        "value": "Which bin has the highest frequency?"
    },
    {
        "from": "gpt",
        "value": "To identify the bin with the highest frequency, we look for the tallest bar in the histogram. The bin with the highest frequency ranges from 20 to 30, with a frequency of 25.",
        "label": "25"
    },
    {
        "from": "human",
        "type_of_question": "Characterize Distribution",
        "value": "How is the data distributed across the bins?"
    },
    {
        "from": "gpt",
        "value": "To characterize the distribution, we observe the shape and spread of the histogram. The data shows a right-skewed distribution with most frequencies concentrated in the bins ranging from 10 to 30, and a gradual decrease in frequencies towards the higher bins.",
        "label": "Right-skewed"
    },
    {
        "from": "human",
        "type_of_question": "Make Comparisons",
        "value": "How do the frequencies of the bins 10-20 and 30-40 compare?"
    },
    {
        "from": "gpt",
        "value": "To compare the frequencies of the bins 10-20 and 30-40, we look at the heights of the respective bars on the histogram. The bin ranging from 10 to 20 has a frequency of 15, while the bin ranging from 30 to 40 has a frequency of 10. Therefore, the 10-20 bin has a higher frequency by 5.",
        "label": "10-20 bin is higher by 5"
    }
]
```
'''
        ]
    elif chart_type == "line_chart":
        return [
            '''
```json
[
    {
        "from": "human",
        "type_of_question": "Data Retrieval",
        "value": "What is the value at X=5?"
    },
    {
        "from": "gpt",
        "value": "To find the value at X=5, we locate the point on the line chart where the X-axis is 5. From the chart, the corresponding Y-value at X=5 is 10.",
        "label": "10"
    },
    {
        "from": "human",
        "type_of_question": "Find Extremum",
        "value": "What is the highest value in the chart?"
    },
    {
        "from": "gpt",
        "value": "To identify the highest value in the chart, we look for the peak point on the line chart. The highest value is at X=7 with a Y-value of 15.",
        "label": "15"
    },
    {
        "from": "human",
        "type_of_question": "Determine Range",
        "value": "What is the range of Y-values?"
    },
    {
        "from": "gpt",
        "value": "To determine the range of Y-values, we look at the minimum and maximum Y-values on the line chart. The Y-values range from 2 to 15.",
        "label": "2 to 15"
    },
    {
        "from": "human",
        "type_of_question": "Find Correlations/Trends",
        "value": "What trend can be observed in the data over time?"
    },
    {
        "from": "gpt",
        "value": "By examining the line chart, we can observe that the values generally increase over time, with some fluctuations. The overall trend shows a positive increase from X=1 to X=10.",
        "label": "Positive trend"
    },
    {
        "from": "human",
        "type_of_question": "Make Comparisons",
        "value": "How do the values at X=3 and X=9 compare?"
    },
    {
        "from": "gpt",
        "value": "To compare the values at X=3 and X=9, we look at their respective points on the line chart. At X=3, the Y-value is 5, and at X=9, the Y-value is 12. Therefore, the value at X=9 is higher than the value at X=3.",
        "label": "X=9 is higher"
    }
]
```
'''

        ]
    elif chart_type == "pie_chart":
        return [
            '''
```json
[
    {
        "from": "human",
        "type_of_question": "Data Retrieval",
        "value": "What is the percentage of Category A?"
    },
    {
        "from": "gpt",
        "value": "To find the percentage of Category A, we look at the pie chart segment labeled 'Category A'. According to the chart, Category A occupies 25% of the pie.",
        "label": "25%"
    },
    {
        "from": "human",
        "type_of_question": "Find Extremum",
        "value": "Which category has the largest share?"
    },
    {
        "from": "gpt",
        "value": "To identify the category with the largest share, we look for the largest segment in the pie chart. The segment labeled 'Category B' is the largest, occupying 40% of the pie.",
        "label": "Category B"
    },
    {
        "from": "human",
        "type_of_question": "Make Comparisons",
        "value": "How do the shares of Category A and Category C compare?"
    },
    {
        "from": "gpt",
        "value": "To compare the shares of Category A and Category C, we look at their respective segments in the pie chart. Category A occupies 25%, while Category C occupies 20%. Therefore, Category A has a larger share than Category C by 5%.",
        "label": "Category A is larger by 5%"
    }
]
```
'''

        ]
    elif chart_type == "scatterplot":
        return [
            '''
```json
[
    {
        "from": "human",
        "type_of_question": "Data Retrieval",
        "value": "What is the Y value of the point at (X=5)?"
    }
    },
    {
        "from": "gpt",
        "value": "To find the value of the point at (X=5), we locate the point with X-coordinate 5 on the scatterplot. The Y value at this point is 10.",
        "label": "10"
    },
    {
        "from": "human",
        "type_of_question": "Find Extremum",
        "value": "Which point has the highest Y-value?"
    },
    {
        "from": "gpt",
        "value": "To identify the point with the highest Y-value, we look for the point that is the highest on the vertical axis. The point with the highest Y-value is (X=7, Y=15).",
        "label": "(7,15)"
    },
    {
        "from": "human",
        "type_of_question": "Determine Range",
        "value": "What is the range of X-values?"
    },
    {
        "from": "gpt",
        "value": "To determine the range of X-values, we look at the minimum and maximum X-values on the scatterplot. The X-values range from 1 to 10.",
        "label": "1 to 10"
    },
    {
        "from": "human",
        "type_of_question": "Characterize Distribution",
        "value": "How are the points distributed across the X and Y axes?"
    },
    {
        "from": "gpt",
        "value": "The points are scattered across the X and Y axes, with a concentration of points in the middle range of X (4 to 6) and Y (8 to 12). There are fewer points at the extremes of both axes.",
        "label": "Concentrated in the middle"
    },
    {
        "from": "human",
        "type_of_question": "Find Anomalies",
        "value": "Are there any points that stand out as anomalies?"
    },
    {
        "from": "gpt",
        "value": "To find anomalies, we look for points that are far from the rest of the data. There is one point at (X=2, Y=14) that stands out as an anomaly since it is significantly higher than other points with similar X-values.",
        "label": "Anomaly"
    },
    {
        "from": "human",
        "type_of_question": "Find Clusters",
        "value": "Are there any clusters of points?"
    {
        "from": "gpt",
        "value": "To identify clusters, we look for groups of points that are close together. There are two main clusters: one around (X=4, Y=8) and another around (X=6, Y=12).",
        "label": "Two clusters"
    },
    {
        "from": "human",
        "type_of_question": "Find Correlations/Trends",
        "value": "Is there a trend or correlation between the X and Y values?"
    },
    {
        "from": "gpt",
        "value": "By examining the scatterplot, we can observe that as the X-values increase, the Y-values also tend to increase. This indicates a positive correlation between X and Y.",
        "label": "Positive correlation"
    },
    {
        "from": "human",
        "type_of_question": "Make Comparisons",
        "value": "How do the points at (X=3, Y=7) and (X=9, Y=13) compare?"
    },
    {
        "from": "gpt",
        "value": "To compare the points at (X=3, Y=7) and (X=9, Y=13), we look at their positions on the scatterplot. The point at (X=9, Y=13) is higher on the Y-axis and further to the right on the X-axis compared to the point at (X=3, Y=7), indicating higher values in both dimensions.",
        "label": "Higher in both dimensions"
    }
]
```
'''
        ]
    elif chart_type == "stacked_area_chart":
        return [
            '''
```json
[
    {
        "from": "human",
        "type_of_question": "Data Retrieval",
        "value": "What was the total sales in 2022?"
    },
    {
        "from": "gpt",
        "value": "To find the total sales in 2022, we look at the vertical axis value for 2022, summing the contributions of all product categories. By observing the stacked area chart, the total sales in 2022 amount to '500 units'.",
        "label": "500 units"
    },
    {
        "from": "human",
        "type_of_question": "Find Extremum",
        "value": "Which year had the highest total sales?"
    },
    {
        "from": "gpt",
        "value": "To identify the year with the highest total sales, we examine the peaks of the stacked area chart. The year with the highest total sales is represented by the peak point where the combined areas of all product categories are at their maximum. In this chart, the highest total sales occur in 2023.",
        "label": "2023"
    },
    {
        "from": "human",
        "type_of_question": "Determine Range",
        "value": "What is the range of total sales from 2019 to 2023?"
    },
    {
        "from": "gpt",
        "value": "To determine the range of total sales from 2019 to 2023, we identify the minimum and maximum total sales values during this period. From the stacked area chart, the minimum total sales occur in 2019 at 300 units, and the maximum total sales occur in 2023 at 600 units. Therefore, the range of total sales is '300 to 600 units'.",
        "label": "300 to 600 units"
    },
    {
        "from": "human",
        "type_of_question": "Find Correlations/Trends",
        "value": "How has the distribution of sales among different product categories changed over the past five years?"
    },
    {
        "from": "gpt",
        "value": "By examining the stacked area chart, we can observe the sales distribution across different product categories from 2019 to 2023. In 2019, Category A dominated the sales, followed by Category B and Category C. Over the years, the proportion of Category A's sales has decreased, while Category B and Category C have seen an increase. In 2023, Category B has overtaken Category A as the leading product category in terms of sales. This trend indicates a shift in consumer preferences or market dynamics over the five-year period.",
        "label": "Shift in market dynamics"
    },
    {
        "from": "human",
        "type_of_question": "Make Comparisons",
        "value": "Which year had the highest total sales, and how do the product categories contribute to it?"
    },
    {
        "from": "gpt",
        "value": "To determine the year with the highest total sales, we look at the peak of the stacked area chart representing each year. The tallest peak corresponds to 2023. In 2023, the contribution of each product category to the total sales is as follows: Category A contributed significantly, followed by Category B and Category C. Thus, 2023 had the highest total sales, with Category A being the major contributor.",
        "label": "2023"
    }
]
```
'''

        ]
    elif chart_type == "stacked_bar_chart":
        return [
            '''
```json
[
    {
        "from": "human",
        "type_of_question": "Data Retrieval",
        "value": "What is the investment in Technology for the year 2020?"
    },
    {
        "from": "gpt",
        "value": "The investment in Technology for the year 2020 can be retrieved directly from the chart. Look for the bar representing 'Technology' (the yellow bar) and identify its length value at the y-axis label for the year 2020. The investment amount shown is 20000.",
        "label": "20000"
    {
        "from": "human",
        "type_of_question": "Find Extremum",
        "value":"Which sector had the highest investment in 2022?"
    },
    {
        "from": "gpt",
        "value": "To determine which sector had the highest investment in 2022, observe the segment of each sector's bar for the year 2022. 'Technology' (the yellow bar) is the highest segment in that year. Therefore, the sector with the highest investment is Technology.",
        "label": "Technology"
    },
    {
        "from": "human",
        "type_of_question": "Determine Range",
        "value": "What is the range of protein content across all fruits?"
    },
    {
        "from": "gpt",
        "value": "To find the range of protein content, we identify the minimum and maximum values of protein across all fruits. The minimum protein content is 1.2 units (found in Grapes, Pineapple, and Watermelon) and the maximum is 1.6 units (found in Banana), resulting in a range of 1.2-1.6 units.",
        "label": "1.2-1.6"
    },
    {
        "from": "human",
        "type_of_question": "Find correlations/ trends",
        "value": "How has the distribution of sales among different product categories changed over the past five years?"
    },
    {
        "from": "gpt",
        "value": "By examining the stacked bar chart, we can observe the sales distribution across different product categories from 2019 to 2023. In 2019, Category A dominated the sales, followed by Category B and Category C. Over the years, the proportion of Category A's sales has decreased, while Category B and Category C have seen an increase. In 2023, Category B has overtaken Category A as the leading product category in terms of sales. This trend indicates a shift in consumer preferences or market dynamics over the five-year period.",
        "label": "Shift in market dynamics"
    },
    {
        "from": "human",
        "type_of_question": "Make Comparisons",
        "value": "Which year had the highest total sales, and how do the product categories contribute to it?"
    },
    {
        "from": "gpt",
        "value": "To determine the year with the highest total sales, we look at the height of the stacked bars representing each year. The tallest bar corresponds to 2021. In 2021, the contribution of each product category to the total sales is as follows: Category A contributed the most, followed by Category B and Category C. Thus, 2021 had the highest total sales, with Category A being the major contributor.",
        "label": "2021"
    }
]
```
'''

        ]
    elif chart_type == "tree_map":
        return [
            '''
```json
[
    {
        "from": "human",
        "type_of_question": "Data Retrieval",
        "value": "What is the number of students majoring in Law?"
    },
    {
        "from": "gpt",
        "value": "To answer this question, I will locate the 'Law' section in the treemap. The value for Business is given as 400. Therefore, the number of students majoring in Business is 400.",
        "label": "400"
    },
    {
        "from": "human",
        "type_of_question": "Find Extremum",
        "value": "Which discipline has the highest number of students enrolled?"
    },
    {
        "from": "gpt",
        "value": "To find the discipline with the highest number of students, I will look for the largest value in the treemap. 'Business' has the highest value of 700. Hence, the discipline with the highest number of students enrolled is Business.",
        "label": "Business"
    },
    {
        "from": "human",
        "type_of_question": "Make Comparisons",
        "value": "Compare the enrollment in Science/Biology and Art/Visual Arts. Which one has more students?"
    },
    {
        "from": "gpt",
        "value": "Science/Biology has a value of 120 and Art/Visual Arts also has a value of 120. Therefore, both have the same number of students enrolled.",
        "label": "Same"
    }
]
```
'''
        ]
    else:
        return [{"role": "system", "content": "Invalid prompt_id provided."}]
    