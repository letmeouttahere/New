from flask import Flask
import socket
app = Flask(__name__)
@app.route('/')
def get_host_name():
    host_name = 'srv-b'
    return f'Host Name: {host_name}'
if __name__ == '__main__':
    app.run(host='0.0.0.0')