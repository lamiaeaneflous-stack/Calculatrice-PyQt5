from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLineEdit,
    QPushButton
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Calculatrice(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculatrice PyQt5")
        self.setFixedSize(350, 500)
        self.expression = ""
        self.creer_interface()
    def creer_interface(self):
        layout = QVBoxLayout()
        self.affichage = QLineEdit()
        self.affichage.setReadOnly(True)
        self.affichage.setAlignment(Qt.AlignRight)
        self.affichage.setFont(QFont("Arial", 24))
        layout.addWidget(self.affichage)
        grille = QGridLayout()
        boutons = [
            ("C", 0, 0),
            ("/", 0, 1),
            ("*", 0, 2),
            ("-", 0, 3),

            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("+", 1, 3),

            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("=", 2, 3),

            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            (".", 3, 3),

            ("0", 4, 0)
        ]
        for texte, ligne, colonne in boutons:
            bouton = QPushButton(texte)
            bouton.setFont(QFont("Arial", 18))
            bouton.setMinimumHeight(60)
            bouton.clicked.connect(
                lambda checked, t=texte:
                self.cliquer_bouton(t)
            )
            grille.addWidget(bouton, ligne, colonne)
        layout.addLayout(grille)
        self.setLayout(layout)
        self.setStyleSheet("""
            QWidget {
                background-color: #202124;
            }
            QLineEdit {
                background-color: #303134;
                color: white;
                border: none;
                padding: 15px;
            }
            QPushButton {
                background-color: #3C4043;
                color: white;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #5F6368;
            }
        """)
    def cliquer_bouton(self, texte):
        if texte == "C":
            self.expression = ""
            self.affichage.clear()
        elif texte == "=":
            try:
                resultat = eval(
                    self.expression,
                    {"__builtins__": {}},
                    {}
                )
                self.expression = str(resultat)
                self.affichage.setText(self.expression)
            except:
                self.expression = ""
                self.affichage.setText("Erreur")
        else:
            self.expression += texte
            self.affichage.setText(self.expression)
