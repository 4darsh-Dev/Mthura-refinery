from django.shortcuts import render

# Importing the necessary modules
import pandas as pd

# Create your views here.

def excel_data_request(request):
    # Reading data from excel , specify path
    excel_data = pd.read_excel("F:/backup-kali/codeFiles/projects/refinery/check1.xlsx")

    
    # Excel data in dictionaries(key-value)pairs
    data_list = excel_data.to_dict(orient= "records")

    # Adding Serial no.
    excel_data['SNo'] = range(1, len(excel_data) + 1)

    return render(request, "index.html", {"data_list" : data_list})



