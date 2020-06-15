#!/usr/bin/python
# -*- coding: utf-8 -*-
def warn(*args, **kwargs):
    pass

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.core.files.storage import FileSystemStorage

#his=[]
#from .models import *



def upload_OD(request):
    default="Paste clipboard(Screenshot) image or choose from file"
    import requests
    import glob
    import os
    extractedInformation=''
    import pytesseract
    import shutil
    import os
    import random
    try:
        from PIL import Image
    except ImportError:
        import Image
    #pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs=FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        

        list_of_files = glob.glob('media/*.png') # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        print (str(latest_file))
        #abc="media"+str('\\')
        #print(abc)
        #latest_file=latest_file.replace(abc,"")
        print (str(latest_file))
        image_path_in_colab=(latest_file)
        extractedInformation = pytesseract.image_to_string(Image.open(image_path_in_colab))
        extractedInformation
        #his.append(extractedInformation)
        #default="/static/"+"1"+uploaded_file.name

       
            
    return render(request,'upload_OD.html',{'result':extractedInformation,'f5':default})


def error_404_view(request, exception):
    return render(request,'404.html')

def index(request):
    try:
        return render(request, 'index.html')
    except:
        return render(request, '404.html')