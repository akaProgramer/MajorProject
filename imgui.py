from re import S
import sys 
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication,QFileDialog,QInputDialog, QLabel, QLineEdit, QSizeGrip, QWidget, QMainWindow, QFrame, QPushButton, QComboBox,QVBoxLayout
from PyQt5.QtGui import QColor, QFont, QIcon, QImage, QLinearGradient, QPalette, QBrush,QPixmap
import PIL
from PIL import Image, BmpImagePlugin
import subprocess, os, platform
from PyQt5.QtCore import Qt, QSize
from qrcode_generator import generator as QR_Generator
from OCR import OCR 

def open_file(filepath):
        if platform.system() == 'Darwin':       # macOS
            subprocess.call(('open', filepath))
        elif platform.system() == 'Windows':    # Windows
            os.startfile(filepath)
        else:                                   # linux variants
            subprocess.call(('xdg-open', filepath))


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'GENXCO Utility Tool'
        self.left = 100
        self.top = 50
        self.width =1690
        self.height = 850
        self.image_width = 0
        self.comp_width =0
        self.setFixedSize(self.width, self.height)
        self.setObjectName('main_window')
        self.statusBar().showMessage("Message")
        self.statusBar().setObjectName("statusbar")
        stylesheet = ""
        with open("design.css", "r") as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)
        self.initUI()

    def generate_qr(self, event):
        self.Qr_text = self.image_quality_f.text()
        generate = QR_Generator.Generator(self.Qr_text)
        generate.generate()
        generate.save()
        open_file("qrcode.png")
        self.statusBar().showMessage("Message: QR Code generated")

    def select_file_path(self):
        self.path_fileName, _ = QFileDialog.getOpenFileName(self,"Select File", "","All Files (*);;JPEG  (*.jpeg);;JPG  (*.jpg);;PNG  (*.png)")
        print(self.path_fileName)
        self.image_extractor_path.setText(self.path_fileName)

    def ocr_extractor(self,event):
        text_ext = OCR.text_extracter()
        try:
            text_ext.extrated_text(self.path_fileName)
        except Exception as f:
            self.statusBar().showMessage("Message: please select appropriate file")
        finally: 
            self.statusBar().showMessage("Message: please select appropriate file")
        



    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        
        # sys.flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint |  QtCore.Qt.CustomizeWindowHint)
        # self.setWindowFlags(sys.flags)
        # vbox =  QVBoxLayout()
        # sizegrip = QSizeGrip
        # vbox.addWidget(self, sizegrip)
        # self.setLayout(vbox)
        # labelimage =  QLabel(self)
        # pixmap = QPixmap("bgimage.jpg") 
        # labelimage.setPixmap(pixmap)

        # vbox.addWidget(labelimage)

        



        
        
        
        
        # main window-------------------------------------------------------
        self.tool_name = QFrame(self)
        self.tool_name.setObjectName("tool")
        self.tool_name.move(0,20)
        
        self.tool_name_heading = QLabel(self.tool_name)
        self.tool_name_heading.setText("GENEXCO UTILITY TOOL")
        self.tool_name_heading.move(606,19)
        self.tool_name_heading.setObjectName("tool_head")
        #image compressor
        self.image_comp_main = QFrame(self)
        self.image_comp_main.setObjectName("img_comp")
        # self.image_comp_main.setFrameStyle(QFrame.Raised)
        # self.image_comp_main.setGeometry(150,30,340,550)
        self.image_comp_main.move(90,180)
        self.image_comp_main.mousePressEvent = self.image_comp_main_clicked

        self.image_comp_main_heading = QLabel(self.image_comp_main)
        self.image_comp_main_heading.setText("Image\nCompressor")
        self.image_comp_main_heading.setFont(QFont('Arial', 28))
        self.image_comp_main_heading.setObjectName("single_img")
        self.image_comp_main_heading.move(35,50)


        self.single_img = QFrame(self)
        self.single_img.setObjectName("img")
        self.single_img.move(655,180)
        self.single_img.mousePressEvent = self.single_img_clicked
        self.single_img.setVisible(False)

        self.back_arrow_s = QLabel(self.single_img)
        self.back_arrow_s.move(20,0)
        self.back_arrow_s.setObjectName("back_arrow")
        self.back_arrow_s.setTextFormat(Qt.RichText)
        self.back_arrow_s.setText("&#8592;")
        self.back_arrow_s.mousePressEvent = self.back_arrow_clicked_IC

        self.single_img_heading = QLabel(self.single_img)
        self.single_img_heading.setText("Compress Image")
        self.single_img_heading.setFont(QFont('Arial', 16))
        self.single_img_heading.setObjectName("single_img")
        self.single_img_heading.move(85,20)


        self.single_img_para = QLabel(self.single_img)
        self.single_img_para.setText("Click here to compress single image")
        self.single_img_para.setFont(QFont('Arial', 12))
        self.single_img_para.setObjectName("s_img_p")
        self.single_img_para.move(30,110)

        
        self.multi_img = QFrame(self)
        self.multi_img.setObjectName("img")
        self.multi_img.move(655,480)
        self.multi_img.mousePressEvent = self.multi_img_clicked
        self.multi_img.setVisible(False)

        self.multi_img_heading = QLabel(self.multi_img)
        self.multi_img_heading.setText("Compress Multiple Images")
        self.multi_img_heading.setFont(QFont('Arial', 16))
        self.multi_img_heading.setObjectName("multi_img")
        self.multi_img_heading.move(25,20)

        self.multi_img_para = QLabel(self.multi_img)
        self.multi_img_para.setText("Click here to compress multiple images \n       by selecting the whole folder")
        # self.multi_img_para.setWordWrap(True)
        self.multi_img_para.setFont(QFont('Arial', 12))
        self.multi_img_para.setObjectName("m_img_p")
        self.multi_img_para.move(15,110)

        
        
        # -----------------------single image expanded----------------------------
        
        self.single_img_expanded = QFrame(self)
        self.single_img_expanded.setObjectName("img_expansion")
        self.single_img_expanded.move(655,180)
        self.single_img_expanded.setVisible(False)

        self.back_arrow_s = QLabel(self.single_img_expanded)
        self.back_arrow_s.move(20,0)
        self.back_arrow_s.setObjectName("back_arrow")
        self.back_arrow_s.setTextFormat(Qt.RichText)
        self.back_arrow_s.setText("&#8592;")
        self.back_arrow_s.mousePressEvent = self.back_arrow_clicked

        self.single_img_heading = QLabel(self.single_img_expanded)
        self.single_img_heading.setText("Compress Image")
        self.single_img_heading.setFont(QFont('Arial', 16))
        self.single_img_heading.setObjectName("single_img")
        self.single_img_heading.move(100,20)

        self.selectimage = QLabel(self.single_img_expanded)
        self.selectimage.setText("Choose Image")
        self.selectimage.setFont(QFont('Arial', 12))
        self.selectimage.setObjectName("m_img_p")
        self.selectimage.move(100,100)

        self.image_path = QLineEdit(self.single_img_expanded)
        self.image_path.setObjectName("path")
        self.image_path.move(100,135)


        self.browse_button = QPushButton(self.single_img_expanded)
        self.browse_button.setText("....")
        self.browse_button.move(280,135)
        self.browse_button.setObjectName("browse_button")
        self.browse_button.clicked.connect(self.select_file)

        self.selectImageQuality_i = QLabel(self.single_img_expanded)
        self.selectImageQuality_i.setText("Choose Quality")
        self.selectImageQuality_i.setFont(QFont('Arial', 12))
        self.selectImageQuality_i.setObjectName("m_img_p")
        self.selectImageQuality_i.move(100,240)

        self.image_quality_i = QLineEdit(self.single_img_expanded)
        self.image_quality_i.setObjectName("quality_path")
        self.image_quality_i.move(100,260)

        self.qcombo = QComboBox(self.single_img_expanded)
        self.qcombo.move(240,278)
        self.qcombo.addItem("High")
        self.qcombo.addItem("Normal")
        self.qcombo.addItem("Medium")
        self.qcombo.addItem("Low")
        self.qcombo.addItem("Very Low")
        self.qcombo.currentIndexChanged.connect(self.quality_value)

        self.compress_button = QPushButton(self.single_img_expanded)
        self.compress_button.setText("COMPRESS")
        self.compress_button.move(140,360)
        self.compress_button.clicked.connect(self.resize_pic)
        self.compress_button.setObjectName("compress_button")
        # self.compress_button.setStyleSheet({background})

        

    # -----------------------multi image expanded------------------------------------
        
        self.multi_img_expanded = QFrame(self)
        self.multi_img_expanded.setObjectName("img_expansion")
        self.multi_img_expanded.move(655,180)
        self.multi_img_expanded.setVisible(False)

        self.back_arrow_m = QLabel(self.multi_img_expanded)
        self.back_arrow_m.move(30,0)
        self.back_arrow_m.setObjectName("back_arrow")
        self.back_arrow_m.setTextFormat(Qt.RichText)
        self.back_arrow_m.setText("&#8592;")
        self.back_arrow_m.mousePressEvent = self.back_arrow_clicked

        self.multi_img_heading = QLabel(self.multi_img_expanded)
        self.multi_img_heading.setText("Compress Images")
        self.multi_img_heading.setFont(QFont('Arial', 16))
        self.multi_img_heading.setObjectName("single_img")
        self.multi_img_heading.move(100,20)

        self.selectFolder = QLabel(self.multi_img_expanded)
        self.selectFolder.setText("Select Folder")
        self.selectFolder.setFont(QFont('Arial', 12))
        self.selectFolder.setObjectName("m_img_p")
        self.selectFolder.move(100,100)

        self.browse_button_f = QPushButton(self.multi_img_expanded)
        self.browse_button_f.setText("....")
        self.browse_button_f.move(280,130)
        self.browse_button_f.setObjectName("browse_button")
        self.browse_button_f.clicked.connect(self.select_source_folder)


        self.folder_path = QLineEdit(self.multi_img_expanded)
        self.folder_path.setObjectName("path")
        self.folder_path.move(100,130)


        self.select_d_folder = QLabel(self.multi_img_expanded)
        self.select_d_folder.setText("Select Destination Folder")
        self.select_d_folder.setFont(QFont('Arial', 11))
        self.select_d_folder.setObjectName("m_img_p")
        self.select_d_folder.move(100,300)

        self.d_folder = QLineEdit(self.multi_img_expanded)
        self.d_folder.setObjectName("path")
        self.d_folder.move(100,328)

        self.browse_button_d = QPushButton(self.multi_img_expanded)
        self.browse_button_d.setText("....")
        self.browse_button_d.move(280,328)
        self.browse_button_d.setObjectName("browse_button")
        self.browse_button_d.clicked.connect(self.select_dest_folder)

        self.selectImageQuality_f = QLabel(self.multi_img_expanded)
        self.selectImageQuality_f.setText("Choose Quality")
        self.selectImageQuality_f.setFont(QFont('Arial', 12))
        self.selectImageQuality_f.setObjectName("m_img_p")
        self.selectImageQuality_f.move(100,200)

        self.image_quality_f = QLineEdit(self.multi_img_expanded)
        self.image_quality_f.setObjectName("quality_path")
        self.image_quality_f.move(100,210)

        self.qcombo_f = QComboBox(self.multi_img_expanded)
        self.qcombo_f.move(240,228)
        self.qcombo_f.addItem("High")
        self.qcombo_f.addItem("Normal")
        self.qcombo_f.addItem("Medium")
        self.qcombo_f.addItem("Low")
        self.qcombo_f.addItem("Very Low")
        self.qcombo_f.currentIndexChanged.connect(self.quality_value_f)

        self.compress_button_f = QPushButton(self.multi_img_expanded)
        self.compress_button_f.setText("COMPRESS")
        self.compress_button_f.move(148,389)
        self.compress_button_f.clicked.connect(self.resize_folder)
        self.compress_button_f.setObjectName("compress_button")
        # self.compress_button.setStyleSheet({background})
       
        
        
        # -----------------------------end of main window-----------------------------------
        # *********IMAGE CONVERTOR******************************************IMAGE CONVERTOR**************************************IMAGE CONVERTOR**********************************************
        self.image_conv_main = QFrame(self)
        self.image_conv_main.setObjectName("img_conv")
        self.image_conv_main.move(480,180)
        self.image_conv_main.mousePressEvent = self.image_conv_main_clicked

        self.image_conv_main_heading = QLabel(self.image_conv_main)
        self.image_conv_main_heading.setText("Image\nConvertor")
        self.image_conv_main_heading.setFont(QFont('Arial', 28))
        self.image_conv_main_heading.setObjectName("single_img")
        self.image_conv_main_heading.move(35,50)


        self.single_img_conv = QFrame(self)
        self.single_img_conv.setObjectName("img_conv_s")
        self.single_img_conv.move(655,180)
        self.single_img_conv.mousePressEvent = self.single_img_conv_clicked
        self.single_img_conv.setVisible(False)

        self.back_arrow_s_conv = QLabel(self.single_img_conv)
        self.back_arrow_s_conv.move(20,0)
        self.back_arrow_s_conv.setObjectName("back_arrow")
        self.back_arrow_s_conv.setTextFormat(Qt.RichText)
        self.back_arrow_s_conv.setText("&#8592;")
        self.back_arrow_s_conv.mousePressEvent = self.back_arrow_conv_clicked_IC

        self.single_img_conv_heading = QLabel(self.single_img_conv)
        self.single_img_conv_heading.setText("Convert Image")
        self.single_img_conv_heading.setFont(QFont('Arial', 16))
        self.single_img_conv_heading.setObjectName("single_img")
        self.single_img_conv_heading.move(85,20)


        self.single_img_conv_para = QLabel(self.single_img_conv)
        self.single_img_conv_para.setText("Click here to convert single image")
        self.single_img_conv_para.setFont(QFont('Arial', 12))
        self.single_img_conv_para.setObjectName("s_img_p_conv")
        self.single_img_conv_para.move(30,110)

        
        self.multi_img_conv = QFrame(self)
        self.multi_img_conv.setObjectName("img_conv_s")
        self.multi_img_conv.move(655,480)
        self.multi_img_conv.mousePressEvent = self.multi_img_conv_clicked
        self.multi_img_conv.setVisible(False)

        self.multi_img_conv_heading = QLabel(self.multi_img_conv)
        self.multi_img_conv_heading.setText("Convert Multiple Images")
        self.multi_img_conv_heading.setFont(QFont('Arial', 16))
        self.multi_img_conv_heading.setObjectName("multi_img")
        self.multi_img_conv_heading.move(25,20)

        self.multi_img_conv_para = QLabel(self.multi_img_conv)
        self.multi_img_conv_para.setText("Click here to convert multiple images \n       by selecting the whole folder")
        # self.multi_img_conv_para.setWordWrap(True)
        self.multi_img_conv_para.setFont(QFont('Arial', 12))
        self.multi_img_conv_para.setObjectName("m_img_p")
        self.multi_img_conv_para.move(15,110)


        # -----------------------single image expanded----------------------------
        
        self.single_img_conv_expanded = QFrame(self)
        self.single_img_conv_expanded.setObjectName("img_expansion")
        self.single_img_conv_expanded.move(655,180)
        self.single_img_conv_expanded.setVisible(False)

        self.back_arrow_conv_s = QLabel(self.single_img_conv_expanded)
        self.back_arrow_conv_s.move(20,0)
        self.back_arrow_conv_s.setObjectName("back_arrow")
        self.back_arrow_conv_s.setTextFormat(Qt.RichText)
        self.back_arrow_conv_s.setText("&#8592;")
        self.back_arrow_conv_s.mousePressEvent = self.back_arrow_conv_clicked

        self.single_img_conv_heading = QLabel(self.single_img_conv_expanded)
        self.single_img_conv_heading.setText("Convert Image")
        self.single_img_conv_heading.setFont(QFont('Arial', 16))
        self.single_img_conv_heading.setObjectName("single_img_conv")
        self.single_img_conv_heading.move(100,20)

        self.selectimage_conv = QLabel(self.single_img_conv_expanded)
        self.selectimage_conv.setText("Choose Image")
        self.selectimage_conv.setFont(QFont('Arial', 12))
        self.selectimage_conv.setObjectName("m_img_p_conv")
        self.selectimage_conv.move(100,100)

        self.image_conv_path = QLineEdit(self.single_img_conv_expanded)
        self.image_conv_path.setObjectName("path_conv")
        self.image_conv_path.move(100,135)


        self.browse_button = QPushButton(self.single_img_conv_expanded)
        self.browse_button.setText("....")
        self.browse_button.move(280,135)
        self.browse_button.setObjectName("browse_button_conv")
        self.browse_button.clicked.connect(self.select_file)

        self.selectImageQuality_i = QLabel(self.single_img_conv_expanded)
        self.selectImageQuality_i.setText("Choose Extension")
        self.selectImageQuality_i.setFont(QFont('Arial', 12))
        self.selectImageQuality_i.setObjectName("m_img_p_conv")
        self.selectImageQuality_i.move(100,240)

        self.image_ext_i = QLineEdit(self.single_img_conv_expanded)
        self.image_ext_i.setObjectName("quality_path_conv")
        self.image_ext_i.move(100,260)

        self.qcombo_ext = QComboBox(self.single_img_conv_expanded)
        self.qcombo_ext.move(240,278)
        self.qcombo_ext.addItem("High")
        self.qcombo_ext.addItem("Normal")
        self.qcombo_ext.addItem("Medium")
        self.qcombo_ext.addItem("Low")
        self.qcombo_ext.addItem("Very Low")
        self.qcombo_ext.currentIndexChanged.connect(self.quality_value)

        self.convert_button = QPushButton(self.single_img_conv_expanded)
        self.convert_button.setText("CONVERT")
        self.convert_button.move(140,360)
        self.convert_button.clicked.connect(self.resize_pic)
        self.convert_button.setObjectName("convert_button")
        # self.compress_button.setStyleSheet({background})

        

    # -----------------------multi image expanded------------------------------------
        
        self.multi_img_conv_expanded = QFrame(self)
        self.multi_img_conv_expanded.setObjectName("img_expansion")
        self.multi_img_conv_expanded.move(655,180)
        self.multi_img_conv_expanded.setVisible(False)

        self.back_arrow_conv_m = QLabel(self.multi_img_conv_expanded)
        self.back_arrow_conv_m.move(30,0)
        self.back_arrow_conv_m.setObjectName("back_arrow")
        self.back_arrow_conv_m.setTextFormat(Qt.RichText)
        self.back_arrow_conv_m.setText("&#8592;")
        self.back_arrow_conv_m.mousePressEvent = self.back_arrow_conv_clicked

        self.multi_img_conv_heading = QLabel(self.multi_img_conv_expanded)
        self.multi_img_conv_heading.setText("Convert Images")
        self.multi_img_conv_heading.setFont(QFont('Arial', 16))
        self.multi_img_conv_heading.setObjectName("single_img_conv")
        self.multi_img_conv_heading.move(100,20)

        self.selectFolder_conv = QLabel(self.multi_img_conv_expanded)
        self.selectFolder_conv.setText("Select Folder")
        self.selectFolder_conv.setFont(QFont('Arial', 12))
        self.selectFolder_conv.setObjectName("m_img_p_conv")
        self.selectFolder_conv.move(100,100)

        self.browse_button_conv_f = QPushButton(self.multi_img_conv_expanded)
        self.browse_button_conv_f.setText("....")
        self.browse_button_conv_f.move(280,130)
        self.browse_button_conv_f.setObjectName("browse_button_conv")
        self.browse_button_conv_f.clicked.connect(self.select_source_folder)


        self.folder_path_conv = QLineEdit(self.multi_img_conv_expanded)
        self.folder_path_conv.setObjectName("path")
        self.folder_path_conv.move(100,130)


        self.select_d_folder = QLabel(self.multi_img_conv_expanded)
        self.select_d_folder.setText("Select Destination Folder")
        self.select_d_folder.setFont(QFont('Arial', 11))
        self.select_d_folder.setObjectName("m_img_p_conv")
        self.select_d_folder.move(100,300)

        self.d_folder_conv = QLineEdit(self.multi_img_conv_expanded)
        self.d_folder_conv.setObjectName("path")
        self.d_folder_conv.move(100,328)

        self.browse_button_conv_d = QPushButton(self.multi_img_conv_expanded)
        self.browse_button_conv_d.setText("....")
        self.browse_button_conv_d.move(280,328)
        self.browse_button_conv_d.setObjectName("browse_button_conv")
        self.browse_button_conv_d.clicked.connect(self.select_dest_folder)

        self.selectImageQuality_f = QLabel(self.multi_img_conv_expanded)
        self.selectImageQuality_f.setText("Choose Extension")
        self.selectImageQuality_f.setFont(QFont('Arial', 12))
        self.selectImageQuality_f.setObjectName("m_img_p_conv")
        self.selectImageQuality_f.move(100,200)

        self.image_quality_f = QLineEdit(self.multi_img_conv_expanded)
        self.image_quality_f.setObjectName("quality_path")
        self.image_quality_f.move(100,210)

        self.qcombo_f = QComboBox(self.multi_img_conv_expanded)
        self.qcombo_f.move(240,228)
        self.qcombo_f.addItem("High")
        self.qcombo_f.addItem("Normal")
        self.qcombo_f.addItem("Medium")
        self.qcombo_f.addItem("Low")
        self.qcombo_f.addItem("Very Low")
        self.qcombo_f.currentIndexChanged.connect(self.quality_value_f)

        self.convert_button = QPushButton(self.multi_img_conv_expanded)
        self.convert_button.setText("CONVERT")
        self.convert_button.move(148,389)
        self.convert_button.setObjectName("convert_button")
        # self.compress_button.setStyleSheet({background})


        
        # *******************QR-CODE*******************************QR-CODE****************************************QR-CODE*********************************************************************** 
        self.qr_main = QFrame(self)
        self.qr_main.setObjectName("qr")
        self.qr_main.move(870,180)
        self.qr_main.mousePressEvent = self.qr_main_clicked

        self.qr_main_heading = QLabel(self.qr_main)
        self.qr_main_heading.setText("QR-Code\nGenerator")
        self.qr_main_heading.setFont(QFont('Arial', 28))
        self.qr_main_heading.setObjectName("single_img")
        self.qr_main_heading.move(35,50)

        self.qr_expanded = QFrame(self)
        self.qr_expanded.setObjectName("img_expansion")
        self.qr_expanded.move(655,180)
        self.qr_expanded.setVisible(False)
        
        self.back_arrow_qr = QLabel(self.qr_expanded)
        self.back_arrow_qr.move(30,0)
        self.back_arrow_qr.setObjectName("back_arrow")
        self.back_arrow_qr.setTextFormat(Qt.RichText)
        self.back_arrow_qr.setText("&#8592;")
        self.back_arrow_qr.mousePressEvent = self.back_arrow_qr_clicked_IC

        self.qr_heading = QLabel(self.qr_expanded)
        self.qr_heading.setText("Generate QR-Code")
        self.qr_heading.setFont(QFont('Arial', 16))
        self.qr_heading.setObjectName("single_img_conv")
        self.qr_heading.move(100,20)

        self.selectImageQuality_f = QLabel(self.qr_expanded)
        self.selectImageQuality_f.setText("Enter Your Text Here")
        self.selectImageQuality_f.setFont(QFont('Arial', 12))
        self.selectImageQuality_f.setObjectName("m_img_p_conv")
        self.selectImageQuality_f.move(100,140)
        
        self.image_quality_f = QLineEdit(self.qr_expanded)
        self.image_quality_f.setObjectName("quality_path_qr")
        self.image_quality_f.move(100,180)

        self.generate_button = QPushButton(self.qr_expanded)
        self.generate_button.setText("Generate")
        self.generate_button.move(100,289)
        self.generate_button.setObjectName("generate_button")
        self.generate_button.mousePressEvent = self.generate_qr

        # *****************TEXT EXTRACTOR*******************************TEXT EXTRACTOR**********************************TEXT EXTRACTOR**********************************************************

        self.extractor_main = QFrame(self)
        self.extractor_main.setObjectName("extractor")
        self.extractor_main.move(1260,180)
        self.extractor_main.mousePressEvent = self.ext_main_clicked

        self.extractor_main_heaading = QLabel(self.extractor_main)
        self.extractor_main_heaading.setText("Text\nExtractor")
        self.extractor_main_heaading.setFont(QFont('Arial', 28))
        self.extractor_main_heaading.setObjectName("single_img")
        self.extractor_main_heaading.move(35,50)

        self.extractor_expanded = QFrame(self)
        self.extractor_expanded.setObjectName("img_expansion")
        self.extractor_expanded.move(655,180)
        self.extractor_expanded.setVisible(False)
        
        self.back_arrow_extractor = QLabel(self.extractor_expanded)
        self.back_arrow_extractor.move(30,0)
        self.back_arrow_extractor.setObjectName("back_arrow")
        self.back_arrow_extractor.setTextFormat(Qt.RichText)
        self.back_arrow_extractor.setText("&#8592;")
        self.back_arrow_extractor.mousePressEvent = self.back_arrow_ext_clicked_IC

        self.extractor_heading = QLabel(self.extractor_expanded)
        self.extractor_heading.setText("Extract Text")
        self.extractor_heading.setFont(QFont('Arial', 16))
        self.extractor_heading.setObjectName("single_img_conv")
        self.extractor_heading.move(100,20)

        self.selectimage_extractor = QLabel(self.extractor_expanded)
        self.selectimage_extractor.setText("Select Image")
        self.selectimage_extractor.setFont(QFont('Arial', 12))
        self.selectimage_extractor.setObjectName("m_img_p_conv")
        self.selectimage_extractor.move(100,120)

        self.image_extractor_path = QLineEdit(self.extractor_expanded)
        self.image_extractor_path.setObjectName("quality_path_ext")
        self.image_extractor_path.move(100,155)


        self.browse_button_extractor = QPushButton(self.extractor_expanded)
        self.browse_button_extractor.setText("....")
        self.browse_button_extractor.move(285,173.5)
        self.browse_button_extractor.setObjectName("browse_button_ext")
        self.browse_button_extractor.clicked.connect(self.select_file_path)


        self.extractor_button = QPushButton(self.extractor_expanded)
        self.extractor_button.setText("Extract")
        self.extractor_button.move(100,289)
        self.extractor_button.setObjectName("ext_button")
        self.extractor_button.mousePressEvent = self.ocr_extractor
        
        self.show()

    # ---------------------------Functions-----------------------------------
    
    def select_file(self):
        
       
        fileName, _ = QFileDialog.getOpenFileName(self,"Select File", "","All Files (*);;JPEG  (*.jpeg);;JPG  (*.jpg);;PNG  (*.png)")
        if fileName:
            try:

                print(fileName,_)
                self.image_path.setText(fileName)
                img = Image.open(fileName)
                self.image_width = img.width
                self.comp_width = self.image_width
                self.image_quality_i.setText(str(self.image_width))
            except:
                print("pass")


    
    def quality_value(self):
        
        if self.qcombo.currentText() == "High":
            self.image_quality_i.setText(str(int(self.image_width)))
            print(self.qcombo.currentText())
            self.comp_width = self.image_width

        if self.qcombo.currentText() == "Normal":
            self.image_quality_i.setText(str(int(self.image_width/2)))
            self.comp_width = int(self.image_width/2)
            
        if self.qcombo.currentText() == "Medium":
            self.image_quality_i.setText(str(int(self.image_width/4)))
            self.comp_width = int(self.image_width/4)
        
        if self.qcombo.currentText() == "Low":
            self.image_quality_i.setText(str(int(self.image_width/6)))
            self.comp_width = int(self.image_width/6)

        if self.qcombo.currentText() == "Very Low":
            self.image_quality_i.setText(str(int(self.image_width/10)))
            self.comp_width = int(self.image_width/10)

        
                  
    
   
    def select_source_folder(self):
        folder = str(QFileDialog.getExistingDirectory(self, "Select Folder"))
        print(folder)
        self.folder_path.setText(folder)
        try:
            files = os.listdir(folder)
            first_pic = folder + "/" + files[0]
            img = Image.open(first_pic)
            self.image_width = img.width
            self.comp_width = self.image_width
            self.image_quality_f.setText(str(self.image_width))
        except:
            print("error handeled")

    def select_dest_folder(self):
        folder = str(QFileDialog.getExistingDirectory(self, "Select Folder"))
        print(folder)
        self.d_folder.setText(folder)
   
    def quality_value_f(self):
        if self.qcombo_f.currentText() == "High":
            self.image_quality_f.setText(str(int(self.image_width)))
            print(self.qcombo_f.currentText())
            self.comp_width = self.image_width

        if self.qcombo_f.currentText() == "Normal":
            self.image_quality_f.setText(str(int(self.image_width/2)))
            self.comp_width = int(self.image_width/2)
            
        if self.qcombo_f.currentText() == "Medium":
            self.image_quality_f.setText(str(int(self.image_width/4)))
            self.comp_width = int(self.image_width/4)
        
        if self.qcombo_f.currentText() == "Low":
            self.image_quality_f.setText(str(int(self.image_width/6)))
            self.comp_width = int(self.image_width/6)

        if self.qcombo_f.currentText() == "Very Low":
            self.image_quality_f.setText(str(int(self.image_width/10)))
            self.comp_width = int(self.image_width/10)


    
    def resize_pic(self):
        oldpic = self.image_path.text()
        print(oldpic)
        print(self.comp_width)
        directories = self.image_path.text().split("/")
        print(directories)
        
        
        
        newpic = ''   
        new_pic_name, okPressed = QInputDialog.getText(self, "Save image as","Image name:", QLineEdit.Normal, "")
        try:
            if okPressed and new_pic_name != '':
                print(new_pic_name)
                
                if oldpic[-4:] == ".jpeg":
                        new_pic_name += ".jpeg"
                    
                if oldpic[-3:] == ".jpg":
                        new_pic_name += ".jpg"
                    
                if oldpic[-3:] == ".png":
                        new_pic_name += ".png"

                else:
                    new_pic_name += ".jpg"

                for directory in directories[:-1]:
                    newpic = newpic + directory + "/"

                newpic+=new_pic_name
                print(newpic)
                self.compress_code(self, oldpic, newpic)
                self.statusBar().showMessage("Message: IMAGE COMPRESSED")
        except:
            self.statusBar().showMessage("Message: please select appropriate file")
        finally:
            self.statusBar().showMessage("Message: please select appropriate file")


        
        

    def resize_folder(self):
        source_directory = self.folder_path.text()
        files = os.listdir(source_directory)

        dest_directory = self.d_folder.text()

        for file in files:
            print(file)
            try:
                if file[-4:] == '.png' or file[-4:] == '.jpg' or file[-5:] == '.jpeg' or file[-4:] == '.PNG' or file[-4:] == '.JPG' or file[-5:] == '.JPEG':
                    
                    oldpic = source_directory + "/" + file
                    newpic = dest_directory + "/" + file
                    
                    img = Image.open(oldpic)
                    self.image_width = img.width
                    # self.comp_width = self.image_width
                    self.image_quality_f.setText(str(self.image_width))
                    
                    print(oldpic)
                    print(newpic)
                    
                    
                    self.compress_code(oldpic, newpic, self.image_width)

                else:
                    print("ignored" + file)
                    continue
                self.statusBar().showMessage("Message: FOLDER COMPRESSED")
            except:
                self.statusBar().showMessage("Message: please select appropriate file")

    def compress_code(self, oldpic, newpic, mywidth):
        try:
            img = Image.open(oldpic)
            mywidth = self.comp_width
            width_size = (mywidth / float(img.size[0]))
            img_size = int((float(img.size[1]) * float(width_size)))
            img = img.resize((mywidth, img_size), PIL.Image.ANTIALIAS)
            img.save(newpic)
        except Exception as e:
            self.statusBar().showMessage("Message : lomda" + str(e))
        finally:
            self.statusBar().showMessage("Message: task cannot be completed")
        


    

   
    
