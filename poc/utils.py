import matplotlib.pyplot as plt
import base64
from io import BytesIO


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_key(res_by):
    if res_by == 'Month':
        key = 'Month_of_Year'
    elif res_by == 'SuperRegion':
        key = 'super_region'
    elif res_by == 'SubRegion':
        key = 'sub_region'
    elif res_by == 'Region':
        key = 'region'
    elif res_by == 'LeadType':
        key = 'Lead_Type'
    return key


def get_plot(data, agg_col, chart_type='bar-chart', results_by='Month', **kwargs):
    plt.switch_backend('AGG')
    plt.figure(figsize=(12, 4))
    key = get_key(results_by)
    print(key)
    d = data.groupby(key, as_index=False)[agg_col].agg('count')
    if chart_type == 'bar-chart':
        plt.bar(d[key], d[agg_col])
        plt.title(f'plotting no of {agg_col} vs {key}')

    elif chart_type == 'pie-chart':
        plt.pie(data=d, x='lead_id', labels=d[key])
        plt.title(f'plotting no of {agg_col} vs {key}')

    elif chart_type == 'line-chart':
        plt.plot(d[key], d[agg_col], color='green', marker='o', linestyle='dashed')
        plt.title(f'plotting no of {agg_col} vs {key}')

    elif chart_type == '':
        print("Default bar chart ")
        plt.bar(d[key], d[agg_col])
        plt.title(f'plotting no of {agg_col} vs {key}')

    plt.tight_layout()
    chart = get_graph()
    return chart
