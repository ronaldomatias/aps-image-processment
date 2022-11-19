import cv2
import apiconsumer.apiconsumer as api_consumer
import util.drawerutil as drawer
import time
from datetime import datetime
import uuid


def init():
    send_message = True
    timer = 0

    capture_service = cv2.VideoCapture("videos/soldados.mp4")

    net = cv2.dnn.readNet("config/yolov3.weights", "config/yolo.cfg")
    model = cv2.dnn_DetectionModel(net)
    model.setInputParams(size=(320, 320), scale=1 / 255)  # size precisa ser múltiplo de 32.

    while cv2.waitKey(1) != 27:

        frame_exists, frame = capture_service.read()

        start_time = time.time()
        classes, acuracias, boxes = model.detect(frame, 0.3, 0.1)
        end_time = time.time()
        timer += end_time - start_time

        for (classid, acuracia, box) in zip(classes, acuracias, boxes):
            print(acuracia)
            box_label = f"gun: {acuracia}"
            drawer.draw_rectangle(frame, box, box_label)

            if (acuracia > 0.75) & send_message:
                date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                imagePath = f"/home/ronaldo/PycharmProjects/log-images/{str(uuid.uuid1())}.jpg"
                cv2.imwrite(imagePath, frame)
                #api_consumer.comunicateApi(imagePath, date)
                send_message = False

        # A CADA 5 MINUTOS É LIBERADO O ENVIO DE UMA NOVA MENSAGEM
        if timer > 300:
            timer = 0
            send_message = True

        drawer.draw_fps(frame, end_time, start_time)
        cv2.imshow("Webcam", frame)


    capture_service.release()
    cv2.destroyAllWindows()
