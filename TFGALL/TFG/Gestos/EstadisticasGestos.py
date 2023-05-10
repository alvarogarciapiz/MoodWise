from reportlab.pdfgen import canvas
import os
import xlsxwriter


class EstadisticasGestos:
    def __init__(self, usuario):
        self.usuario = usuario

    def generarEstadisticas(self):
        data = generarDatos(self.usuario.username)
        return data

    def exportarEstadisticas(self, dateFrom, dateTo):
        data = generarDatos(self.usuario.username)
        data = filtrarDatos(data, dateFrom, dateTo)
        ruta_escritorio = os.path.join(os.path.expanduser("~"), "Desktop")
        pdf = canvas.Canvas(ruta_escritorio + "/Gestos.pdf")
        # pdf = canvas.Canvas("../data/users/" + self.usuario.username + "/Gestos.pdf")
        y = 750
        pdf.drawString(100, y,
                       "Estadísticas de Gestos del usuario " + self.usuario.username + " del " + dateFrom + " al " + dateTo)
        y -= 30
        for clave, valor in data.items():
            pdf.drawString(100, y, clave + ": " + str(valor))
            y -= 20
        pdf.save()

    def exportarEstadisticasExcel(self, dateFrom, dateTo):
        data = generarDatos(self.usuario.username)
        data = filtrarDatos(data, dateFrom, dateTo)
        ruta_escritorio = os.path.join(os.path.expanduser("~"), "Desktop")
        rutaExcel = ruta_escritorio + "/gestos.xlsx"
        workbook = xlsxwriter.Workbook(rutaExcel)
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'Fecha Hora')
        worksheet.write('B1', 'Gesto')
        row = 1
        for key, value in data.items():
            worksheet.write(row, 0, key)
            worksheet.write(row, 1, value)
            row +=1
        workbook.close()

# Devuelve un diccionario leído del fichero txt donde se almacenan los datos del usuario
def generarDatos(username):
    ruta = "TFG/data/users/" + username + "/gestos.txt"
    data = {}
    with open(ruta, "r") as file:
        for linea in file:
            clave, valor = linea.strip().split("|")
            data[clave] = valor
    file.close()
    return data


def filtrarDatos(data, dateFrom, dateTo):
    newData = {}
    dateFrom += " 00:00:00"
    dateTo += " 23:59:59"
    for clave, valor in data.items():
        if clave>= dateFrom and clave <= dateTo:
            newData[clave] = valor
    return newData
