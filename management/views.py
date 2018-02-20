#from django.contrib.auth.decorators import login_required
#from django.http import HttpResponseRedirect

#from django.views.decorators.http import require_POST
#from django.shortcuts import render
from django.views import generic


#from .models import Charge

#@login_required

class IndexView(generic.TemplateView):
    template_name = 'management/management_list.html'
    '''
    model = Charge
    paginate_by = 1

    def get_context_data(self):
        """テンプレートへ渡す辞書の作成"""
        context = super().get_context_data()

        return context
'''
