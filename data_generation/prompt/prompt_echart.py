import json
def get_prompt_vega(method, chart_type, original_vl_code, topics_pool):
    if chart_type == "100_stacked_bar_chart":
        return [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and echart."},
        {"role": "user", "content": "Given the following echart code of a percentage (100%) stacked bar chart: " + original_vl_code +
         " Please generate a diversified version of this echart code of percentage stacked bar. Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data point with new corresponding values to enrich the visualization.\
            print the final table data you use in the code within triple backticks (```), and don't include things like csv, plaintext in the triple backticks (```).\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width of bars reasonably\
            5. change width and height of the chart reasonably\
            6. change the direction of chart (vertical to horizontal or vertical to horizontal)\
            7. change the band width/height for bars e.g. height/width : band : band height/width\
            8. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " \
            Do not use random data\
            different data points should have different values\
            you only need to generate code start from 'var dom = document.getElementById('container');' and  end at 'if (option && typeof option === 'object') myChart.setOption(option);', make sure you include these two in your code\
            You should give FULL code with ALL datapoints and don't miss any detail\
            I need you to generate vertical percentage (100%) stacked bar chart this time so the chart have to be vertical not horizontal\
            print table data first, the table data format should be able to directly write in csv file, then print your code\
            Include the code with ``` ``` format."}
        ]
    elif chart_type == "area_chart":
        return [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and echart."},
        {"role": "user", "content": "Given the following echart code of a area chart: " + original_vl_code +
         " Please generate a diversified version of this echart code of an area chart. Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data point with new corresponding values to enrich the visualization.\
            print the final table data you use in the code within triple backticks (```), and don't include things like csv, plaintext in the triple backticks (```).\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width and height of the chart reasonably\
            5. Assign numerical/text label/annotation in the chart.\
            6. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic \
            Do not use random data\
            different data points should have different values\
            you only need to generate code start from 'var dom = document.getElementById('container');' and  end at 'if (option && typeof option === 'object') myChart.setOption(option);', make sure you include these two in your code\
            You should give FULL code with ALL datapoints and don't miss any detail\
            print table data first, the table data format should be able to directly write in csv file, then print your code\
            Include the code with ``` ``` format."}

        ]
    elif chart_type == "bar_chart":
        return [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and echart."},
        {"role": "user", "content": "Given the following echart code of a bar chart: " + original_vl_code +
         " Please generate a diversified version of this echart code of an bar chart. Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data point with new corresponding values to enrich the visualization.\
            print the final table data you use in the code within triple backticks (```), and don't include things like csv, plaintext in the triple backticks (```).\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width and height of the chart reasonably\
            5. Assign numerical/text label/annotation in the chart.\
            6. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic \
            Do not use random data\
            7. change the band width/height for bars\
            8. change the width of bars\
            different data points should have different values\
            do not skip any eneity text label in the axis\
            I want you to generate vertical bar this time, so the bar chart has to be vertical\
            you only need to generate code start from 'var dom = document.getElementById('container');' and  end at 'if (option && typeof option === 'object') myChart.setOption(option);', make sure you include these two in your code\
            You should give FULL code with ALL datapoints and don't miss any detail\
            print table data first, the table data format should be able to directly write in csv file, then print your code\
            Include the code with ``` ``` format."}
        ]
    elif chart_type == "histogram":
        return [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and echart."},
        {"role": "user", "content": "Given the following echart code of a histogram: " +original_vl_code +
         " Please generate a diversified version of this echart code of an histogram. Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data point with new corresponding values to enrich the visualization.\
            print the final table data you use in the code within triple backticks (```), and don't include things like csv, plaintext in the triple backticks (```).\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width and height of the chart reasonably\
            5. Assign numerical/text label/annotation in the chart.\
            6. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic and use specific things as topic for example  not just 'Future Technologies & Society' but some specific in this broad topic\
            Do not use random data\
            7. change the band width/height for bars\
            8. change the width of bars\
            different data points should have different values\
            you are generating histogram, so the table data you generated should be only one single numerical column! , and should use bin to seperate data, and use frequency as another axis\
            you only need to generate code start from 'var dom = document.getElementById('container');' and  end at 'if (option && typeof option === 'object') myChart.setOption(option);', make sure you include these two in your code\
            You should give FULL code with ALL datapoints and don't miss any detail\
            print table data first, the table data format should be able to directly write in csv file, then print your code\
            Include the code with ``` ``` format."}

        ]
    elif chart_type == "line_chart":
        return [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and echart."},
        {"role": "user", "content": "Given the following echart code of a line chart: " + original_vl_code +
         " Please generate a diversified version of this echart code of an line chart. Specificly, I want you to only generate the case that the y axis becomes higher from up to down, which inverse: true in yaxis must be in your code. Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data point with new corresponding values to enrich the visualization.\
            print the final table data you use in the code within triple backticks (```), and don't include things like csv, plaintext in the triple backticks (```).\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width and height of the chart reasonably\
            5. Assign numerical/text label/annotation in the chart.\
            6. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic, do not use tempreture. \
            Do not use random data\
            Do not generate area chart\
            different data points should have different values\
            you only need to generate code start from 'var dom = document.getElementById('container');' and  end at 'if (option && typeof option === 'object') myChart.setOption(option);', make sure you include these two in your code\
            You should give FULL code with ALL datapoints and don't miss any detail\
            print table data first, the table data format should be able to directly write in csv file, then print your code\
            Include the code with ``` ``` format."}
        ]
    elif chart_type == "pie_chart":
        return [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and echart."},
        {"role": "user", "content": "Given the following echart code of a pie chart: " + original_vl_code +
         " Please generate a diversified version of this echart code of an pie chart. Here are some options you should follow:\
            1. Generate data points that fit the pie chart, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data point with new corresponding values to enrich the visualization.\
            print the final table data you use in the code within triple backticks (```), and don't include things like csv, plaintext in the triple backticks (```).\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic and use specific things as topic for example  not just 'Future Technologies & Society' but some specific in this broad topic\
            5. keep distance between legend and pie so that text won't overlap.\
            6. assign numerical annotation.\
            Do not use random data\
            you only need to generate code start from 'var dom = document.getElementById('container');' and  end at 'if (option && typeof option === 'object') myChart.setOption(option);', make sure you include these two in your code\
            You should give FULL code with ALL datapoints and don't miss any detail\
            print table data first, the table data format should be able to directly write in csv file, then print your code\
            Include the code with ``` ``` format."}
        ]
    elif chart_type == "scatterplot":
        return [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and echart."},
        {"role": "user", "content": "Given the following echart code of a scatterplot: " + original_vl_code +
         " Please generate a diversified version of this echart code of an scatterplot. Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data point with new corresponding values to enrich the visualization.\
            print the final table data you use in the code within triple backticks (```), and don't include things like csv, plaintext in the triple backticks (```).\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width and height of the chart reasonably\
            5. place the legend in appropriate place that does not overlap with other things.\
            6. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic and use specific things as topic for example  not just 'Future Technologies & Society' but some specific in this broad topic\
            Do not use random data\
            7. I want you to generate data in downward way, but do not generate too simple downward data, make some variation and occlusion\
            different data points should have different values\
            you only need to generate code start from 'var dom = document.getElementById('container');' and  end at 'if (option && typeof option === 'object') myChart.setOption(option);', make sure you include these two in your code\
            You should give FULL code with ALL datapoints and don't miss any detail\
            print table data first, the table data format should be able to directly write in csv file, then print your code\
            Include the code with ``` ``` format."}

        ]
    elif chart_type == "stacked_area_chart":
        return [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and echart."},
        {"role": "user", "content": "Given the following echart code of a stacked area chart: " + original_vl_code +
         " Please generate a diversified version of this echart code of an stacked area chart. Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data point with new corresponding values to enrich the visualization.\
            print the final table data you use in the code within triple backticks (```), and don't include things like csv, plaintext in the triple backticks (```).\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width and height of the chart reasonably\
            5. Assign numerical/text label/annotation in the chart.\
            6. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic and use specific things as topic for example  not just 'Future Technologies & Society' but some specific in this broad topic\
            7. have more complex trend of data, can be upward,downward,middle up, middle down, and the the data should have variance for example not just directly down rather have some waves.\
            Do not use random data\
            different data points should have different values\
            you only need to generate code start from 'var dom = document.getElementById('container');' and  end at 'if (option && typeof option === 'object') myChart.setOption(option);', make sure you include these two in your code\
            You should give FULL code with ALL datapoints and don't miss any detail\
            print table data first, the table data format should be able to directly write in csv file, then print your code\
            Include the code with ``` ``` format."}
        ]
    elif chart_type == "stacked_bar_chart":
        return [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and echart."},
        {"role": "user", "content": "Given the following echart code of a stacked bar chart: " + original_vl_code +
         " Please generate a diversified version of this echart code of a stacked bar chart. Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data point with new corresponding values to enrich the visualization.\
            print the final table data you use in the code within triple backticks (```), and don't include things like csv, plaintext in the triple backticks (```).\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width and height of the chart reasonably\
            5. Assign numerical/text label/annotation in the chart.\
            6. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic and use specific things as topic for example  not just 'Future Technologies & Society' but some specific in this broad topic\
            Do not use random data\
            7. change the band width/height for bars\
            8. change the width of bars\
            9. I want you to generate \
            different data points should have different values\
            do not skip any eneity text label in the axis\
            you only need to generate code start from 'var dom = document.getElementById('container');' and  end at 'if (option && typeof option === 'object') myChart.setOption(option);', make sure you include these two in your code\
            You should give FULL code with ALL datapoints and don't miss any detail\
            print table data first, the table data format should be able to directly write in csv file, then print your code\
            Include the code with ``` ``` format."}
        ]
    elif chart_type == "tree_map":
        return [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and echart."},
        {"role": "user", "content": "Given the following echart code of a treemap: " + original_vl_code +
         " Please generate a diversified version of this echart code of an treemap. Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data point with new corresponding values to enrich the visualization.\
            print the final table data you use in the code within triple backticks (```), and don't include things like csv, plaintext in the triple backticks (```).\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width and height of the chart reasonably\
            5. assign numerical annotation in the chart\
            6. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you should randomly choose one of the topic from:( " +str(topics_pool) + ") but reduce using global...topic and use specific things as topic for example  not just 'Future Technologies & Society' but some specific in this broad topic\
            Do not use random data\
            different data points should have different values\
            you only need to generate code start from 'var dom = document.getElementById('container');' and  end at 'if (option && typeof option === 'object') myChart.setOption(option);', make sure you include these two in your code\
            You should give FULL code with ALL datapoints and don't miss any detail\
            print table data first, the table data format should be able to directly write in csv file, then print your code\
            Include the code with ``` ``` format."}
        ]
    else:
        return [{"role": "system", "content": "Invalid prompt_id provided."}]