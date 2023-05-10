import cv2, os, time


def foto(username):
    ruta = "TFG/data/users/" + username + "/fotosGEST"
    if not os.path.exists(ruta):
        os.makedirs(ruta)
    cap = cv2.VideoCapture(0) # Captura la imagen de la cámara
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # Establece el ancho del fotograma en 640 píxeles
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640) # Establece la altura del fotograma en 640 píxeles

    ret, frame = cap.read() # Lee un fotograma de la cámara
    cap.release() # Libera la cámara
    ruta = ruta + "/foto.jpg"
    cv2.imwrite(ruta, frame) # Guarda la imagen en la ruta especificada

    return ruta


def video(username):
    # Define el directorio donde se guardará el video
    dir_path = "TFG/data/users/" + username + "/videoGEST"
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # Inicializa la cámara
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 24)  # Fija la tasa de fotogramas a 10fps
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Fija la anchura del fotograma a 640 píxeles
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Fija la altura del fotograma a 480 píxeles

    # Define el codec y crea el objeto VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Codec para el video
    out = cv2.VideoWriter(os.path.join(dir_path, "video.mp4"), fourcc, 10.0, (640, 480))

    # Captura y escribe el video durante 3 segundos
    start_time = cv2.getTickCount()  # Marca de tiempo de inicio
    while (cv2.getTickCount() - start_time) / cv2.getTickFrequency() < 4:  # Captura durante 3 segundos
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)

    # Libera los objetos VideoCapture y VideoWriter
    cap.release()
    out.release()

    print("Video guardado en:", os.path.join(dir_path, "video.mp4"))
    ruta = os.path.join(dir_path, "video.mp4")
    time.sleep(2)
    mostrarVideo(ruta)
    return ruta


def mostrarVideo(ruta):
    cap = cv2.VideoCapture(ruta)

    # Reproducir el video
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.putText(frame, 'Espere...', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (1, 255, 1), 2)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Salir al presionar la tecla "q"
            break

    # Liberar los recursos
    cap.release()
    cv2.destroyAllWindows()


def mostrarVideoProcesado(ruta):
    cap = cv2.VideoCapture(ruta)

    # Reproducir el video
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.putText(frame, 'Se ha detectado lo siguiente: ', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (1, 255, 1), 2)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Salir al presionar la tecla "q"
            break

    # Liberar los recursos
    cap.release()
    cv2.destroyAllWindows()    
