import sys
import webbrowser

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QInputDialog,QMessageBox

# ---------------------------- CRIANDO E NOMEANDO A JANELA ----------------------------
class Caixa(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Caixa")

        self.setGeometry(50,50,1200,800)
        self.setFixedSize(1200,800)
# ---------------------------- CONFIGURANDO A IMAGEM ----------------------------
        self.imagem_label = QLabel()
        self.imagem_label.setPixmap(QPixmap("padaria2.jpg"))
        self.imagem_label.setScaledContents(True)
        self.imagem_label.setFixedSize(600,300)
# ---------------------------- ADICIONANDO AS CAIXAS DE INSERÇÃO ----------------------------
        self.codigo_label = QLabel("Código do Produto")
        self.codigo_label.setStyleSheet("QLabel{font-size:10pt}")

        self.codigo_edit = QLineEdit()
        self.codigo_edit.setStyleSheet("QLineEdit{font-size:20pt}")



        self.nome_label = QLabel("Nome do Produto")
        self.nome_label.setStyleSheet("QLabel{font-size:10pt}")

        self.nome_edit = QLineEdit()
        self.nome_edit.setStyleSheet("QLineEdit{font-size:20pt}")



        self.descricao_label = QLabel("Descrição do Produto")
        self.descricao_label.setStyleSheet("QLabel{font-size:10pt}")

        self.descricao_edit = QLineEdit()
        self.descricao_edit.setStyleSheet("QLineEdit{font-size:50pt}")



        self.quantidade_label = QLabel("Quantidade do Produto")
        self.quantidade_label.setStyleSheet("QLabel{font-size:10pt}")

        self.quantidade_edit = QLineEdit()
        self.quantidade_edit.setStyleSheet("QLineEdit{font-size:20pt}")



        self.preco_label = QLabel("Preço do Produto")
        self.preco_label.setStyleSheet("QLabel{font-size:10pt}")

        self.preco_edit = QLineEdit()
        self.preco_edit.setStyleSheet("QLineEdit{font-size:20pt}")



        self.subtotal_label = QLabel("Sub Total")
        self.subtotal_label.setStyleSheet("QLabel{font-size:10pt}")

        self.subtotal_edit = QLineEdit("Tecle F3 para calcular o subtotal")
        self.subtotal_edit.setStyleSheet("QLineEdit{font-size:20pt}")



# ---------------------------- CRIANDO A TABELA DO LADO DIREITO ----------------------------
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(5)
        self.tabela.setRowCount(8)
# ---------------------------- ADICIONANDO OS ITENS DA TABELA ----------------------------
        #self.tabela.setItem(0,0,QTableWidgetItem("Código"))
        #self.tabela.setItem(0,1,QTableWidgetItem("Nome Produto"))
        #self.tabela.setItem(0,2,QTableWidgetItem("Quantidade"))
        #self.tabela.setItem(0,3,QTableWidgetItem("Preço Utilitário"))
        #self.tabela.setItem(0,4,QTableWidgetItem("Preço Total"))
# ---------------------------- ADICIONANDO O PREÇO TOTAL ----------------------------
        self.linha = 0
        self.total = 0.00

        self.total_label = QLabel("Total a pagar")
        self.total_label.setStyleSheet("QLabel{font-size:10pt}")

        self.total_edit = QLineEdit("0,00")
        self.total_edit.setStyleSheet("QLineEdit{font-size:50pt}")





# ---------------------------- ADICIONANDO AS JANELAS E LAYOUTS ----------------------------
        self.horizontal_layout = QHBoxLayout()
        self.setLayout(self.horizontal_layout)
# ------------------------------------------------------------------------------------
        self.vertical_esquerda_layout = QVBoxLayout()

        self.vertical_esquerda_layout.addWidget(self.imagem_label)
        self.vertical_esquerda_layout.addWidget(self.codigo_label)
        self.vertical_esquerda_layout.addWidget(self.codigo_edit)
        self.vertical_esquerda_layout.addWidget(self.nome_label)
        self.vertical_esquerda_layout.addWidget(self.nome_edit)
        self.vertical_esquerda_layout.addWidget(self.descricao_label)
        self.vertical_esquerda_layout.addWidget(self.descricao_edit)
        self.vertical_esquerda_layout.addWidget(self.quantidade_label)
        self.vertical_esquerda_layout.addWidget(self.quantidade_edit)
        self.vertical_esquerda_layout.addWidget(self.preco_label)
        self.vertical_esquerda_layout.addWidget(self.preco_edit)
        self.vertical_esquerda_layout.addWidget(self.subtotal_label)
        self.vertical_esquerda_layout.addWidget(self.subtotal_edit)

        self.coluna_esquerda_label = QLabel()
        self.coluna_esquerda_label.setStyleSheet("QLabel{background-color:brown}")
        self.coluna_esquerda_label.setLayout(self.vertical_esquerda_layout)
        self.horizontal_layout.addWidget(self.coluna_esquerda_label)
# ------------------------------------------------------------------------------------
        self.vertical_direita_layout = QVBoxLayout()

        self.vertical_direita_layout.addWidget(self.tabela)
        self.vertical_direita_layout.addWidget(self.total_label)
        self.vertical_direita_layout.addWidget(self.total_edit)

        self.coluna_direita_label = QLabel()
        self.coluna_direita_label.setStyleSheet("QLabel{background-color:#D3D3D3}")
        self.coluna_direita_label.setLayout(self.vertical_direita_layout)
        self.horizontal_layout.addWidget(self.coluna_direita_label)
# ------------------------------------------------------------------------------------
#keypress quando aperta (ira disparar o evento), key release quando vc solta a tecla.
        self.keyPressEvent = self.capturaTecla

    #voltar 1 função e usar o def para capturar
    # === CAPTURA DE TECLAS ===
    def capturaTecla(self, e):
        # F2 → calcula subtotal
        if e.key() == Qt.Key_F2:
            try:
                quantidade = float(self.quantidade_edit.text())
                preco = float(self.preco_edit.text())
                subtotal = quantidade * preco
                self.subtotal_edit.setText(f"{subtotal:.2f}")
            except ValueError:
                QMessageBox.warning(self, "Erro", "Digite valores numéricos válidos!")

        # F3 → adiciona item à tabela e soma total
        elif e.key() == Qt.Key_F3:
            try:
                codigo = self.codigo_edit.text()
                nome = self.nome_edit.text()
                quantidade = float(self.quantidade_edit.text())
                preco = float(self.preco_edit.text())
                subtotal = quantidade * preco

                self.tabela.insertRow(self.linha)
                self.tabela.setItem(self.linha, 0, QTableWidgetItem(codigo))
                self.tabela.setItem(self.linha, 1, QTableWidgetItem(nome))
                self.tabela.setItem(self.linha, 2, QTableWidgetItem(str(quantidade)))
                self.tabela.setItem(self.linha, 3, QTableWidgetItem(f"{preco:.2f}"))
                self.tabela.setItem(self.linha, 4, QTableWidgetItem(f"{subtotal:.2f}"))

                # soma no total geral
                self.total += subtotal
                self.total_edit.setText(f"{self.total:.2f}")

                self.linha += 1


            except ValueError:
                QMessageBox.warning(self, "Erro", "Preencha os campos corretamente!")

        # F4 → confirma pagamento
        elif(e.key()==Qt.Key_F4):
            op = QMessageBox.question(self,"Pagamento","Deseja efetuar o pagamento?")
            if op == QMessageBox.Yes:
                rs,ok = QInputDialog().getText(self,"Forma Pagamento","Escolha uma forma de Pagamento:\n1 - Pix\n2 - Cartão de Crédito\n3 - Cartão de Débito\n4 - Dinheiro\n5 - Voucher")
                if ok :
                # vamos criar uma lista(array) para guardar TODOS os dados da tabela para criar uma nota fiscal
                        dados = []
                        for linha in range(self.tabela.rowCount()):
                            dados_linha = []
                            for coluna in range(self.tabela.columnCount()):
                                item = self.tabela.item(linha,coluna)
                                if item:
                                    dados_linha.append(item.text())
                                else:
                                    break
                                        # dados_linha.append("")
                            dados.append(dados_linha)
                        nota = """
                                <html>
                                <head>
                                <title> Nota Fiscal </title>
                                <style>
                                    body{
                                    text-align:center;
                                    }
                                    table{
                                    margin-left:auto;
                                    margin-right:auto;
                                    border:10px solid black;
                                    text-align:center;
                                    }
                                    table, td, td {
                                    border:5px solid black;
                                    border-collapse: collapse;
                                    }
                                
                                </style>

                                </head>
                                <body>
                                <h1>Nota Fiscal de Compra</h1>
                                <table>
                                <tr>
                                    <th>Cód.</th>
                                    <th>Descrição</th>
                                    <th>Qtd.</th>
                                    <th>Preço</th>
                                    <th>Preço Total</th>
                                </tr>
                            """
                        for lin in dados:
                                nota = nota+"<tr>"
                                for col in lin:
                                    nota = nota+"<td>"+col+"</td>"
                                nota = nota+"</tr>"

                        nota = nota + """
                                
                                </table>
                                </body>
                                </html>
                            """
                        arq = open("nota.html","w")
                        arq.write(nota)
                        arq.close()
                        webbrowser.open("nota.html")
                    
            else:
                # vamos criar uma lista(array) para guardar TODOS os dados da tabela para criar uma nota fiscal
                dados = []
                for linha in range(self.tabela.rowCount()):
                    dados_linha = []
                    for coluna in range(self.tabela.columnCount()):
                        item = self.tabela.item(linha,coluna)
                        if item:
                            dados_linha.append(item.text())
                        else:
                            break
                            # dados_linha.append("")
                        dados.append(dados_linha)
                print(dados)



# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

app = QApplication(sys.argv)
janela = Caixa()
janela.show()
app.exec_()