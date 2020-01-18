from django.views.generic import (UpdateView)
from django.shortcuts import get_object_or_404
class BaseUpdateView(UpdateView):
    template_name = 'edit/editbase.html'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.model, id=id_)