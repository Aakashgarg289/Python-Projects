from flask import Flask, render_template, request
import pickle


app = Flask(__name__)

f = open("model.pkl", "rb")
clf = pickle.load(f)
# print(clf)
f.close()


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method=="POST":
        myDict = request.form
        fever = int(myDict['fever'])
        age = int(myDict['age'])
        pain = int(myDict['pain'])
        nose = int(myDict['nose'])
        breath = int(myDict['breath'])
        inpu = [fever, age, pain, nose, breath]
        infec = clf.predict_proba([inpu])[0][1]
        return render_template('show.html', inf = round(infec*100))
    return render_template('index.html')
    # return "Hello World" + " " + str(infec)

if __name__=='__main__':
    app.run(debug=True)