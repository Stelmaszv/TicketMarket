from django.views.generic.base import TemplateView
from django.views.generic import (DeleteView,UpdateView)
from django.shortcuts import render,get_object_or_404,redirect
from core.getData import data
class baseListView(TemplateView):
    def get(self,request,*args,**kwargs):
        self.setContext(request)
        return render(request,self.template_name,self.context)
    def setContext(self,request):
        pass
class baseCreate(TemplateView):
    success_url = '/mycompany/'
    data=[]
    def get(self,request,id=None,*args, **kwargs):
        return self.addget(request)
    def addget(self,request):
        self.setContext(request)
        self.form = self.setform(request)
        return render(request, self.template_name, self.context)
    def setContext(self,request):
        self.items = data().set(request)
        self.context = {'form': self.form, 'items': self.items, 'adddata': self.data}
    def post(self,request, *args, **kwargs):
        self.setContext(request)
        self.form = self.setform(request)
        if self.form.is_valid():
            return self.basePostusbmit(request)
        else:
            self.setContext(request)
            return render(request, self.template_name, self.context)
        return render(request, self.template_name, self.context)
    def basePostusbmit(self,request):
        self.postInit(request)
        self.item=self.form.save()
        self.postSave(request)
        return redirect(self.success_url)
    def setform(self,request):
        return self.form(request.POST)
    def postInit(self,request,*args, **kwargs):
        pass
    def postSave(self,request, *args, **kwargs):
        pass
class baseShowView(TemplateView):
    def get(self,request,*args,**kwargs):
        self.context={'context':self.get_object()}
        return render(request,self.template,self.context)
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.getObject, id=id_)
class baseUpdateView(UpdateView):
    success_url = '/mycompany/'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.getObject, id=id_)
class baseDeleteView(DeleteView):
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.getObject, id=id_)
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.getObject, id=id_)
