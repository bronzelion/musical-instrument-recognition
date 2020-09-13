from django.shortcuts import *
from extract_features import *
from csvtolibsvm import *
from svm_prediction import predict
from django.http import *
from models import *

# Create your views here.

from mir.extractor.models import UploadForm, Upload
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


# Create your views here.
def home(request):
    if request.method == "POST":
        audio_clip = UploadForm(request.POST, request.FILES)
        if audio_clip.is_valid():
            audio_clip.save()
            uploaded_file_name = request.FILES["pic"]
            print ("Recieved file {0}".format(uploaded_file_name))
            feats, features,  = extract_feature(uploaded_file_name)
            input_vec = csvtolibsvm("1", features)
            inst = predict(input_vec)
            print (inst)
            return HttpResponse(
                "The Instrument Recognition system detects a presence of <b> {0} </b> ".format(inst)
            )

    else:
        audio_clip = UploadForm()

    images = Upload.objects.all()
    return render(request, "home.html", {"form": audio_clip, "images": images})
