from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
import pandas as pd
# Create your views here.

class ImportHomePage(TemplateView):
    template_name = 'upload_data_home.html'

def upload(request):
    if request.method == 'POST':
        # uploaded file will be in request>FILES as a dictionary
        # the key is the name we gave it in the HTML
        uploaded_file = request.FILES['document']
        print(uploaded_file.name, uploaded_file.size)
        if not uploaded_file.name.endswith('.csv'):
            print("Not a csv file ")
            messages.error(request, "Unsupported filetype")

        df = pd.read_csv(uploaded_file)
        print(df.head(5))
    else:
        print("Nothing?")
    return render(request, 'upload.html')