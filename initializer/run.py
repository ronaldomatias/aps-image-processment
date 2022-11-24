import cv2
import apiconsumer.apiconsumer as api_consumer
import util.drawerutil as drawer
import util.dateutil as dateUtil
import time
import uuid


def init():
    send_message = True
    timer = 0

    capture_service = cv2.VideoCapture("videos/soldadoss.mp4")

    net = cv2.dnn.readNetFromDarknet("config/yolo.cfg", "config/yolo.weights")
    model = cv2.dnn_DetectionModel(net)
    model.setInputParams(size=(320, 320), scale=1/255)  # size precisa ser múltiplo de 32.s

    while cv2.waitKey(1) != 27:

        frame_exists, frame = capture_service.read()

        start_time = time.time()
        classes, acuracias, boxes = model.detect(frame, 0.3, 0.1)
        end_time = time.time()
        timer += end_time - start_time

        for (classid, acuracia, box) in zip(classes, acuracias, boxes):
            drawer.draw_rectangle(frame, box, f"gun: {acuracia}")

            if (acuracia > 0.75) & send_message:
                date = dateUtil.getDateNow()
                imagePath = f"/home/ronaldo/PycharmProjects/log-images/{str(uuid.uuid1())}.jpg"
                cv2.imwrite(imagePath, frame)
                api_consumer.comunicateApi(imagePath, date)
                print("Mensagem enviada.")
                send_message = False

        # A CADA 5 MINUTOS É LIBERADO O ENVIO DE UMA NOVA MENSAGEM
        if timer > 300:
            timer = 0
            send_message = True

        drawer.draw_fps(frame, end_time, start_time)
        cv2.imshow("Webcam", frame)


    capture_service.release()
    cv2.destroyAllWindows()
