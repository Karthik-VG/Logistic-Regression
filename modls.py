from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.metrics import confusion_matrix
import numpy as np
import pickle

import pandas as pd
import os
sc = StandardScaler()


class modls:

    def __init__(self,basepath):
        self.basepath=basepath

    def read_clean_model_build(self):
        data=pd.read_csv(self.basepath+"combineddata.csv")
        df = data.dropna(axis=0)
        x_data=df.drop(columns=["class"],axis=1)
        y_data=df["class"]
        names=x_data.columns
        scaler=StandardScaler()
        df_scaled=pd.DataFrame(scaler.fit_transform(x_data))
        df_scaled.columns=[names]

        #splitting test and train data
        x_train,x_test,y_train,y_test=train_test_split(df_scaled,y_data,test_size=0.30,random_state=123,stratify=y_data)

        #Scaling the data
        x_train_scaled=sc.fit_transform(x_train)
        x_test_scaled = sc.fit_transform(x_test)

        #Building the classification model
        # multinomial solver and newton-cg
        lr_new = LogisticRegression(solver="newton-cg", multi_class="multinomial")
        lr_new.fit(x_train_scaled, y_train)
        lr_new.score(x_test_scaled, y_test)

        #Saving the model
        filename = 'model_prod.sav'
        pickle.dump(lr_new, open(filename, 'wb'))

    def predict(self,val):
        filename = 'model_prod.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        val_scaled=sc.fit_transform(val)
        result = loaded_model.predict(val_scaled)
        return result




print(os.getcwd())







