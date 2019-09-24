
from django.shortcuts import render
from .models import RecordForm, Record

def record_list(request):
    return render(request, 'record_list.html')



def upload_record(request):
    form = RecordForm()
    return render(request, 'myfirstapp/upload_record.html', {'form': form})


