import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QPushButton, QFileDialog, QTextEdit, QLabel

class SequenceAlignmentApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sequence Alignment GUI')
        self.setGeometry(100, 100, 600, 400)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.pairwise_tab = QWidget()
        self.multiple_tab = QWidget()

        self.tabs.addTab(self.pairwise_tab, 'Pairwise Alignment')
        self.tabs.addTab(self.multiple_tab, 'Multiple Sequence Alignment')

        self.init_pairwise_tab()  
        self.init_multiple_tab()

    def init_pairwise_tab(self):
        layout = QVBoxLayout()
        self.input_text = QTextEdit()
        self.result_text = QTextEdit()
        self.align_button = QPushButton('Align')
        self.align_button.clicked.connect(self.pairwise_align)
        layout.addWidget(QLabel('Input Sequences:'))
        layout.addWidget(self.input_text)
        layout.addWidget(self.align_button)
        layout.addWidget(QLabel('Alignment Result:'))
        layout.addWidget(self.result_text)

        self.pairwise_tab.setLayout(layout)

    def init_multiple_tab(self):
        layout = QVBoxLayout()
        self.input_text_multi = QTextEdit()
        self.result_text_multi = QTextEdit()
        self.file_button = QPushButton('Load File')
        self.align_multi_button = QPushButton('Align Multiple')
        self.file_button.clicked.connect(self.load_file)
        self.align_multi_button.clicked.connect(self.multiple_align)
        layout.addWidget(QLabel('Input Sequences:'))
        layout.addWidget(self.input_text_multi)
        layout.addWidget(self.file_button)
        layout.addWidget(self.align_multi_button)
        layout.addWidget(QLabel('Alignment Result:'))
        layout.addWidget(self.result_text_multi)

        self.multiple_tab.setLayout(layout)

    def load_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, 'Open Sequence File', '', 'Text Files (*.txt);;All Files (*)', options=options)
        if filename:
            with open(filename, 'r') as file:
                self.input_text_multi.setPlainText(file.read())

    def pairwise_align(self):
        seqs = self.input_text.toPlainText().split('\n')
        # Implement your pairwise alignment algorithm here
        result = '\n'.join(seqs)  # Placeholder for actual results
        self.result_text.setPlainText(result)

    def multiple_align(self):
        seqs = self.input_text_multi.toPlainText().split('\n')
        # Implement your multiple sequence alignment algorithm here
        result_multi = '\n'.join(seqs)  # Placeholder for actual results
        self.result_text_multi.setPlainText(result_multi)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SequenceAlignmentApp()
    window.show()
    sys.exit(app.exec_())