from flask import Flask
import psutil 

app = Flask(__name__)
@app.route('/')
def hello_world():
    cpu_usage=psutil.cpu_percent(4)
    ram_usage=psutil.virtual_memory()[2]
    return "Hello, Docker! Your CPU usage is : " + str(cpu_usage) + "% and RAM usage is : " + str(ram_usage) + "%"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
