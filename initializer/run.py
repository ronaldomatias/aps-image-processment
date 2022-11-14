import cv2
import apiconsumer.apiconsumer as apiconsumer

def init():
    # CARREGA AS CLASSES
    class_name = ['gun']

    # CAPTURA DO VÍDEO
    captureService = cv2.VideoCapture(0)

    # CARREGANDO OS PESOS DA REDE NEURAL
    net = cv2.dnn.readNet("config/yolo.weights", "config/yolo.cfg")

    # SETANDO OS PARÂMETROS DA REDE NEURAL
    model = cv2.dnn_DetectionModel(net)
    model.setInputParams(size=(416, 416), scale=1 / 255)

    send_message = True
    # LENDO OS FRAMES DO VÍDEO
    while cv2.waitKey(1) != 27:

        # CAPTURA DO FRAME
        frameExists, frame = captureService.read()

        if not frameExists:
            break

        classes, precisoes, boxes = model.detect(frame, 0.1, 0.2)

        # PERCORRER TODAS AS DETECÇÕES
        for (classid, precisao, box) in zip(classes, precisoes, boxes):
            # GERANDO UMA COR PARA A CLASSE
            color = (0, 255, 255)

            # PEGANDO O NOME DA CLASSE PELO ID E SEU SCORE DE ACURÁCIA
            label = f"{class_name[0]} : {precisao}"

            # DESENHANDO A BOX DA DETECÇÃO
            cv2.rectangle(frame, box, color, 2)

            # ESCREVENDO O NOME DA CLASSE EM CIMA DA BOX DO OBJETO
            cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            if send_message:
                apiconsumer.comunicateApi()
                send_message = False

        cv2.imshow("Webcam", frame)

    captureService.release()
    cv2.destroyAllWindows()