from flask import Flask,request,render_template

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

if __name__=="__main__":
    app.run()  
