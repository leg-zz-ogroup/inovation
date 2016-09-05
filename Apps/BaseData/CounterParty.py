from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from django.core import serializers
import json


from Apps.models import CounterpartyBaseInformation
from Apps.models import CustomerGroup


class CounterParty(TemplateView):
    @staticmethod
    def index(request):
        return render_to_response('actual_counterparty_list_maker.html')
    @staticmethod
    def actual_counterparty_list_maker(request):
        if request.method == 'GET':
            actual_counterparty_list = CounterpartyBaseInformation.objects.only('ManualCode', 'Path', 'Address',
                                                                                'ActualCounterparty').filter(
                IsCounterpartyTypeActual=True).prefetch_related('Path', 'ActualCounterparty')
            actual_counterparty_table_info = list()
            temp_actual_counterparty = TempObjectForActualParty()
            for actual_counterparty in actual_counterparty_list:
                temp_actual_counterparty.code = actual_counterparty.ManualCode
                temp_actual_counterparty.name = actual_counterparty.ActualCounterparty.Name
                temp_actual_counterparty.family = actual_counterparty.ActualCounterparty.Family
                temp_actual_counterparty.job = actual_counterparty.ActualCounterparty.Job
                temp_actual_counterparty.state = actual_counterparty.Path.Region.City.State.StateName
                temp_actual_counterparty.city = actual_counterparty.Path.Region.City.CityName
                temp_actual_counterparty.region = actual_counterparty.Path.Region.RegionName
                temp_actual_counterparty.path = actual_counterparty.Path.PathName
                temp_actual_counterparty.address = actual_counterparty.Address

                actual_counterparty_table_info.append(temp_actual_counterparty)

            return HttpResponse(json.dumps([any_actual_counterparty.__dict__ for any_actual_counterparty in actual_counterparty_table_info]))

    @staticmethod
    def counter_group_maker(request):
        if request.method == 'GET':
            counter_group_list = CustomerGroup.objects.only("Name")
            counter_group_list_info = list()
            temp_counter_group = TempObjectForCounterGroup()
            for counter_group in counter_group_list:
                temp_counter_group.id = counter_group.id
                temp_counter_group.name = counter_group.Name

                counter_group_list_info.append(temp_counter_group)

            return HttpResponse(json.dumps([any_counter_group.__dict__ for any_counter_group in counter_group_list_info]))

class TempObjectForActualParty():
    code = None
    name = None
    family = None
    job = None
    state = None
    city = None
    region = None
    path = None
    address = None

class TempObjectForCounterGroup():
    id = None
    name = None
