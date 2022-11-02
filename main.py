import cv2

# CORES DAS CLASSES
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

# CARREGA AS CLASSES
class_names = []

with open("coco.names", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]

# CAPTURA DO VÍDEO
captureService = cv2.VideoCapture(0)

# CARREGANDO OS PESOS DA REDE NEURAL
net = cv2.dnn.readNet("yolov4-tiny.weights", "yolov4-tiny.cfg")

# SETANDO OS PARÂMETROS DA REDE NEURAL
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1 / 255)

# LENDO OS FRAMES DO VÍDEO
while cv2.waitKey(5) != 27:

    # CAPTURA DO FRAME
    frameExists, frame = captureService.read()

    if not frameExists:
        break

    classes, scores, boxes = model.detect(frame, 0.1, 0.2)

    # PERCORRER TODAS AS DETECÇÕES
    for (classid, score, box) in zip(classes, scores, boxes):
        # GERANDO UMA COR PARA A CLASSE
        color = COLORS[int(classid) % len(COLORS)]

        # PEGANDO O NOME DA CLASSE PELO ID E SEU SCORE DE ACURÁCIA
        label = f"{class_names[classid]} : {score}"

        # DESENHANDO A BOX DA DETECÇÃO
        cv2.rectangle(frame, box, color, 2)

        # ESCREVENDO O NOME DA CLASSE EM CIMA DA BOX DO OBJETO
        cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    cv2.imshow("Webcam", frame)

captureService.release()
cv2.destroyAllWindows()
