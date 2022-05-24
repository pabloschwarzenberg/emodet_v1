import numpy as np
import cv2
import pickle

#Cascada_CaraFrontal = cv2.CascadeClassifier('HaarCascade/haarcascade_frontalface_alt2.xml')
Cascada_CaraFrontal = cv2.CascadeClassifier('HaarCascade/haarcascade_frontalface_default.xml')

reconocer = cv2.face.LBPHFaceRecognizer_create()
reconocer.read("entrenamiento.yml")

etiquetas = {"emocion": 1}
with open("labels.pickle", "rb") as f:
    global_etiquetas = pickle.load(f)
    etiquetas = {v:k for k,v in global_etiquetas.items()}

cap = cv2.VideoCapture(0)

# Uso de camara
while True:
    # frame de camara
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    caras = Cascada_CaraFrontal.detectMultiScale(gray, scaleFactor=1.7, minNeighbors=3)
    for (x, y, w, h) in caras:
        #print(x, y, w, h)
        recorte_cara_gray = gray[y:y + h, x:x + w]  # area de interes para recortar, en esta caso es la cara
        marcar_cara = frame[y:y + h, x:x + w]  # cuadrado en la cara del jugador

        # reconoce?
        id_, conf = reconocer.predict(recorte_cara_gray)
        if conf >= 45:# and conf <= 85:
            print(id_)
            print(etiquetas[id_])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = etiquetas[id_]
            color = (255, 255, 255)
            stroke = 2
            cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

        image = "prueba.png"
        cv2.imwrite(image, recorte_cara_gray)

        color = (0,255,0) # genera color verde para el cuadrado de cara
        stroke = 2
        fin_coordX = x + w
        fin_coordY = y + h
        cv2.rectangle(frame, (x, y), (fin_coordX, fin_coordY), color, stroke)



    # pantalla frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()