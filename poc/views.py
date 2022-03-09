import os
from pathlib import Path
from django.shortcuts import render
from rest_framework.reverse import reverse
from .models import SfdcLead
from .serializers import SfdcLeadSerializer
from django.views.generic import View
from rest_framework import generics
from rest_framework.response import Response
from .utils import get_plot
import pandas as pd

sql_base_dir = os.path.join(Path(__file__).resolve().parent, 'sqls')

# read sfdc_lead sql file
raw_sfdc_lead_sql_path = os.path.join(sql_base_dir, 'sfdc_lead.sql')
raw_sfdc_lead_sql_file = open(raw_sfdc_lead_sql_path)
sfdc_lead_sql_file_read = raw_sfdc_lead_sql_file.read()


# creating root api for home page
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        api_root_json = {
            'sfdc_leads': reverse(SfdcLeadListView.name, request=request),
            'vizualize_data': reverse(HomeView.name, request=request)
        }
        return Response(api_root_json)


class SfdcLeadListView(generics.ListCreateAPIView):
    queryset = SfdcLead.objects.raw(sfdc_lead_sql_file_read)
    serializer_class = SfdcLeadSerializer
    name = 'sfdc-api-list'


class HomeView(View):
    name = 'home-viz'

    def get(self, request, *args, **kwargs):
        sfdc_lead_qs = SfdcLead.objects.raw(sfdc_lead_sql_file_read)
        sfdc_lead_dict = dict()
        sfdc_lead_df = pd.DataFrame()
        # print(sfdc_lead_df)
        for item in sfdc_lead_qs:
            # print(item.lead_id, item.super_region, item.sub_region, item.region)
            sfdc_lead_dict['lead_id'] = item.lead_id
            sfdc_lead_dict['year_created'] = item.year_created
            sfdc_lead_dict['Month_of_Year'] = item.Month_of_Year
            sfdc_lead_dict['super_region'] = item.super_region
            sfdc_lead_dict['sub_region'] = item.sub_region
            sfdc_lead_dict['region'] = item.region
            sfdc_lead_dict['Lead_Type'] = item.Lead_Type
            # print(sfdc_lead_dict)
            sfdc_lead_df = sfdc_lead_df.append(sfdc_lead_dict, ignore_index=True)

        chart_bar1 = get_plot(data=sfdc_lead_df, agg_col='lead_id', chart_type='bar-chart', results_by='Region')
        chart_bar2 = get_plot(data=sfdc_lead_df, agg_col='lead_id', chart_type='bar-chart', results_by='SuperRegion')
        chart_pie = get_plot(data=sfdc_lead_df, agg_col='lead_id', chart_type='pie-chart', results_by='LeadType')
        chart_line = get_plot(data=sfdc_lead_df, agg_col='lead_id', chart_type='line-chart')
        context = {'chart1': chart_bar1, 'chart2': chart_bar2, 'chart3': chart_pie,
                   'chart4': chart_line}
        return render(request, 'poc/index.html', context)
