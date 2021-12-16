from socketio import Client
from base64 import b64encode
import cv2

# sio = Client()

class Socketio_handler():
    def __init__(self, url):
        self.sio = Client()
        self.url = url

        @self.sio.on('detected')
        def message(data):
            print(data)

        @self.sio.event
        def connect():
            print("connected!")
            self.sio.emit('img', {'data': test_img()})

        @self.sio.event
        def connect_error(data):
            print("connection failed!")

        @self.sio.event
        def disconnect():
            print("disconnected!")
        
        def test_img():
            with open('./tes.jpg', 'rb') as img:
                return b64encode(img.read())      

    def handler_connect(self):
        self.sio.connect(self.url)

    def handler_disconnect(self):
        self.sio.disconnect()

if __name__ == '__main__':
    handler = Socketio_handler('http://192.168.0.113:5000')
    handler.handler_connect()
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            handler.handler_disconnect()