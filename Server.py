from flask import Flask,Response
from flask import render_template,request
import requests

app = Flask(__name__)

@app.route('/xml')
def home():
    file_ = open('voice.vxml')
    return Response(file_,mimetype='text/xml')

@app.route('/cse462')
def projects():
    return render_template("Homepage.html", title = 'Projects')

@app.route('/go', methods=['POST'])
def go():
    number = request.form['number']
    param = request.form['param']
    text = request.form['text']
    if param == 'sms':
        headers = {'api_key': '09d25641-93ec-41e0-be21-d703825cbc88'}
        payload = {'from':'5070479894','to':number, 'content': text}
        req = None
        req = requests.post('https://api-gw.turkcell.com.tr/api/v1/sms',headers=headers,data=payload)
        if req:
            print("----success----")
    elif(param == 'phone'):
        headers = {'api_key': '09d25641-93ec-41e0-be21-d703825cbc88'}
        payload = {'from':'5070479894','to':number, 'audio_text': text}
        req = None
        req = requests.post('https://api-gw.turkcell.com.tr/api/v1/call',headers=headers,data=payload)
        if req:
            print("----success----")

    return 'OK'



if __name__ == "__main__":
    app.run(debug=True)
