from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from dictionary.models import Dictionary


class DictionaryList(ListView):
    model = Dictionary
    paginate_by = 10

    def get_queryset(self):
        search_animal_name = self.request.GET.get('search_animal_name', '')

        if search_animal_name == '':
            dictionary_list = self.model.objects.all()
        else:
            dictionary_list = self.model.objects.filter(animal_name__contains=search_animal_name)
        return dictionary_list

class DictionaryFishList(ListView):
    model = Dictionary
    paginate_by = 10
    def get_queryset(self):
        dictionary_list = self.model.objects.filter(kind='어류')
        return dictionary_list

class DictionaryAmphibiaList(ListView):
    model = Dictionary
    paginate_by = 10
    def get_queryset(self):
        dictionary_list = self.model.objects.filter(kind='양서류')
        return dictionary_list

class DictionaryReptileList(ListView):
    model = Dictionary
    paginate_by = 10
    def get_queryset(self):
        dictionary_list = self.model.objects.filter(kind='파충류')
        return dictionary_list

class DictionaryMammalList(ListView):
    model = Dictionary
    paginate_by = 10
    def get_queryset(self):
        dictionary_list = self.model.objects.filter(kind='포유류')
        return dictionary_list

class DictionaryBirdList(ListView):
    model = Dictionary
    paginate_by = 10
    def get_queryset(self):
        dictionary_list = self.model.objects.filter(kind='조류')
        return dictionary_list

class DictionaryCreateView(CreateView):
    model = Dictionary
    fields = '__all__'
    template_name_suffix = '_create'
    success_url = reverse_lazy('dictionary:list')

class DictionaryDetailView(DetailView):
    model = Dictionary

class DictionaryUpdateView(UpdateView):
    model = Dictionary
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = reverse_lazy('dictionary:list')

class DictionaryDeleteView(DeleteView):
    model = Dictionary
    success_url = reverse_lazy('dictionary:list')