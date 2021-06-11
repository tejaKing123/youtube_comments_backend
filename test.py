from flask import Flask,render_template,request
import pandas as pd
import extract

app=Flask(__name__)

@app.route('/',methods=['GET'])
def hello_world():
    
    return render_template('index.html')

@app.route('/sentiment',methods=['POST','GET'])
def sentiment():
    temp=request.form
    test=extract.main_method(temp['fname'])
    return render_template('index.html',data=test[0],data1=test[1],data2=test[2],data3=test[3],data4=test[4])

if __name__=='__main__':
    app.run(port=3000,debug=True)

#  <h1>Youtube Comment analyser</h1>
#         <form action="/sentiment" method="POST">
#             <label for="fname">Video title:</label>
#             <input type="text" id="fname" name="fname"><br><br>
            
#             <input type="submit" value="Submit">
#           </form>
        
#         <h2>{{data}}</h2>
#         <h2>{{data1}}</h2>
#         <h2>{{data2}}</h2>
#         <h2>{{data3}}</h2>
#         <h2>{{data4}}</h2>