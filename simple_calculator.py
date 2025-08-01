"""
name: Simple Calculator
author: Ayden
version: 1.0.0
description: Performs basic arithmetic operations (add, subtract, multiply, divide)
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QComboBox, QPushButton, QLabel, QFormLayout
from PySide6.QtCore import Qt

class PluginWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        form = QFormLayout()

        self.num1_input = QLineEdit()
        self.num2_input = QLineEdit()
        form.addRow("Number 1:", self.num1_input)
        form.addRow("Number 2:", self.num2_input)

        self.operator_box = QComboBox()
        self.operator_box.addItems(["+", "-", "×", "÷"])
        form.addRow("Operation:", self.operator_box)

        layout.addLayout(form)

        self.calc_button = QPushButton("Calculate")
        self.calc_button.clicked.connect(self.calculate)
        layout.addWidget(self.calc_button)

        self.result_label = QLabel("Result will appear here")
        self.result_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def run(self):
        """Reset all fields when plugin is launched"""
        self.num1_input.clear()
        self.num2_input.clear()
        self.operator_box.setCurrentIndex(0)
        self.result_label.setText("Result will appear here")

    def calculate(self):
        try:
            num1 = float(self.num1_input.text())
            num2 = float(self.num2_input.text())
            op = self.operator_box.currentText()

            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "×":
                result = num1 * num2
            elif op == "÷":
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                result = num1 / num2
            else:
                self.result_label.setText("Invalid operation")
                return

            self.result_label.setText(f"Result: {result:.4f}")
        except ValueError:
            self.result_label.setText("Please enter valid numbers")
        except ZeroDivisionError as e:
            self.result_label.setText(str(e))