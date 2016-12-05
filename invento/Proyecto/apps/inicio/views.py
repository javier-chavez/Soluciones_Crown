from django.shortcuts import render_to_response
from django.http import HttpResponse

from io import BytesIO
import os

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import  Paragraph, Table, TableStyle, Image
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors

#importacion para clases
from django.views.generic import TemplateView
from django.views.generic import CreateView
# Create your views here.


#def index (request):
# https://www.youtube.com/watch?v=UVXu-N_Zojw return render_to_response('inicio/index.html')

def index2 (request):
  return render_to_response('inicio/index2.html')

#class index2 (TemplateView):
	#template_name = 'inicio/index2.html'

def index3(request):
	return HttpResponse("Indexs")


def index (request):
    #Crear el Http response
    response = HttpResponse(content_type='application/pdf')
    response ['Content-Disposition'] = 'attachment; filename=Report.pdf'
    #Crear el objeto PDF
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize =A4)

    #Header cabezera de Documento
    c.setLineWidth(.3)
    c.setFont('Helvetica',22)
    c.drawString(30,750,'Ubicaciones - Crown')

    c.setFont('Helvetica-Bold',12)
    c.drawString(30,735,'Reporte')

    c.setFont('Helvetica-Bold',12)
    c.drawString(400,750,'11/10/2016')

    c.line(300,747,560,747)

    #encabezado de la tabla
    styles = getSampleStyleSheet()
    styleBH = styles["Normal"]
    styleBH.alignment = TA_CENTER
    styleBH.fontSize = 10

    numero = Paragraph('''No.''', styleBH)
    alumno = Paragraph('''Alumno''', styleBH)
    b1 = Paragraph('''BIM1''', styleBH)
    b2 = Paragraph('''BIM2''', styleBH)
    b3 = Paragraph('''BIM3''', styleBH)
    total = Paragraph('''TOTAL''', styleBH)

    data = [[numero,alumno,b1,b2,b3,total]]

    #Datos de la Tabla






    #grabar el PDF
    c.save()
    #tomar el valor de BytesIO y escribirlo
    pdf = buffer.getvalue()
    buffer.close ()
    response.write(pdf)

    return response
