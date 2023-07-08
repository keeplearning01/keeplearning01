from flask import Flask, render_template, request,Response
import spider
import asyncio
app = Flask(__name__)

# spider.startBrowser()

async def run_web_crawler(user):
    like_post=spider.get_like_post(user)
    return like_post

@app.route('/form')
def formPage():
    # like=str(spider.get_like(0))
    return render_template('form.html')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        input_data = request.form['input_data']
        # like=str(spider.get_like(user))
        # print("post : user => ", user)
        return render_template('loading.html',input_data=input_data)
        # return redirect(url_for('success', name=like, action="post"))
    # else:
    #     user = request.args.get('user')
    #     print("get : user => ", user)
    #     return redirect(url_for('success', name=user, action="get"))

# @app.route('/success/<action>/<name>')
# def success(name, action):
#     return 'the total like from {} is {}'.format(action, name)

@app.route('/loading',methods=['POST','GET'])
def loading_model():
    user=request.form['user']
    return render_template("loading.html",user=user)

@app.route('/get_result')
async def get_result():
    user = request.args.get('input_data') # Retrieve input data from query parameter
    result = await run_web_crawler(user)
    f=(int(result['like'])+int(result['n_c']))/(int(result['followers']*(result['post_num']-result['not_post'])))
    return 'the engagemnt rate is {}'.format(f)



if __name__ =="__main__":
    app.run(debug=True)