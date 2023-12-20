import os
from django.urls import reverse_lazy
from django.views.generic import ListView , DetailView, CreateView, UpdateView, DeleteView
from .models import Modelo, Marca, MarcaModelo, Auto

# CRUD modelo
class ModeloListView(ListView):
    model = Modelo
    template_name ='agencia/modelos/modelo_list.html'
    context_object_name = 'modelos'

class ModeloDetailsViews(DetailView):
    model = Modelo
    template_name = 'agencia/modelos/modelo_detail.html'
    context_object_name = 'modelo'

class ModeloCreateView(CreateView):
    model = Modelo
    template_name = 'agencia/modelos/modelo_from.html'
    context_object_name = 'modelo'
    fields = '__all__'
    success_url = reverse_lazy('modelo_list')

class ModeloUpdateView(UpdateView):
    model = Modelo
    template_name = 'agencia/modelos/modelo_from.html'
    context_object_name = 'modelo'
    fields = '__all__'
    success_url = reverse_lazy('modelo_list')

class ModeloDeleteView(DeleteView):
    model = Modelo
    template_name = 'agencia/modelos/modelo_confirm_delete.html'
    context_object_name = 'modelo'
    success_url = reverse_lazy('modelo_list')

# CRUD marca
class MarcaListView(ListView):
    model = Marca
    template_name ='agencia/marcas/marca_list.html'
    context_object_name = 'marcas'

class MarcaDetailsViews(DetailView):
    model = Marca
    template_name = 'agencia/marcas/marca_detail.html'
    context_object_name = 'marca'

class MarcaCreateView(CreateView):
    model = Marca
    template_name = 'agencia/marcas/marca_from.html'
    context_object_name = 'marca'
    fields = '__all__'
    success_url = reverse_lazy('marca_list')

class MarcaUpdateView(UpdateView):
    model = Marca
    template_name = 'agencia/marcas/marca_from.html'
    context_object_name = 'marca'
    fields = '__all__'
    success_url = reverse_lazy('marca_list')

class MarcaDeleteView(DeleteView):
    model = Marca
    template_name = 'agencia/marcas/marca_confirm_delete.html'
    context_object_name = 'marca'
    success_url = reverse_lazy('marca_list')

# CRUD MarcaModelo
class MarcaModeloListView(ListView):
    model = MarcaModelo
    template_name ='agencia/marcasmodelos/marca_modelo_list.html'
    context_object_name = 'marcamodelos'

class MarcaModeloDetailsViews(DetailView):
    model = MarcaModelo
    template_name = 'agencia/marcasmodelos/marca_modelo_detail.html'
    context_object_name = 'marcamodelo'

class MarcaModeloCreateView(CreateView):
    model = MarcaModelo
    template_name = 'agencia/marcasmodelos/marca_modelo_from.html'
    context_object_name = 'marcamodelo'
    fields = '__all__'
    success_url = reverse_lazy('marca_modelo_list')

class MarcaModeloUpdateView(UpdateView):
    model = MarcaModelo
    template_name = 'agencia/marcasmodelos/marca_modelo_from.html'
    context_object_name = 'marcamodelo'
    fields = '__all__'
    success_url = reverse_lazy('marca_modelo_list')

class MarcaModeloDeleteView(DeleteView):
    model = MarcaModelo
    template_name = 'agencia/marcasmodelos/marca_modelo_confirm_delete.html'
    context_object_name = 'marcamodelo'
    success_url = reverse_lazy('marca_modelo_list')

# CRUD Auto
class AutoListView(ListView):
    model = Auto
    template_name ='agencia/autos/auto_list.html'
    context_object_name = 'autos'

class AutoDetailsViews(DetailView):
    model = Auto
    template_name = 'agencia/autos/auto_detail.html'
    context_object_name = 'auto'

class AutoCreateView(CreateView):
    model = Auto
    template_name = 'agencia/autos/auto_from.html'
    context_object_name = 'auto'
    fields = '__all__'
    success_url = reverse_lazy('auto_list')

class AutoUpdateView(UpdateView):
    model = Auto
    template_name = 'agencia/autos/auto_from.html'
    fields = '__all__'
    success_url = reverse_lazy('auto_list')

class AutoDeleteView(DeleteView):
    model = Auto
    template_name = 'agencia/autos/auto_confirm_delete.html'
    success_url = reverse_lazy('auto_list')
    #eliminar imagen guardada en media (hay que importar OS primero)
    def form_valid(self, form):
        auto = self.get_object()
        if auto.imagen:
            image_path = auto.imagen.path
        if os.path.exists(image_path):
            os.remove(image_path)
        return super().form_valid(form)
    