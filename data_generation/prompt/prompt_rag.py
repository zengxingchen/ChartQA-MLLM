import json
def get_prompt_rag_echart(chart_type, table_data_records, seed_vl_codes):
    return [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and echart."},
        {"role": "user", "content": " Here is some chart table data:" + str(table_data_records) + "and examples of echart code that you can refer to the visual encoding: " + seed_vl_codes[0] + seed_vl_codes[1]  + seed_vl_codes[2]  +
         f" Please generate a diversified echart code of a {chart_type} based on the given table data and examples, use as diversified visual encoding in the example as possible.\
           You should give code with all detail and don's miss any data points.\
           you only need to generate code start from 'var dom = document.getElementById('container');' and  end at 'if (option && typeof option === 'object') myChart.setOption(option);', make sure you include these two in your code\
            Include the code with ``` ``` format."}
        ]
def get_prompt_rag_vega(chart_type, table_data_records, seed_vl_code1, seed_vl_code2, seed_vl_code3):
    return [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and Vega-Lite."},
        {"role": "user", "content": " Here is some chart table data:" + str(table_data_records) + "and examples of vega-lite code that you can refer to the visual encoding: " + json.dumps(seed_vl_code1) + json.dumps(seed_vl_code2)  + json.dumps(seed_vl_code3)  +
         f" Please generate a diversified Vega-Lite code of a {chart_type} based on the given table data and examples, use as diversified visual encoding in the example as possible.\
           You should give code with all detail and don's miss any data points.\
            It is really important that do not miss the ''field'' assignment of x or y axis! After generating the code, you must check that the data fields of x and y axis are correctly bound to the corresponding axes, if not, complement the field! \
            Include the code with ```json ``` format."}
        ]
def get_prompt_rag_python(method, chart_type, table_data_records, seed_vl_codes):
    return [
        {"role": "system", "content": f"You are a highly intelligent AI familiar with data visualization and {method}."},
        {"role": "user", "content": " Here is some chart table data:" + str(table_data_records) + f"and examples of {method} code that you can refer to the visual encoding: " + seed_vl_codes[0] + seed_vl_codes[1]  + seed_vl_codes[2]  +
         f" Please generate a diversified {method} code of a {chart_type} based on the given table data and examples, use as diversified visual encoding in the example as possible.\
           You should give code with all detail and don's miss any data points.\
            Include the code with ``` ``` format."}
        ]