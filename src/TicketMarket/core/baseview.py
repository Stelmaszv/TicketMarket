from django.views.generic.base import TemplateView
from django.views.generic import (DeleteView,UpdateView)
from django.shortcuts import render,get_object_or_404,redirect
from core.getData import data
class baseListView(TemplateView):
    redirect=False
    def addGet(self,request,*args,**kwargs):
        self.setContext(request)
        if self.redirect:
            return redirect(self.success_url)
        return render(request, self.template_name, self.context)
    def get(self,request,*args,**kwargs):
        return self.addGet(request)
    def setContext(self,request):
        pass
class baseForm(TemplateView):
    def addget(self,request):
        self.form = self.setform(request)
        self.setContext(request)
        return render(request, self.template_name, self.context)
    def addGet(self, request, *args, **kwargs):
        self.request = request
        return self.addget(request)
    def get(self,request,*args,**kwargs):
        return self.addGet(request)
    def setContext(self,request):
        self.items = data().set(request)
        self.context = {'form': self.form, 'items': self.items}
    def postInit(self,request,*args, **kwargs):
        pass
    def postSave(self,request, *args, **kwargs):
        pass
    def setform(self,request):
        pass
    def basePostusbmit(self,request):
        self.postInit(request)
        self.item=self.form.save()
        self.postSave(request)
        return redirect(self.success_url)
    def post(self,request, *args, **kwargs):
        self.setContext(request)
        self.form = self.setform(request)
        if self.form.is_valid():
            return self.basePostusbmit(request)
        else:
            self.setContext(request)
            return render(request, self.template_name, self.context)
        return render(request, self.template_name, self.context)
class baseCreate(baseForm):
    success_url = '/mycompany/'
    data=[]
    def setform(self,request):
        return self.form(request.POST)
class baseShowView(TemplateView):
    def get(self,request,*args,**kwargs):
        self.setContext()
        return render(request,self.template,self.context)
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.getObject, id=id_)
    def setContext(self):
        self.context={'context':self.get_object()}
class baseUpdateView(baseForm):
    success_url = '/mycompany/'
    context={}
    def addget(self,request):
        self.form = self.form(instance=self.get_object())
        self.setContext(request)
        return render(request, self.template_name, self.context)
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.getObject, id=id_)
    def setform(self,request):
        return self.form(request.POST,instance=self.get_object())
class baseDeleteView(DeleteView):
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.getObject, id=id_)
