from django.views.generic.base import TemplateView
from django.shortcuts import render,get_object_or_404
class baseShowView(TemplateView):
    def get(self,request,*args,**kwargs):
        context={'context':self.get_object()}
        return render(request,self.template,context)
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj