import json
from PyQt5.QtCore import QObject, pyqtSignal
from socketio import Client
from base64 import b64encode
import cv2

# sio = Client()

class Socketio_handler(QObject):
    signal_detected = pyqtSignal(list)
    signal_log = pyqtSignal(str)
    def __init__(self, url:str):
        super().__init__()
        self.sio = Client()
        self.url = url
        self.__log('建立伺服器連線...')

        @self.sio.on('detected')
        def message(data):
            json_res = json.loads(data)
            self.signal_detected.emit(json_res)
            # detected return : 
            # {
            #     x, y, conf, name
            # }

        @self.sio.event
        def connect():
            # print("connected!")
            self.__log('連線成功')
            # self.sio.emit('img', {'data': test_img()})

        @self.sio.event
        def connect_error(data):
            # print("connection failed!")
            self.__log('連線錯誤')

        @self.sio.event
        def disconnect():
            # print("disconnected!")
            self.__log('連線中斷')
        
        def test_img():
            with open('./tes.jpg', 'rb') as img:
                return b64encode(img.read())      

    def handler_connect(self):
        self.sio.connect(self.url)

    def handler_disconnect(self):
        self.sio.disconnect()

    def __log(self, log):
        self.signal_log.emit('伺服器線程： ' + log)

    def sent_map(self, img_b64):
        self.sio.emit('img', {'data': img_b64})

if __name__ == '__main__':
    handler = Socketio_handler('http://192.168.0.113:5000')
    handler.handler_connect()
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            handler.handler_disconnect()