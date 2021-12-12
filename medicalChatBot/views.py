from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import os


 # Unpickle model
model = pd.read_pickle("medicalChatBot/ML/model.pickle")
feature_names= pd.read_csv("medicalChatBot/ML/features.csv",index_col=0)
feature_names=feature_names.index.tolist()
# feature_name = [
#     feature_names[i] if i != model.TREE_UNDEFINED else "undefined!"
#     for i in model.feature
# ]
#chk_dis=",".join(feature_names).split(",")
symptoms_present = []

# Create your views here.
def index(request):

    return render(request,"home.html",{'feature_names': feature_names})


def predict(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        input = request.POST.get('input')
 
        # Make prediction
       # result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

        #classification = result[0]

        #PredResults.objects.create(sepal_length=sepal_length, sepal_width=sepal_width, petal_length=petal_length,petal_width=petal_width, classification=classification)
        print(feature_names[0])
        return JsonResponse({'result': feature_names[0],'input':input},safe=False)
