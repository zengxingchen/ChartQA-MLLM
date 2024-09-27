import json
def get_prompt_vega(method, chart_type, original_vl_code, topics_pool):
    if chart_type == "100_stacked_bar_chart":
        return [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and Vega-Lite."},
        {"role": "user", "content": "Given the following Vega-Lite code of a percentage (100%) stacked bar chart: " + json.dumps(original_vl_code) +
         " Please generate a diversified version of this Vega-Lite code of percentage stacked bar. Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data point with new corresponding values to enrich the visualization.\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width of bars reasonably\
            5. change width and height of the chart reasonably\
            6. change the direction of chart (vertical to horizontal or vice versa)\
            7. change the band width/height for bars e.g. height/width : band : band height/width\
            8. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic. The real topic you choose should be specific not the general topic I gave. \
            It is really important that do not miss the ''field'' assignment of x or y axis! After generating the code, you must check that the data fields of x and y axis are correctly bound to the corresponding axes, if not, complement the field! \
            use transformations(like fold in form of ''fold'':[], ''as'':[]) as needed\
            You should choose some of these options not all of them to diversfy the visualization\
            different data points should have different values\
            avoid using 'aggregate': 'sum' in the code\
            You should give FULL code with ALL datapoints and don't miss any detail\
            Include the code with ```json ``` format."}
        ]
    elif chart_type == "area_chart":
        return [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and Vega-Lite."},
        {"role": "user", "content": "Given the following Vega-Lite code of chart related to area chart: " + json.dumps(original_vl_code) +
         " Please generate a diversified version of this Vega-Lite code.Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some entities with new corresponding values to enrich the visualization.\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            5. change width and height of the chart reasonably\
            6. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic,do not use temperature \
            You should choose some of these options not all of them to diversfy the visualization\
            7. add numerical annotation in the chart\
            bring more variety of data points to show characteristics of the area chart\
            You should give FULL code with ALL data points and don't miss any detail\
            Include the code with ```json ``` format."}

        ]
    elif chart_type == "bar_chart":
        return [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and Vega-Lite."},
        {"role": "user", "content": "Given the following Vega-Lite code of chart related to bar: " + json.dumps(original_vl_code) +
         " Please generate a diversified version of this Vega-Lite code with quantitative label. Here are some options you should follow:\
            1. Generate data points that fit the chart. Specificly, I want you to generate truncated bar chart, that by setting the scale property in the y channel to start from a specific value other than zero. You should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some entities with new corresponding values to enrich the visualization.\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width of bars reasonably\
            5. change width and height of the chart reasonably\
            6. change the direction of chart (vertical to horizontal or vice versa)\
            7. change the band width/height for bars e.g. height/width : band : band height/width\
            8. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic \
            9. assign text label in the chart of bars.\
            You should choose some of these options not all of them to diversfy the visualization\
            You should give FULL code with ALL datapoints and don't miss any detail\
            Include the code with ```json ``` format."}
        ]
    elif chart_type == "bubble_chart":
        return [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and Vega-Lite."},
        {"role": "user", "content": "Given the following Vega-Lite code of chart related to bubble chart: " + json.dumps(original_vl_code) +
         " Please generate a diversified bubble chart code of this Vega-Lite code.Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data points with new corresponding values to enrich the visualization.\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width and height of the chart reasonably\
            5. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic \
            You should choose some of these options not all of them to diversfy the visualization\
            You should give FULL code with ALL data points and don't miss any detail\
            Include the code with ```json ``` format."}
        ]
    elif chart_type == "histogram":
        return [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and Vega-Lite."},
        {"role": "user", "content": "Given the following Vega-Lite code of chart related to a histogram: " + json.dumps(original_vl_code) +
         " Please generate a diversified histogram. Here are some options you should follow:\
            1. Generate meaningful data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data point with new corresponding values to enrich the visualization.\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width of bars reasonably\
            5. change width and height of the chart reasonably\
            6. change the band width/height for bars e.g. height/width : band : band height/width\
            7. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic \
            You should choose some of these options not all of them to diversfy the visualization\
            You should give FULL code with ALL datapoints and don't miss any detail\
            Include the code with ```json ``` format."}

        ]
    elif chart_type == "line_chart":
        return [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and Vega-Lite."},
        {"role": "user", "content": "Given the following Vega-Lite code of chart related to line: " + json.dumps(original_vl_code) +
         " Please generate a diversified line chart of this Vega-Lite code. Specificly, I want you to only generate the case that the y axis becomes higher from up to down, which means you need to have scale: reverse: true'\
            }. Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some entities with new corresponding values to enrich the visualization.\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width and height of the chart reasonably\
            5. change the topic,headline and data type (which fit the topic) of the chart, you should choose one of the topic from: " +str(topics_pool) + " \
            6. assign label in the line chart indicate the specific number.\
            You should choose some of these options not all of them to diversfy the visualization\
            You should give FULL code with ALL datapoints and don't miss any detail\
            Don't change to other chart type\
            Don't wrongly use layer as specifications inside layer cannot use row and column channels as layering facet specifications is not allowed.\
            Include the code with ```json ``` format."}
        ]
    elif chart_type == "pie_chart":
        return [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and Vega-Lite."},
        {"role": "user", "content": "Given the following Vega-Lite code of chart related to pie: " + json.dumps(original_vl_code) +
         " Please generate a diversified pie chart of this Vega-Lite code with text labeling. Here are some options you should follow:\
            1. Generate data points that fit the chart, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some entities with new corresponding values to enrich the visualization.\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width and height of the chart reasonably\
            5. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic \
            You should choose some of these options not all of them to diversify the visualization\
            Do not add text mark\
            You should give FULL code with ALL datapoints and don't miss any detail\
            Include the code with ```json ``` format."}
        ]
    elif chart_type == "scatterplot":
        return [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and Vega-Lite."},
        {"role": "user", "content": "Given the following Vega-Lite code of chart related to scatter plot: " + json.dumps(original_vl_code) +
         " Please generate a diversified bubble chart code of this Vega-Lite code.Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some entities with new corresponding values to enrich the visualization.\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width and height of the chart reasonably\
            5. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic \
            We are not generating bubble chart, so the size of point should be same for each point.\
            You should choose some of these options not all of them to diversfy the visualization\
            You should give FULL code with ALL data points and don't miss any detail\
            Do not draw points too small, set the size of point that easy to read\
            Include the code with ```json ``` format."}

        ]
    elif chart_type == "stacked_area_chart":
        return [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and Vega-Lite."},
        {"role": "user", "content": "Given the following Vega-Lite code of a stacked area chart: " + json.dumps(original_vl_code) +
         " Please generate a diversified version of this Vega-Lite code.Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some entities with new corresponding values to enrich the visualization.\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            5. change width and height of the chart reasonably\
            6. Experiment with the opacity of the area fill to balance the emphasis between the area volume and the underlying grid or background elements.\
            7. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic \
            You should choose some of these options not all of them to diversfy the visualization\
            bring more variety of data points to show characteristics of the area chart\
            You should give FULL code with ALL data points and don't miss any detail\
            Include the code with ```json ``` format."}
        ]
    elif chart_type == "stacked_bar_chart":
        return [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and Vega-Lite."},
        {"role": "user", "content": "Given the following Vega-Lite code of a stacked bar: " + json.dumps(original_vl_code) +
         " Please generate a diversified version of this Vega-Lite code of stacked bar. Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some data points with new corresponding values to enrich the visualization.\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width of bars reasonably\
            5. change width and height of the chart reasonably\
            6. change the direction of chart (vertical to horizontal or vice versa)\
            7. change the band width/height for bars e.g. height/width : band : band height/width\
            8. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic \
            It is really important that do not miss the ''field'' assignment of x or y axis! After generating the code, you must check that the data fields of x and y axis are correctly bound to the corresponding axes, if not, complement the field! \
            use transformations(like fold in form of ''fold'':[], ''as'':[]) as needed\
            You should choose some of these options not all of them to diversfy the visualization\
            avoid using 'aggregate': 'sum' in the code\
            You should give FULL code with ALL datapoints and don't miss any detail\
            Include the code with ```json ``` format."}
        ]
    else:
        return [{"role": "system", "content": "Invalid prompt_id provided."}]