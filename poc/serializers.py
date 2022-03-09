from rest_framework import serializers
from .models import SfdcLead


class SfdcLeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SfdcLead
        fields = ['year_created', 'Month_of_Year', 'super_region', 'sub_region', 'region', 'Lead_Type', 'lead_id']


