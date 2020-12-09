from PySide2.QtWidgets import QMainWindow, QFileDialog,QMessageBox,QTableWidgetItem, QGraphicsScene
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from PySide2.QtGui import QPen, QColor, QTransform
from particulas import Particulas
from particula import Particula
from grafo import Grafo
from pprint import pprint, pformat

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()  

        self.particulas = Particulas()
        self.grafo = Grafo()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.finalcap.clicked.connect(self.click_agregarfinal)
        self.ui.Iniciocap.clicked.connect(self.click_agregarinicio)      
        self.ui.Mostrar.clicked.connect(self.click_mostrar)
        self.ui.OrigenX.valueChanged.connect(self.setValue)
        self.ui.OrigenY.valueChanged.connect(self.setValue)
        self.ui.DestinoX.valueChanged.connect(self.setValue)
        self.ui.DestinoY.valueChanged.connect(self.setValue)
        self.ui.Verde.valueChanged.connect(self.setValue)
        self.ui.Rojo.valueChanged.connect(self.setValue)
        self.ui.Azul.valueChanged.connect(self.setValue)

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)
        self.ui.actionPor_ID.triggered.connect(self.action_ordenarid)
        self.ui.actionVelocidad.triggered.connect(self.action_ordenarvelocidad)
        self.ui.actionDistancia.triggered.connect(self.action_ordenardistancia)
        self.ui.actionGrafo.triggered.connect(self.action_transformaragrafo)
        self.ui.actionBusquedaGrafo.triggered.connect(self.busqueda_grafos)

        self.ui.Mostrartabla_push.clicked.connect(self.Mostrar_tabla)
        self.ui.Buscar_push.clicked.connect(self.buscar_id)
        
        self.ui.Dibujarpush.clicked.connect(self.dibujar)
        self.ui.Limpiarpush.clicked.connect(self.limpiar)

        self.scene = QGraphicsScene()  
        self.ui.graphicsView.setScene(self.scene)

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    @Slot()
    def Mostrar_tabla(self):
        self.ui.Tabla.setColumnCount(10)
        headers = ["Id", "origen_x", "origen_y", "destino_x", "destino_y", "velocidad","rojo", "verde","azul", "distancia"]
        self.ui.Tabla.setHorizontalHeaderLabels(headers)

        self.ui.Tabla.setRowCount(len(self.particulas))

        row = 0
        for particula in self.particulas:
            Id_widget = QTableWidgetItem(str(particula.Id))
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula. origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))           
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            rojo_widget = QTableWidgetItem(str(particula.rojo))
            verde_widget = QTableWidgetItem(str(particula.verde))
            azul_widget = QTableWidgetItem(str(particula.azul))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.Tabla.setItem(row, 0,  Id_widget)
            self.ui.Tabla.setItem(row, 1,  origen_x_widget)
            self.ui.Tabla.setItem(row, 2,  origen_y_widget)
            self.ui.Tabla.setItem(row, 3,  destino_x_widget)
            self.ui.Tabla.setItem(row, 4,  destino_y_widget)
            self.ui.Tabla.setItem(row, 5,  velocidad_widget)
            self.ui.Tabla.setItem(row, 6,  rojo_widget)
            self.ui.Tabla.setItem(row, 7,  verde_widget)
            self.ui.Tabla.setItem(row, 8,  azul_widget)
            self.ui.Tabla.setItem(row, 9,  distancia_widget)

            row += 1
            
    @Slot()
    def buscar_id(self):

        headers = ["Id", "origen_x", "origen_y", "destino_x", "destino_y", "velocidad","rojo", "verde","azul", "distancia"]
        Id = self.ui.LineadeBusqueda.text()
        
        encontrado = False

        for particula in self.particulas:
            if Id == str(particula.Id):
                self.ui.Tabla.clear()
                self.ui.Tabla.setRowCount(1)
                self.ui.Tabla.setColumnCount(10)
                self.ui.Tabla.setHorizontalHeaderLabels(headers)

                Id_widget = QTableWidgetItem(str(particula.Id))
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula. origen_y))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))           
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                rojo_widget = QTableWidgetItem(str(particula.rojo))
                verde_widget = QTableWidgetItem(str(particula.verde))
                azul_widget = QTableWidgetItem(str(particula.azul))
                distancia_widget = QTableWidgetItem(str(particula.distancia))

                self.ui.Tabla.setItem(0, 0,  Id_widget)
                self.ui.Tabla.setItem(0, 1,  origen_x_widget)
                self.ui.Tabla.setItem(0, 2,  origen_y_widget)
                self.ui.Tabla.setItem(0, 3,  destino_x_widget)
                self.ui.Tabla.setItem(0, 4,  destino_y_widget)
                self.ui.Tabla.setItem(0, 5,  velocidad_widget)
                self.ui.Tabla.setItem(0, 6,  rojo_widget)
                self.ui.Tabla.setItem(0, 7,  verde_widget)
                self.ui.Tabla.setItem(0, 8,  azul_widget)
                self.ui.Tabla.setItem(0, 9,  distancia_widget)

                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atencion",
                f'La particula con ID = "{Id}" no fue encontrado'
            )


    @Slot()
    def action_abrir_archivo(self):
       # print('Abrir Archivo')
        ubicacion = QFileDialog.getOpenFileName(
           self,
           'Abrir Archivo',
           '.',
           'JSON (*.json)'
        )[0]
        if self.particulas.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se abrió el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo " + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self):
        #print('Guardar Archivo')
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.particulas.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
               self,
               "Error",
               "No se pudo crear el archivo " + ubicacion
            )
     
    @Slot()
    def click_agregarfinal(self):
        Id = self.ui.ID.value()
        Ox = self.ui.OrigenX.value()   
        Oy = self.ui.OrigenY.value() 
        Dx = self.ui.DestinoX.value()
        Dy = self.ui.DestinoY.value()
        Vel = self.ui.Velocidad.value()
        Red = self.ui.Rojo.value()       
        Green = self.ui.Verde.value()   
        Blue = self.ui.Azul.value()
        particula = Particula(Id,Ox,Oy,Dx,Dy,Vel,Red,Green,Blue)
        self.particulas.agregar_final(particula)
        
        #print(particula)
        #self.ui.salida.insertPlainText(str(IDD)+str(Ox)+str(Oy)+str(Dx)+str(Dy)+str(Vel)+str(Red)+str(Blue)+str(Green))

    @Slot()
    def click_agregarinicio(self):
        Id = self.ui.ID.value()
        Ox = self.ui.OrigenX.value()   
        Oy = self.ui.OrigenY.value() 
        Dx = self.ui.DestinoX.value()
        Dy = self.ui.DestinoY.value()
        Vel = self.ui.Velocidad.value()
        Red = self.ui.Rojo.value()        
        Green = self.ui.Verde.value()
        Blue = self.ui.Azul.value()
        particula = Particula(Id,Ox,Oy,Dx,Dy,Vel,Red,Blue,Green)
        self.particulas.agregar_inicio(particula)

        #print(IDD,Ox,Oy,Dx,Dy,Vel,Red,Blue,Green)
        #self.ui.salida.insertPlainText(str(IDD)+str(Ox)+str(Oy)+str(Dx)+str(Dy)+str(Vel)+str(Red)+str(Blue)+str(Green))

    @Slot()
    def click_mostrar(self):
       # self.particulas.mostrar()
       self.ui.salida.clear()
       self.ui.salida.insertPlainText(str(self.particulas))
       
    
    @Slot()
    def setValue(self,valor):
       self.ui.NumAct.clear()
       self.ui.NumAct.insertPlainText(str(valor))

    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(3)
        
        for particula in self.particulas:

         r= particula.rojo
         g= particula.verde
         b= particula.azul
         color = QColor(r, g, b)
         pen.setColor(color)
         
         pox= particula.origen_x
         poy= particula.origen_y
         pdx= particula.destino_x
         pdy= particula.destino_y

         self.scene.addEllipse(pox, poy, 3, 3, pen)
         self.scene.addEllipse(pdx, pdy, 3, 3, pen)
         self.scene.addLine(pox+3, poy+1, pdx+2, pdy+1, pen)

    @Slot()
    def limpiar(self):
        self.scene.clear()  

    @Slot()
    def action_ordenarid(self):
        self.particulas.__sortid__()

    @Slot()
    def action_ordenarvelocidad(self):
        self.particulas.__sortvel__()

    @Slot()
    def action_ordenardistancia(self):
        self.particulas.__sortdis__()
            
    @Slot()
    def action_transformaragrafo(self):   
        for particula in self.particulas:
            self.grafo.__Add__(particula.origen_x,particula.origen_y,particula.destino_x,
            particula.destino_y)
         
        self.grafo.Mostrargrafo()
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(pformat(self.grafo.Grafo, width=40, indent=1))
    
    @Slot()
    def busqueda_grafos(self):
        
        self.grafo.quitar_peso()
        self.ui.salida.clear()

        origen = (self.ui.OrigenX.value() , self.ui.OrigenY.value())
        recorrido = self.grafo.algoritmo_busqueda_profundidad(origen)
            
        print('Profundidad')

        self.ui.salida.insertPlainText('Profundidad' + '\n')
        for i in recorrido:
            self.ui.salida.insertPlainText(str(i) + '\n')
            print(i)

        recorrido2 = self.grafo.algoritmo_busqueda_Amplitud(origen)

        print('\n' + 'Amplitud')
         
        self.ui.salida.insertPlainText('\n' + 'Amplitud' + '\n' )
        for i in recorrido2:
            self.ui.salida.insertPlainText(str(i) + '\n')
            print(i)