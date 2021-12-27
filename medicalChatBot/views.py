from tkinter import Message
from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import numpy as np

from medicalChatBot.models import Resultat
from medicalChatBot.ML import classifier



#make model
feature_names, prognosis = classifier.makeModel()
#Unpickle model
model = pd.read_pickle("medicalChatBot/ML/model.pickle")
df=pd.read_csv('medicalChatBot/ML/proposition.csv')
df=df.iloc[:,0:14]
df=df.fillna('Non_symptoms')

def liste_proposal(proposal_symptom):
    ligne=[]
    symptoms_new=[]
    symptoms=[]
    for i in range(0,len(df)):
        ligne=[]
        for k in df.iloc[i,1:]:
            if k != 'Non_symptoms':
                ligne.append(k)
        if proposal_symptom in ligne:
            symptoms.extend(ligne)
    for i in symptoms : 
        if i not in symptoms_new: 
             symptoms_new.append(i) 
    print("prop symtom",proposal_symptom)
    symptoms_new.remove(proposal_symptom)
    return symptoms_new

listeproposal=[]
symptoms_present = []
indexFeatures=-1
listeproposal_len=0

# Create your views here.
def index(request):
    return render(request,"index.html")

def home(request):
    global symptoms_present,indexFeatures
    symptoms_present = []
    indexFeatures=-1
    return render(request,"home.html",{'feature_names': feature_names})

def makePredict():
    feature_names_binary=[0] * len(feature_names)
    for k in range(0,len(feature_names)):
        for  z in symptoms_present:
            if z == feature_names[k]:
                feature_names_binary[k]=1
                break
    return prognosis[model.predict([feature_names_binary])[0]]

    
def predict(request):
    global indexFeatures
    global listeproposal
    global listeproposal_len
    if request.POST.get('action') == 'post':
        # Receive data from client
        input = str(request.POST.get('input')).lower()
        if input=='yes':
            symptoms_present.append(listeproposal[indexFeatures])
            print(symptoms_present)
        elif len(symptoms_present)==0:
            input=input.replace(" ","_")
            symptoms_present.append(input)
            listeproposal=liste_proposal(input)
            listeproposal_len=len(listeproposal)
            input=input.replace("_"," ")
        indexFeatures+=1
        print("len list prop",listeproposal_len,"index",indexFeatures)
        if listeproposal_len<=indexFeatures: 
            predected_disease=str(makePredict())
            print(predected_disease)
            print(predected_disease.isdigit())
            if predected_disease.isdigit()==False:
                Message="After the diagnostic we conlused that You may have "+predected_disease
            else:
                Message="No disease !!"

            return JsonResponse({'predict':Message},safe=False)
        else:
            return JsonResponse({'result':'Are you experiencing any '+str(listeproposal[indexFeatures]).replace("_", " "),'input':input},safe=False)

def result(request):
    r = Resultat()
    r.plainte = "test"
    r.histoire = "test"
    r.examen = "test"
    r.assesment = "test"
    r.causes = "test"
    return render(request,"resultat.html",{'r': r})