from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView

from Apps.models import CounterpartyBaseInformation


class CounterParty(TemplateView):
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

            return render_to_response('actual_counterparty_list_maker.html',
                                      {'counterparty_list': actual_counterparty_table_info},
                                      context_instance=RequestContext(request))


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
