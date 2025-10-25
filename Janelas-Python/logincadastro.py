import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QInputDialog, QMessageBox, QVBoxLayout, QHBoxLayout, QCheckBox

# CRIANDO E NOMEANDO A JANELA -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class logincadastro(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Caixa")

        self.setGeometry(560,240,800,600)
        self.setFixedSize(800,600)
        self.setStyleSheet("""
                            background-color: #ffffff;
                           """)

# CRIANDO O CABEÇALHO ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        self.emailvindo_label = QLabel("Welcome to email")
        self.emailvindo_label.setStyleSheet("""
                                                font-family: 'Times New Roman';
                                                font-size: 30px; 
                                            """)
        self.emailvindo_label.setAlignment(Qt.AlignCenter)

        self.loginpfv_label = QLabel("Please login to your account")
        self.loginpfv_label.setStyleSheet("""
                                            font-family: 'Times New Roman';
                                            font-size: 15px;
                                          """)
        self.loginpfv_label.setAlignment(Qt.AlignCenter)

# EMAIL ADDRESS, PASSWORD -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        self.emaillogin_label = QLabel("Email Address")
        self.emaillogin_label.setStyleSheet("""
                                                font-family: 'Arial';
                                                font-size: 12px;
                                            """)
        self.emaillogin_label.setAlignment(Qt.AlignCenter)

        self.emaillogin_edit = QLineEdit()
        self.emaillogin_edit.setStyleSheet("""
                                            QLineEdit {
                                                font-family: 'Arial;
                                                font-size: 12px;
                                                font-weight: bold;
                                                border-radius: 15px;
                                                background-color: #f6f6f6;
                                            }
                                           """)
        self.emaillogin_edit.setFixedSize(300,30)
        self.emaillogin_edit.setAlignment(Qt.AlignCenter)

# -------------------------

        self.senhalogin_label = QLabel("Password")
        self.senhalogin_label.setStyleSheet("""
                                                font-family: 'Arial';
                                                font-size: 12px;
                                            """)
        self.senhalogin_label.setAlignment(Qt.AlignCenter)

        self.senhalogin_edit = QLineEdit()
        self.senhalogin_edit.setStyleSheet("""
                                            QLineEdit {
                                                font-family: 'Arial;
                                                font-size: 12px;
                                                font-weight: bold;
                                                border-radius: 15px;
                                                background-color: #f6f6f6;
                                            }
                                           """)
        self.senhalogin_edit.setFixedSize(300,30)
        self.senhalogin_edit.setAlignment(Qt.AlignCenter)

# REMEMBER-ME, FORGOT YOUR PASSWORD? ------------------------------------------------------------------------------------------------------------------------------------------------------------------

        self.rememberme_checkbox = QCheckBox("Remember-me")
        self.rememberme_checkbox.setStyleSheet("""
                                                margin-left: 260px;
                                                font-family: 'Arial';
                                                font-size: 12px;
                                               """)
        
        self.forgot_label = QLabel("Forgot your password?")
        self.forgot_label.setStyleSheet("""
                                            font-family: 'Arial';
                                            font-size: 12px;
                                            color: #00a2ff;
                                        """)

# BOTÃO LOGIN -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        self.login_botao = QPushButton("Login")
        self.login_botao.setStyleSheet("""
                                        QPushButton {
                                            font-family: 'Times New Roman';
                                            font-size: 16px;
                                            border-radius: 20px;
                                            color: #ffffff;
                                            background-color: #003cff;
                                        }
                                        QPushButton:hover {
                                            background-color: #0060ff;
                                        }
                                        QPushButton:pressed {
                                            background-color: #1200ff;
                                        }
                                       """)
        self.login_botao.setFixedSize(120,40)
        
# NEU USER? CREATE AN ACCOUNT, OR ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

        self.newuser_label = QLabel ("New User? Create an Account")
        self.newuser_label.setText("""
                                    New User? <span style='color:#00a2ff; text-decoration: underline;'>Create an Account</span>
                                   """)
        self.newuser_label.setStyleSheet("""
                                            font-family: 'Times New Roman';
                                            font-size: 15px;
                                         """)
        self.newuser_label.setAlignment(Qt.AlignCenter)
        
