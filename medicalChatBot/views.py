from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import numpy as np


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
indexFeatures=-1
feature_names_len=len(feature_names)
# Create your views here.
def index(request):

    return render(request,"home.html",{'feature_names': feature_names})

def makePredict(symptoms_exp):

    symptoms_dict = {}

    for index, symptom in enumerate(feature_names):
        symptoms_dict[symptom] = index

    input_vector = np.zeros(len(symptoms_dict))
    for item in symptoms_exp:
      input_vector[[symptoms_dict[item]]] = 1


    return model.predict([input_vector])
    
def predict(request):
    global indexFeatures
    if request.POST.get('action') == 'post':
        # Receive data from client
        input = str(request.POST.get('input')).lower()
        if input=='yes':
            symptoms_present.append(feature_names[indexFeatures])
            print(symptoms_present)
        # Make prediction
       # result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

        #classification = result[0]

        #PredResults.objects.create(sepal_length=sepal_length, sepal_width=sepal_width, petal_length=petal_length,petal_width=petal_width, classification=classification)
        indexFeatures+=1
        if feature_names_len<=indexFeatures:
            return JsonResponse({'result':makePredict(symptoms_present),'input':input},safe=False)
        else:
            return JsonResponse({'result':'Are you experiencing any '+str(feature_names[indexFeatures]),'input':input},safe=False)
