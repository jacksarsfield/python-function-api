from flask import Flask, request
#import function

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

#@app.route('/api/function/<name>/exec', methods = ['GET','POST'])
#def execute(name):
#    input = request.data
#    output = getattr(function, name)(input)
#    return output
        
if __name__ == '__main__':
   app.run()
