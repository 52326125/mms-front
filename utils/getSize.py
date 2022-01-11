import io
from PIL import ImageGrab
import cv2
import numpy as np
import base64

def get_img_str(img_from_dm) ->str:
    arr = np.fromstring(base64.b64decode(img_from_dm), np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_ANYCOLOR)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img = cv2.imencode('.jpg', img)[1].tostring()
    return base64.b64encode(img)


class GetSize():
    def __init__(self, event_hook) -> None:
        self.start_x = 0
        self.start_y = 0
        self.start_x_temp = 0
        self.start_y_temp = 0
        self.end_x = 800
        self.end_y = 600
        self.click = 0
        self.WINDOW_NAME = 'mini map picker'
        self.event_hook = event_hook

    def show_img(self, img_b64):
        cv2.namedWindow(self.WINDOW_NAME)
        cv2.setMouseCallback(self.WINDOW_NAME, self.__mouse_click)
        arr = np.fromstring(base64.b64decode(img_b64), np.uint8)
        img = cv2.imdecode(arr, cv2.IMREAD_ANYCOLOR)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        self.img = img
        cv2.imshow(self.WINDOW_NAME, img)

    def __mouse_click(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            if self.click == 0:
                self.start_x_temp = x
                self.start_y_temp = y
                self.click = 1
            else:
                self.click = 0
                cv2.destroyWindow(self.WINDOW_NAME)
                img = self.img[self.start_y_temp:y, self.start_x_temp:x]
                cv2.imwrite('mini_map.jpg', img)
                self.event_hook(self.start_x_temp, self.start_y_temp, x, y)
                

# def show_img(img_b64):
#     cv2.namedWindow(WINDOW_NAME)
#     cv2.setMouseCallback(WINDOW_NAME, mouse_click)
#     arr = np.fromstring(base64.b64decode(img_b64), np.uint8)
#     img = cv2.imdecode(arr, cv2.IMREAD_ANYCOLOR)
#     img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
#     cv2.imshow(WINDOW_NAME, img)
    


# if __name__ == '__main__':
#     cv2.namedWindow('test')
#     cv2.setMouseCallback('test', mouse_click)
#     while True:
#         img_grb = ImageGrab.grab((start_x, start_y, end_x, end_y))
#         img_grb = np.array(img_grb, np.uint8)
#         img_bgr = cv2.cvtColor(img_grb, cv2.COLOR_RGB2BGR)

#         cv2.imshow('test', img_bgr)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break