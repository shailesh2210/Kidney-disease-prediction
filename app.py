from flask import Flask , request , render_template
import pickle 
import numpy as np

model = pickle.load(open("rf_model.pkl ", "rb"))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict' , methods = ["GET" , "POST"])
def predict():
    if request.method == "POST":
        age = float(request.form["age"])
        bp = float(request.form["bp"])
        al = float(request.form["al"])
        su = float(request.form["su"])
        rbc = float(request.form["rbc"])
        pc = float(request.form["pc"])
        pcc = float(request.form["pcc"])
        ba = float(request.form["ba"])
        bgr = float(request.form["bgr"])
        bu = float(request.form["bu"])
        sc = float(request.form["sc"])
        pot = float(request.form["pot"])
        wc = float(request.form["wc"])
        htn = float(request.form["htn"])
        dm = float(request.form["dm"])
        cad = float(request.form["cad"])
        pe = float(request.form["pe"])
        ane = float(request.form["ane"])

        pred = model.predict([[age ,bp ,  al , su ,rbc , pc , pcc , ba , bgr 
                              , bu , sc , pot , wc , htn , dm , cad , pe , ane]])

        # data = np.array.reshape([[pred]])
        
        output = pred[0]
        if output == 0:
            return render_template("predict.html" , predicted_text = "You dont habe any kidney problem")
        
        else:
            return render_template("predict.html" , predicted_text = "Yes you have kidney problem ")

    return render_template("predict.html")

if __name__ == '__main__':
    app.run(debug=True)