# ************************************COMPRESSOR****************************************************

    def back_arrow_clicked(self, event):
        self.single_img.setVisible(True)
        self.multi_img.setVisible(True)
        self.single_img_expanded.setVisible(False)
        self.multi_img_expanded.setVisible(False)

    def back_arrow_clicked_IC(self, event):
        self.single_img.setVisible(False)
        self.multi_img.setVisible(False)
        self.single_img_expanded.setVisible(False)
        self.multi_img_expanded.setVisible(False)
        
        self.image_comp_main.setVisible(True)
        self.image_conv_main.setVisible(True)
        self.extractor_main.setVisible(True)
        self.qr_main.setVisible(True)

    
    def image_comp_main_clicked(self, event):
        self.single_img.setVisible(True)
        self.multi_img.setVisible(True)
        self.image_comp_main.setVisible(False)
        self.image_conv_main.setVisible(False)
        self.qr_main.setVisible(False)
        self.extractor_main.setVisible(False)

    def single_img_clicked(self , event):
        print("single clicked")
        self.single_img.setVisible(False)
        self.multi_img.setVisible(False)
        self.single_img_expanded.setVisible(True)
        self.multi_img_expanded.setVisible(False)

    def multi_img_clicked(self , event):
        print("multi clicked")
        self.single_img.setVisible(False)
        self.multi_img.setVisible(False)
        self.multi_img_expanded.setVisible(True)
        self.single_img_expanded.setVisible(False)
