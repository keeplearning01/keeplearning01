from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello_world():
    data=request.form
    print(data)
    return render_template("index.html")
        # para=request.get_json()
        # account=para["account"]
        # return account
@app.route("/get")
def hello_world2():
        return render_template('index2.html')
if __name__ =="__main__":
    app.run(debug=True)