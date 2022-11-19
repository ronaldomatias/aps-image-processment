import cv2

def draw_rectangle(frame, box, label):

    color = (0, 0, 255)
    # DESENHAR A CAIXA DE DETECÇÃO
    cv2.rectangle(frame, box, color, 2)
    # DESENHAR O NOME DA CLASSE
    cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)


def draw_fps(frame, end_time, start_time):
    color = (0, 255, 255)
    fps = f"FPS: {round((1.0 / (end_time - start_time)), 2)}"
    cv2.putText(frame, fps, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)