from django.shortcuts import render_to_response
from Apps.verbatim_templatetag import verbatim

class MainPage:
    @staticmethod
    def index_page(request):
        return render_to_response('index.html')