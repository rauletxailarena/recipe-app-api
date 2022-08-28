from django.shortcuts import render

# Create your views here.
from django_filters.views import FilterView

from reader.filters import ReaderFilter
from reader.models import Reader


class TeacherFilteredListView(FilterView):
    model = Reader
    context_object_name = 'reader_list'


def reader_list(request):
    f = ReaderFilter(request.GET, Reader.objects.all())
    return render(request, 'reader/reader_filterV2.html', {'filter': f})
