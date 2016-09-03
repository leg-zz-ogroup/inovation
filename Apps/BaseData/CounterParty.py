from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from django.core import serializers
# from django.http import JsonResponse
import json

from Apps.models import CounterpartyBaseInformation


class CounterParty(TemplateView):
    @staticmethod
    def index():
        return render_to_response('actual_counterparty_list_maker.html')

    @staticmethod
    def actual_counterparty_list_maker(request):
        if request.method == 'GET':
            actual_counterparty_list = CounterpartyBaseInformation.objects.only('ManualCode', 'Path', 'Address',
                                                                                'ActualCounterparty').filter(
                IsCounterpartyTypeActual=True).prefetch_related('Path', 'ActualCounterparty')
            for element in request.GET:
                # if element == 'ManualCode':
                #     actual_counterparty_list = actual_counterparty_list.filter(ManualCode=request.GET[element])
                filter_parameter = ''
                filter_criteria = request.GET[element]
                if element in ('ManualCode', 'Address'):
                    filter_parameter = element + '__contains'
                elif element in ('Name', 'Family', 'Job', 'IdNumber', 'FatherName', 'NationalCode'):
                    filter_parameter = 'ActualCounterparty__' + element + '__contains'
                elif element is 'PathName':
                    filter_parameter = 'Path__' + element + '__contains'
                elif element is 'RegionName':
                    filter_parameter = 'Path__Region__' + element + '__contains'
                elif element is 'CityName':
                    filter_parameter = 'Path__Region__City__' + element + '__contains'
                elif element is 'StateName':
                    filter_parameter = 'Path__Region__City__State__' + element + '__contains'
                if filter_parameter is not '':
                    actual_counterparty_list = actual_counterparty_list.filter(**{filter_parameter: filter_criteria})

            paged_actual_counterparty_list = Paginator(actual_counterparty_list,
                                                       request.GET.get('NumberOfRecordsInPage', 25))

            actual_counterparty_table_info = list()
            temp_actual_counterparty = TempObjectForActualParty()
            for actual_counterparty in paged_actual_counterparty_list.page(request.GET.get('PageNumber', 1)):
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

            return HttpResponse(json.dumps(
                [any_actual_counterparty.__dict__ for any_actual_counterparty in actual_counterparty_table_info]))
        else:
            return HttpResponse()


class TempObjectForActualParty:
    code = None
    name = None
    family = None
    job = None
    state = None
    city = None
    region = None
    path = None
    address = None