# *****************************************************COMPRESSOR END***********************************************************

# ****************************************************CONVERTOR*****************************************************************

    
    def back_arrow_conv_clicked(self, event):
        self.single_img_conv.setVisible(True)
        self.multi_img_conv.setVisible(True)
        self.single_img_conv_expanded.setVisible(False)
        self.multi_img_conv_expanded.setVisible(False)

    def back_arrow_conv_clicked_IC(self, event):
        self.single_img_conv.setVisible(False)
        self.multi_img_conv.setVisible(False)
        self.single_img_conv_expanded.setVisible(False)
        self.multi_img_conv_expanded.setVisible(False)
        
        self.image_comp_main.setVisible(True)
        self.image_conv_main.setVisible(True)
        self.single_img_conv.setVisible(False)
        self.multi_img_conv.setVisible(False)

        self.extractor_main.setVisible(True)
        self.qr_main.setVisible(True)
    
    
    def image_conv_main_clicked(self, event):
        self.single_img_conv.setVisible(True)
        self.multi_img_conv.setVisible(True)
        self.image_comp_main.setVisible(False)
        self.image_conv_main.setVisible(False)
        self.qr_main.setVisible(False)
        self.extractor_main.setVisible(False)

    def single_img_conv_clicked(self, event):
        self.single_img_conv.setVisible(False)
        self.multi_img_conv.setVisible(False)
        self.multi_img_conv_expanded.setVisible(False)
        self.single_img_conv_expanded.setVisible(True)

    def multi_img_conv_clicked(self, event):
        self.single_img_conv.setVisible(False)
        self.multi_img_conv.setVisible(False)
        self.multi_img_conv_expanded.setVisible(True)
        self.single_img_conv_expanded.setVisible(False)    



