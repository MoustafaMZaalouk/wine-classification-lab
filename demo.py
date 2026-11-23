"""Small, reproducible educational experiment. See README for limitations."""
import json
from pathlib import Path
import numpy as np

def save(result, output):
    Path(output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix

def run(output="results.json"):
    X,y=load_wine(return_X_y=True)
    Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,stratify=y,random_state=42)
    models={"majority":DummyClassifier(strategy="most_frequent"),
            "logistic":make_pipeline(StandardScaler(),LogisticRegression(max_iter=2000,random_state=42)),
            "forest":RandomForestClassifier(n_estimators=150,max_depth=5,random_state=42,n_jobs=1)}
    results={}
    for name,m in models.items():
        cv=cross_val_score(m,Xtr,ytr,cv=StratifiedKFold(5,shuffle=True,random_state=42),scoring="f1_macro")
        pred=m.fit(Xtr,ytr).predict(Xte)
        results[name]={"accuracy":float(accuracy_score(yte,pred)),"macro_f1":float(f1_score(yte,pred,average="macro")),"train_cv_macro_f1":float(cv.mean()),"confusion_matrix":confusion_matrix(yte,pred).tolist()}
    return save({"seed":42,"train_rows":len(ytr),"test_rows":len(yte),"models":results},output)

if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
