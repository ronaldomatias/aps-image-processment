import cv2

def draw_rectangle(frame, box, label):

    color = (0, 0, 255)
    # DESENHAR A BOX DA DETECÇÃO
    cv2.rectangle(frame, box, color, 2)

    # ESCREVER O NOME DA CLASSE EM CIMA DA BOX DO OBJETO
    cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)