import streamlit as st
'''from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report'''

def app():
    st.header('CENSUS INTERVIEW DATA COLLECTION PROGRESS REPORT')

    ''' # Load iris dataset
    iris = datasets.load_iris()
    X = iris.data
    Y = iris.target

    # Model building
    st.header('Model performance')
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier()
    clf.fit(X_train, Y_train)
    score = clf.score(X_test, Y_test)
    st.write('Accuracy:')
    st.write(score)'''

    # Alternative syntax, declare a form and use the returned object
    form = st.form(key='my_form')
    form.text_input(label='Enter some text', key='name')
    submit_button = form.form_submit_button(label='Submit')

    if submit_button:
        st.write({name})