# ****************************************************QR CODE*****************************************************************


    def back_arrow_qr_clicked_IC(self, event): 
        
        self.qr_expanded.setVisible(False)
        self.image_comp_main.setVisible(True)
        self.image_conv_main.setVisible(True)
        self.extractor_main.setVisible(True)
        self.qr_main.setVisible(True)






    def qr_main_clicked(self, event):
        self.qr_expanded.setVisible(True)
        self.single_img_conv.setVisible(False)
        self.multi_img_conv.setVisible(False)
        self.image_comp_main.setVisible(False)
        self.image_conv_main.setVisible(False)
        self.qr_main.setVisible(False)
        self.extractor_main.setVisible(False)


# ****************************************************QR CODE END*****************************************************************

# ****************************************************TEXT EXTRACTOR**************************************************************

    def back_arrow_ext_clicked_IC(self, event):  
        
        self.extractor_expanded.setVisible(False)
        self.image_comp_main.setVisible(True)
        self.image_conv_main.setVisible(True)
        self.extractor_main.setVisible(True)
        self.qr_main.setVisible(True)


    def ext_main_clicked(self, event):
        self.extractor_expanded.setVisible(True)
        self.qr_expanded.setVisible(False)
        self.single_img_conv.setVisible(False)
        self.multi_img_conv.setVisible(False)
        self.image_comp_main.setVisible(False)
        self.image_conv_main.setVisible(False)
        self.qr_main.setVisible(False)
        self.extractor_main.setVisible(False)


# ****************************************************TEXT EXTRACTOR END**************************************************************



        

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
