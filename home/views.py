from django.shortcuts import render

# Importing the necessary modules
import pandas as pd

# Create your views here.

def excel_data_request(request):

    # For First excel file check1
    # Reading data from excel , specify path
    excel_data_first = pd.read_excel("F:/backup-kali/codeFiles/projects/refinery/check1_new.xlsx")

    data_list_first = [
        {"Field": excel_data_first.iloc[0, 0], "Value": excel_data_first.iloc[0, 1]},
        {"Field": excel_data_first.iloc[1, 0], "Value": excel_data_first.iloc[1, 1]},
        {"Field": excel_data_first.iloc[2, 0], "Value": excel_data_first.iloc[2, 1]},
    ]


    # For second excel file check2
    # Reading data from excel , specify path
    excel_data_second = pd.read_excel("F:/backup-kali/codeFiles/projects/refinery/check2.xlsx")

    # Excel data in dictionaries(key-value)pairs
    data_list_second = excel_data_second.to_dict(orient= "records")

    # Adding Serial no.
    excel_data_second['SNo'] = range(1, len(excel_data_second) + 1)


    # For third excel file check3
    # Reading data from excel , specify path
    excel_data_third = pd.read_excel("F:/backup-kali/codeFiles/projects/refinery/check3.xlsx")

    # Excel data in dictionaries(key-value)pairs
    data_list_third = excel_data_third.to_dict(orient= "records")

    # Adding Serial no.
    excel_data_third['SNo'] = range(1, len(excel_data_third) + 1)


    return render(request, "index.html", {"data_list_first" : data_list_first, "data_list_second" : data_list_second, "data_list_third" : data_list_third })


def fire_safety(request):
    # For First excel file check1
    # Reading data from excel , specify path
    fire_safety_excel = pd.read_excel("F:/backup-kali/codeFiles/projects/refinery/fire-safety-data.xlsx")

    fire_safety_data = [
        {"Field": fire_safety_excel.iloc[0, 0], "Value": fire_safety_excel.iloc[0, 1]},
        {"Field": fire_safety_excel.iloc[1, 0], "Value": fire_safety_excel.iloc[1, 1]},
        {"Field": fire_safety_excel.iloc[2, 0], "Value": fire_safety_excel.iloc[2, 1]},
    ]


    # fire_safety_data = fire_safety_excel.to_dict(orient= "records")

    return render(request, "fire-safety.html", {"data_list_first": fire_safety_data})



