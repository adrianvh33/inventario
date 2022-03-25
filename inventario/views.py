
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Inventarios
from django.views.generic import ListView,CreateView, UpdateView
from .forms import InventariosForms


class InventariosListView(LoginRequiredMixin,ListView):
    model = Inventarios
    context_object_name = 'inventarios'
    template_name = 'inventario/inventarios_list.html'
    login_url = '/'

class InventariosCreateView(LoginRequiredMixin,CreateView):
    model= Inventarios
    template_name = 'inventario/inventarios_form.html'
    success_url = '/inventarios'
    form_class = InventariosForms
    login_url = '/'