# -------------------------

        #self.create_label = QLabel ("Create an Account")
        #self.create_label.setStyleSheet("""
                                            #font-family: 'Times New Roman';
                                            #font-size: 15px;
                                            #text-decoration: underline;
                                            #color: #00a2ff;
                                        #""")
        
# -------------------------

        self.or_label = QLabel ("OR")
        self.or_label.setStyleSheet("""
                                        font-family: 'Arial';
                                        font-size: 12px;
                                    """)
        self.or_label.setAlignment(Qt.AlignCenter)

# WIDGET COLORIDA, LOGIN WITH FACEBOOK, LOGIN WITH GOOGLE ---------------------------------------------------------------------------------------------------------------------------------------------

        self.fundopreto_widget = QWidget()
        self.fundopreto_widget.setStyleSheet("""
                                                background-color: #1a1a45;
                                             """)

# -------------------------

        self.facebook_imagem = QLabel("Login with Facebook")
        self.facebook_imagem.setPixmap(QPixmap("facebookicon.png").scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.facebook_imagem.move(100,80)
        
# -------------------------

        self.google_imagem = QLabel("Login with Facebook")
        self.google_imagem.setPixmap(QPixmap("googleicon.png").scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.google_imagem.move(100,80)

# ADICIONANDO AS JANELAS E LAYOUTS --------------------------------------------------------------------------------------------------------------------------------------------------------------------

        self.normal = QVBoxLayout()
        self.setLayout(self.normal)
# -------------------------
        self.horizontal = QHBoxLayout()
# -------------------------
        self.horizontal_layout = QHBoxLayout()
# -------------------------
        self.normal.addWidget(self.emailvindo_label)
        self.normal.addWidget(self.loginpfv_label)
        self.normal.addWidget(self.emaillogin_label)
        self.normal.addWidget(self.emaillogin_edit, alignment=Qt.AlignCenter)
        self.normal.addWidget(self.senhalogin_label)
        self.normal.addWidget(self.senhalogin_edit, alignment=Qt.AlignCenter)

        self.normal.addLayout(self.horizontal) # Precisa ficar nessa posição
        self.horizontal.addWidget(self.rememberme_checkbox)
        self.horizontal.addWidget(self.forgot_label)

        self.normal.addSpacing(5)
        self.normal.addWidget(self.login_botao, alignment=Qt.AlignCenter)
        self.normal.addSpacing(20)
        self.normal.addWidget(self.newuser_label)
        self.normal.addSpacing(20)
        self.normal.addWidget(self.or_label)
        self.normal.addSpacing(20)

        self.horizontal_layout.addStretch(1) # Precisa ficar nessa posição
        self.horizontal_layout.addWidget(self.facebook_imagem)
        self.horizontal_layout.addWidget(self.google_imagem)
        self.horizontal_layout.addStretch(1)

        self.fundopreto_widget.setLayout(self.horizontal_layout)
        self.normal.addWidget(self.fundopreto_widget)

# MANIPULANDO AS MARGINS/ESPAÇOS ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Geometry: (50, 50, 1200, 800)
# Lembre-se: Esquerda, Cima, Direita, Baixo (afastar das bordas)

        self.normal.addStretch(1)
# -------------------------
        self.emailvindo_label.setContentsMargins(50,100,50,0)
        self.loginpfv_label.setContentsMargins(50,0,50,40)

        self.horizontal.addSpacing(-100)
        self.horizontal.setContentsMargins(0,0,100,0)
# -------------------------
        self.horizontal_layout.setSpacing(60) #espaço entre as imagens

# Estes são controlados pelo addStretch

        #self.emaillogin_label.setContentsMargins(0,0,0,0)
        #self.emaillogin_edit.setContentsMargins(0,0,0,0)
        #self.senhalogin_label.setContentsMargins(0,0,0,0)
        #self.senhalogin_edit.setContentsMargins(0,0,0,0)
        #self.or_label.setContentsMargins(0,0,0,0)
        #self.fundopreto_widget.setContentsMargins(0,0,0,400)

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

app = QApplication(sys.argv)
janela = logincadastro()
janela.show()
app.exec_()