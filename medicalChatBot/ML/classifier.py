from sklearn import tree
import pandas as pd

def makeModel():
    print("makeModal======================")
    #training data :
    df=pd.read_csv('medicalChatBot/ML/Training.csv')

    feature_names=[]
    for i in df.columns[0:len(df.columns)-1] :
        feature_names.append(i)

    prognosis=df['prognosis'].drop_duplicates().tolist()

    df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
    'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
    'Migraine':11,'Cervical spondylosis':12,
    'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
    'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
    'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
    'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
    '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
    'Impetigo':40}},inplace=True)

    X_train=df[feature_names]
    y_train=df['prognosis']
    print("++++++++++++++y train++++++++++++++++++")
    print(y_train)
    clf=tree.DecisionTreeClassifier()
    clf=clf.fit(X_train,y_train)
    pd.to_pickle(clf,"medicalChatBot/ML/model.pickle")
    return feature_names,prognosis