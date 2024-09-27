def get_prompt_python(method, chart_type, original_vl_code, topics_pool):
    if chart_type == "100_stacked_bar_chart":
        return [
         {"role": "system", "content": f"You are a highly intelligent AI familiar with data visualization and {method}."},
         {"role": "user", "content": f"Given the following {method} code of a percentage (100%) stacked bar chart: " + original_vl_code +
         f" Please generate a diversified version of this {method} code of percentage stacked bar. Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data point with new corresponding values to enrich the visualization.\
            print the final table data you use in the code within triple backticks (```), and don't include things like csv, plaintext in the triple backticks (```).\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width of bars reasonably\
            5. change width and height of the chart reasonably\
            6. change the direction of chart (vertical to horizontal or vice versa)\
            7. change the band width/height for bars e.g. height/width : band : band height/width\
            8. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic \
            Do not use random data\
            I want you to generate vertical chart this time\
            You should choose some of these options not all of them to diversfy the visualization\
            different data points should have different values\
            You should give FULL code with ALL datapoints and don't miss any detail\
            print table data first, the table data format should be able to directly write in csv file, then print your code\
            Include the code with ``` ``` format."}
        ]
    elif chart_type == "area_chart":
        return [
         {"role": "system", "content": f"You are a highly intelligent AI familiar with data visualization and {method}."},
         {"role": "user", "content": f"Given the following {method} code of a area chart: " + original_vl_code +
         f" Please generate a diversified version of this {method} code of area chart. Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data point with new corresponding values to enrich the visualization.\
            print the final table data you use in the code within triple backticks (```), and don't include things like csv, plaintext in the triple backticks (```).\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width and height of the chart reasonably\
            5. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic, do not use tempreture \
            6. generate only area chart with one column of value not stacked area chart.\
            7. assign annotation/text label on the chart.\
            Do not use random data\
            You should choose some of these options not all of them to diversfy the visualization\
            different data points should have different values\
            You should give FULL code with ALL datapoints and don't miss any detail\
            print table data first, the table data format should be able to directly write in csv file, then print your code\
            Include the code with ``` ``` format."}

        ]
    elif chart_type == "bar_chart":
        return [
        {"role": "system", "content": f"You are a highly intelligent AI familiar with data visualization and {method}."},
        {"role": "user", "content": f"Given the following {method} code of a bar chart: " + original_vl_code +
         f" Please generate a diversified version of this {method} code of bar chart. Specificly, I want you to generate truncated bar chart, that to let y axis start from a specific value other than zero, by setting the y-axis limits using the set_ylim() method.Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data point with new corresponding values to enrich the visualization.\
            print the final table data you use in the code within triple backticks (```), and don't include things like csv, plaintext in the triple backticks (```).\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width of bars reasonably\
            5. change width and height of the chart reasonably\
            6. change the direction of chart (vertical to horizontal or vice versa)\
            7. change the band width/height for bars e.g. height/width : band : band height/width\
            8. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic \
            Do not use random data\
            Do not generate stacked bar\
            You should choose some of these options not all of them to diversfy the visualization\
            different data points should have different values\
            You should give FULL code with ALL datapoints and don't miss any detail\
            print table data first, the table data format should be able to directly write in csv file, then print your code\
            Include the code with ``` ``` format."}
        ]
    elif chart_type == "bubble_chart":
        return [
        {"role": "system", "content": f"You are a highly intelligent AI familiar with data visualization and {method}."},
        {"role": "user", "content": f"Given the following {method} code of a bubble chart: " + original_vl_code +
         f" Please generate a diversified version of this {method} code of bubble chart. Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data point with new corresponding values to enrich the visualization.\
            print the final table data you use in the code within triple backticks (```), and don't include things like csv, plaintext in the triple backticks (```).\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width and height of the chart reasonably\
            5. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic \
            Do not use random data\
            You should choose some of these options not all of them to diversfy the visualization\
            different data points should have different values\
            You should give FULL code with ALL datapoints and don't miss any detail\
            print table data first, the table data format should be able to directly write in csv file, then print your code\
            Include the code with ``` ``` format."}
        ]
    elif chart_type == "histogram":
        return [
        {"role": "system", "content": f"You are a highly intelligent AI familiar with data visualization and{method}."},
        {"role": "user", "content": f"Given the following {method} code of a histogram chart: " + original_vl_code +
         f" Please generate a diversified version of this {method} code of histogram chart. Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data point with new corresponding values to enrich the visualization.\
            print the final table data you use in the code within triple backticks (```), and don't include things like csv, plaintext in the triple backticks (```).\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width of histograms reasonably\
            5. change width and height of the chart reasonably\
            6. change the direction of chart (vertical to horizontal or vice versa)\
            7. change the band width/height for histograms e.g. height/width : band : band height/width\
            8. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic \
            Do not use random data\
            You are generating histogram, so the table data should one single numerical column, and you should bin the data and count the frequency.\
            You should choose some of these options not all of them to diversfy the visualization\
            different data points should have different values\
            You should give FULL code with ALL datapoints and don't miss any detail\
            print table data first, the table data format should be able to directly write in csv file, then print your code\
            Include the code with ``` ``` format."}

        ]
    elif chart_type == "line_chart":
        return [
        {"role": "system", "content": f"You are a highly intelligent AI familiar with data visualization and {method}."},
        {"role": "user", "content": f"Given the following {method} code of a line chart: " + original_vl_code +
         f" Please generate a diversified version of this {method} code of line chart. Here are some options you should follow:\
            1. Generate data points that fit the chart.Specificly, I want you to only generate the case that the y axis becomes higher from up to down, invert_yaxis() must be in your code. you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data point with new corresponding values to enrich the visualization.\
            print the final table data you use in the code within triple backticks (```), and don't include things like csv, plaintext in the triple backticks (```).\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width and height of the chart reasonably\
            5. change the trend of data (down/up/cross)\
            6. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic， do not use tempreture. \
            7. assign annotation/label in the chart\
            Do not use random data\
            You should choose some of these options not all of them to diversfy the visualization\
            different data points should have different values\
            You should give FULL code with ALL datapoints and don't miss any detail\
            print table data first, the table data format should be able to directly write in csv file, then print your code\
            Include the code with ``` ``` format."}
        ]
    elif chart_type == "pie_chart":
        return [
        {"role": "system", "content": f"You are a highly intelligent AI familiar with data visualization and {method}."},
        {"role": "user", "content": f"Given the following {method} code of a pie chart: " + original_vl_code +
         f" Please generate a diversified version of this {method} code of pie chart. Here are some options you should follow:\
            1. Generate data points that fit the pie chart (not too much datapoint), but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data point with new corresponding values to enrich the visualization.\
            print the final table data you use in the code within triple backticks (```), and don't include things like csv, plaintext in the triple backticks (```).\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width and height of the chart reasonably\
            5. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic \
            Do not use random data\
            You should choose some of these options not all of them to diversfy the visualization\
            different data points should have different values\
            You should give FULL code with ALL datapoints and don't miss any detail\
            print table data first, the table data format should be able to directly write in csv file, then print your code\
            Include the code with ``` ``` format."}
        ]
    elif chart_type == "scatterplot":
        return [
        {"role": "system", "content": f"You are a highly intelligent AI familiar with data visualization and {method}."},
        {"role": "user", "content": f"Given the following {method} code of a  scatterplot: " + original_vl_code +
         f" Please generate a diversified version of this {method} code of scatterplot. Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data point with new corresponding values to enrich the visualization.\
            print the final table data you use in the code within triple backticks (```), and don't include things like csv, plaintext in the triple backticks (```).\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width and height of the chart reasonably\
            5. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic, do not use temperature \
            6. the scatter data should be real, like 'scatter' not simply form a line.\
            Do not use random data\
            You should choose some of these options not all of them to diversfy the visualization\
            different data points should have different values\
            You should give FULL code with ALL datapoints and don't miss any detail\
            print table data first, the table data format should be able to directly write in csv file, then print your code\
            Include the code with ``` ``` format."}

        ]
    elif chart_type == "stacked_area_chart":
        return [
        {"role": "system", "content": f"You are a highly intelligent AI familiar with data visualization and {method}."},
        {"role": "user", "content": f"Given the following {method} code of a stacked area chart: " + original_vl_code +
         f" Please generate a diversified version of this {method} code of stacked area chart. Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data point with new corresponding values to enrich the visualization.\
            print the final table data you use in the code within triple backticks (```), and don't include things like csv, plaintext in the triple backticks (```).\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width and height of the chart reasonably\
            5. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic \
            6. assign annotation/text label on the chart.\
            7. do not miss the legend.\
            Do not use random data\
            You should choose some of these options not all of them to diversfy the visualization\
            different data points should have different values\
            You should give FULL code with ALL datapoints and don't miss any detail\
            print table data first, the table data format should be able to directly write in csv file, then print your code\
            Include the code with ``` ``` format."}
        ]
    elif chart_type == "stacked_bar_chart":
        return [
        {"role": "system", "content": f"You are a highly intelligent AI familiar with data visualization and {method}."},
        {"role": "user", "content": f"Given the following {method} code of a stacked bar chart: " + original_vl_code +
         f" Please generate a diversified version of this {method} code of stacked bar chart. Here are some options you should follow:\
            1. Generate data points that fit the chart, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data point with new corresponding values to enrich the visualization.\
            print the final table data you use in the code within triple backticks (```), and don't include things like csv, plaintext in the triple backticks (```).\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width of bars reasonably\
            5. change width and height of the chart reasonably\
            6. change the direction of chart (vertical to horizontal or vice versa)\
            7. change the band width/height for bars e.g. height/width : band : band height/width\
            8. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic \
            9. assign numerical label of each bar.\
            Do not use random data\
            You should choose some of these options not all of them to diversfy the visualization\
            different data points should have different values\
            You should give FULL code with ALL datapoints and don't miss any detail\
            print table data first, the table data format should be able to directly write in csv file, then print your code\
            Include the code with ``` ``` format."}
        ]
    elif chart_type == "tree_map":
        return [
        {"role": "system", "content": f"You are a highly intelligent AI familiar with data visualization and {method}."},
        {"role": "user", "content": f"Given the following {method} code of a treemap: " + original_vl_code +
         f" Please generate a diversified version of this {method} code of treemap. Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data point with new corresponding values to enrich the visualization.\
            print the final table data you use in the code within triple backticks (```), and don't include things like csv, plaintext in the triple backticks (```).\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width and height of the chart reasonably\
            5. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic \
            Do not use random data\
            You should choose some of these options not all of them to diversfy the visualization\
            different data points should have different values\
            You should give FULL code with ALL datapoints and don't miss any detail\
            print table data first, the table data format should be able to directly write in csv file, then print your code\
            Include the code with ``` ``` format."}
        ]
    else:
        return [{"role": "system", "content": "Invalid prompt_id provided."}]

