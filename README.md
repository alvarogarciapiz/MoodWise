# TFG
# MoodWise
<!---![MoodWise main](https://i.ibb.co/tLQBGLF/git.jpg)--->

**MoodWise** es el nombre que le he dado al programa prototipo que formará parte de mi trabajo fin de grado para el grado en ingeniería informática. El presente trabajo tiene como objetivo utilizar librerías de aprendizaje automático para el reconocimiento de gestos y emociones de videos tomados por la cámara y poder visualziar y exportar los datos recogidos. Todo ello agrupado en una interfaz sencilla.

## Uso e instalación
Desde la línea de comandos clona el repositorio:
`git clone https://github.com/alvarogarciapiz/MoodWise.git`
El programa ha sido desarollado con un MacBook Air 2017 en la versión macOS Monterrey 12.6.4 en un entorno virtual de python versión 3.9 y con el IDE Visual Studio Code versión 1.77.1

Para su uso podemos ejecutar el fichero **run.py** desde línea de comandos.

### Instalación de requisitos
Para instalar las librerías utilizadas en el proyecto se facilita un requirements.txt en la raiz del proyecto. Para su uso:
`pip install -r requirements.txt`

## Usuarios
El subsistema de **usuarios** es el encargado de la gestión de todos los usuarios que utilicen la herramienta, desde su identificación hasta su registro. Los usuarios son guardados en un fichero _json_ con las claves almacenadas en **MD5**. Cuando un usuario es registrado se crea una estructura de directorios asociado al usuarios donde se almacenarán sus datos, incluyendo un log.

## Data
En el directorio **data** se encuentran almacenados los directorios con la información de los usuarios así como la clase _Log.py_ encargada de llevar un registro de log de las acciones que realizan los usuarios en el sistema.

## Assets
En el directorio **assets** se encuentran almacenados los iconos y recursos que se emplearán en la interfaz de usuario del sistema que ha sido desarrollada con _tkinter_ y _customtkinter_.

## Admin
El fichero de ejecución **run.py** que se encuentra en la raiz del proyecto permite la entrada de parámetros de administración: Log y Backup. El primer parámetro será la función a ejecutar y el segundo otro argumeto que será necesario en el caso de Log.
`python run.py ARGUMENTO1 ARGUMENTO2`

### Comando Log
Con este comando podemos especificar un usuario del que obtendremos su registro de Log. Por ejemplo si queremos obtener el log del usuario 'a' tendremos que ejecutar desde línea de comandos lo siguiente:
`python run.py log a`
El log será exportado a un _.txt_ en nuestro Escritorio del sistema.

### Comando Backup
Con el comando backup se realiza una copia de seguridad de todos los archivos de todos los usuarios que será exportada a un zip.
`python run.py backup`
El backup será exportado a un _.zip_ en nuestro Escritorio del sistema.

## Gestos y Emociones
En el lado izquierdo de la interfaz se recopilan las acciones asociadas al reconocimiento, visualización y exportación de Gestos miestras que en el lado derecho tendremos los de emociones. A continuación se explican las diferentes opciones. Los gestos que se reconocen son: perfecto, un poco, corazón y suerte. En el caso de las emociones se reconoce: enfado, desprecio, disgusto, miedo, contento, triste y sorpresa.

### Visualizar estadísticas
![Estadisticas](https://i.ibb.co/s99F3Ph/Captura-de-Pantalla-2023-04-13-a-las-15-22-09.png)
Para la visualización de estadísticas se muestran dos gráficos creados con MatPlotLib con los diferentes gestos o emociones registrados. Se incluye una barra de herramientas con cada gráfico para su exportación y modificación.

### Exportar estadísticas
![Exportar estadisticas](https://i.ibb.co/194qRQS/Captura-de-Pantalla-2023-04-13-a-las-15-22-37.png)

Después de realizar varios reconocimientos ya sea de gestos o emociones resulta interesante poder exportarnos esos datos. Se ofrecen dos selectores de fehcas para poder ajustar el rango  de fechas que queramos para la exportación y dos opciones: Exportación de PDF o en Excel.

### Reconocimiento | Introudcción a yolo
La parte de reconocimiento funciona gracias a un modelo previamente entrenado y cuyo entrenamiento se explica en el siguiente apartado. Se emplea la librería de OpenCV para registrar videos y posteriormente la librería de Yolo para el reconocimiento.

# Entrenamiento del Modelo con YOLOV7
A la hora de detectar gestos y emociones se hace uso de la librería de [YoloV7](https://github.com/WongKinYiu/yolov7). Esta librería nos permite entrenar un modelo para posteriormente realizar detecciones. Debido a las limitaciones de mi máquina he usado Google Colab para entrenar los dos modelos (Gestos y Emociones) aunque la detección se realiza en local. El objetivo es obtener un fichero de pesos _.pt_ que utiliza el script _test.py_ de Yolo para realizar la detección.

Para entrenar el modelo primero se debe tener un dataset. En el caso de los gestos crée mi propio dataset a base de imágenes mientras que en el caso de las emociones partí de un dataset ya creado para ahorrar tiempo en el proceso de etiquetado. Recomiendo utilizar la herramienta Roboflow para el etiquetado de las imágenes del dataset por su versatilidad, facilidad de uso y opciones que nos da. Puedes ver mi dataset de gestos desde aquí: [dataset gestos](https://universe.roboflow.com/uemc-y7rsy/gestos-tfg/dataset/2).

Una vez tomado el dataset se genera un fichero _.yaml_ donde se indican el número de clases y tipo que se van a reconocer con el modelo. A continuación se muestra el fichero yaml asociado a las emociones:
```
train: train/images
val: valid/images

nc: 7
names: ['enfado', 'desprecio', 'disgusto', 'miedo', 'contento' , 'triste', 'sorpresa']
```
Se debe indicar el número de clases que vamos a reconocer, una lista con las diferentes clases (importante el orden en el que aparecen) y las rutas donde se almacenan las imágenes separadas para el entrenamiento y las de validación (también se tiene una carpeta para test que se usará más adelante).

Entrenar el modelo en google Colab es realmente sencillo con los siguientes pasos:
```
# Descargamos Repositorio de YoloV7 e instalamos los requerimientos
!git clone https://github.com/WongKinYiu/yolov7
# %cd yolov7
!pip install -r requirements.txt

#Descargamos el dataset etiquetado para yoloV7, en este caso son imágenes de matriculaa
!curl -L "https://universe.roboflow.com/ds/Ev3PeBzZ1o?key=ooXyCeAEJw" > gestos.zip
!unzip gestos.zip
!rm gestos.zip

# Traemos un fichero yaml modificado para que pueda funcionar en Google Colab (se modifica el directorio a donde se acceden los conjuntos de train y val)
!curl -L "https://raw.githubusercontent.com/alvarogarciapiz/gestos/main/data_4gestos.yaml" > data_4gestos.yaml

# Nos descargamos unos pesos iniciales de YoloV7 para proceder a hacer transfer learning posteriormente
# %cd /content/yolov7
!wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7_training.pt

#Solución error pytorch
# %cd /content/yolov7/utils
!rm loss.py
!wget https://raw.githubusercontent.com/alvarogarciapiz/gestos/main/loss.py

# %cd /content/yolov7
!python train.py --batch 14 --epochs 20 --data /content/yolov7/data_4gestos.yaml  --weights 'yolov7_training.pt' --device 0

# Run evaluation
!python detect.py --weights runs/train/exp/weights/best.pt --conf 0.1 --source /content/yolov7/test/images #Cambiar la carpeta exp si hay alguna posterior

#Veamos los resultados
import glob
from IPython.display import Image, display

i = 0
limit = 10000 # max images to print
for imageName in glob.glob('/content/yolov7/runs/detect/exp/*.jpg'): #Aquí asumimos que los ficheros son JPG y que solo hemos hecho una detección, si hemos hecho más: cambiar exp por exp2,exp3 o la última
    if i < limit:
      display(Image(filename=imageName))
      print("\n")
    i = i + 1
```
Una vez entrenado el modelo (que dependiendo del dataset, los epochs y el batch size tardará más o menos) descargamos el fichero best.pt con los pesos asociados al modelo. Estos pesos son los que se utilizarán para el reconocimiento de gestos por un lado, y de emociones por otro.

# Mejoras
Usar variables globales para rutas
