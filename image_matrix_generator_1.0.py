import os
import json
from PIL import Image, ImageDraw
from concurrent.futures import ThreadPoolExecutor
import multiprocessing
import subprocess
import platform
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QPushButton, QLineEdit, QFileDialog, QMessageBox, 
                             QColorDialog, QStackedWidget, QFrame, QStatusBar, QFormLayout)
from PyQt5.QtGui import QColor, QFont, QPalette
from PyQt5.QtCore import Qt

class ImageMatrixGeneratorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Matrix Generator")
        self.setGeometry(100, 100, 1000, 600)  # Increased width to accommodate instructions

        self.config_file = 'image_matrix_config.json'
        self.last_directory = self.load_last_directory()

        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # Left column for existing elements
        left_column = QVBoxLayout()
        self.add_ascii_art(left_column)
        self.create_form(left_column)
        self.add_generate_button(left_column)
        main_layout.addLayout(left_column, 2)  # 2/3 of the width

        # Right column for instructions
        right_column = QVBoxLayout()
        self.add_instructions(right_column)
        main_layout.addLayout(right_column, 1)  # 1/3 of the width

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")

    def add_ascii_art(self, layout):
        ascii_art = """
   ██▓ ███▄ ▄███▓ ▄▄▄        ▄████ ▓█████     ███▄ ▄███▓ ▄▄▄     ▄▄▄█████▓ ██▀███   ██▓▒██   ██▒     ▄████ ▓█████  ███▄    █ 
  ▓██▒▓██▒▀█▀ ██▒▒████▄     ██▒ ▀█▒▓█   ▀    ▓██▒▀█▀ ██▒▒████▄   ▓  ██▒ ▓▒▓██ ▒ ██▒▓██▒▒▒ █ █ ▒░    ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
  ▒██▒▓██    ▓██░▒██  ▀█▄  ▒██░▄▄▄░▒███      ▓██    ▓██░▒██  ▀█▄ ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██▒░░  █   ░   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
  ░██░▒██    ▒██ ░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄    ▒██    ▒██ ░██▄▄▄▄██░ ▓██▓ ░ ▒██▀▀█▄  ░██░ ░ █ █ ▒    ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
  ░██░▒██▒   ░██▒ ▓█   ▓██▒░▒▓███▀▒░▒████▒   ▒██▒   ░██▒ ▓█   ▓██▒ ▒██▒ ░ ░██▓ ▒██▒░██░▒██▒ ▒██▒   ░▒▓███▀▒░▒████▒▒██░   ▓██░
  ░▓  ░ ▒░   ░  ░ ▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░   ░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒▓ ░▒▓░░▓  ▒▒ ░ ░▓ ░    ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
   ▒ ░░  ░      ░  ▒   ▒▒ ░  ░   ░  ░ ░  ░   ░  ░      ░  ▒   ▒▒ ░   ░      ░▒ ░ ▒░ ▒ ░░░   ░▒ ░     ░   ░  ░ ░  ░░ ░░   ░ ▒░
   ▒ ░░      ░     ░   ▒   ░ ░   ░    ░      ░      ░     ░   ▒    ░        ░░   ░  ▒ ░ ░    ░     ░ ░   ░    ░      ░   ░ ░ 
   ░         ░         ░  ░      ░    ░  ░          ░         ░  ░           ░      ░   ░    ░           ░    ░  ░         ░ 
                                                                                                                             
"""
        ascii_art_label = QLabel(ascii_art)
        ascii_art_label.setFont(QFont("Courier", 8))
        ascii_art_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(ascii_art_label)

    def create_form(self, layout):
        form_layout = QFormLayout()
        
        self.input_folder_edit = QLineEdit(self.last_directory)
        self.output_folder_edit = QLineEdit(self.last_directory)
        self.rows_edit = QLineEdit("3")
        self.cols_edit = QLineEdit("3")
        self.base_filename_edit = QLineEdit("matrix")
        self.border_thickness_edit = QLineEdit("2")
        
        self.color_preview = QLabel()
        self.color_preview.setFixedSize(20, 20)
        self.color_preview.setStyleSheet("background-color: #000000; border: 1px solid #cccccc;")
        color_layout = QHBoxLayout()
        color_layout.addWidget(self.color_preview)
        color_layout.addWidget(QPushButton("Choose", clicked=self.choose_color))

        form_layout.addRow("Input Folder:", self.create_browse_layout(self.input_folder_edit, self.browse_input))
        form_layout.addRow("Output Folder:", self.create_browse_layout(self.output_folder_edit, self.browse_output))
        form_layout.addRow("Rows:", self.rows_edit)
        form_layout.addRow("Columns:", self.cols_edit)
        form_layout.addRow("Base Filename:", self.base_filename_edit)
        form_layout.addRow("Border Thickness:", self.border_thickness_edit)
        form_layout.addRow("Border Color:", color_layout)

        layout.addLayout(form_layout)

    def create_browse_layout(self, line_edit, browse_function):
        layout = QHBoxLayout()
        layout.addWidget(line_edit)
        layout.addWidget(QPushButton("Browse", clicked=browse_function))
        return layout

    def add_generate_button(self, layout):
        generate_button = QPushButton("Generate Matrix")
        generate_button.setFixedSize(150, 30)
        generate_button.clicked.connect(self.generate_matrix)
        
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(generate_button)
        button_layout.addStretch()
        
        layout.addLayout(button_layout)
        layout.addSpacing(20)

    def add_instructions(self, layout):
        instructions = """
        <h3>Instructions:</h3>
        <ol>
            <li><b>Input Folder:</b> Select the folder containing your images.</li>
            <li><b>Output Folder:</b> Choose where to save the generated matrices.</li>
            <li><b>Rows:</b> Enter the number of rows for each matrix.</li>
            <li><b>Columns:</b> Enter the number of columns for each matrix.</li>
            <li><b>Base Filename:</b> Set the base name for output files.</li>
            <li><b>Border Thickness:</b> Set the thickness of borders between images (0 for no borders).</li>
            <li><b>Border Color:</b> Choose the color for the borders.</li>
            <li>Click <b>'Generate Matrix'</b> to create your image matrices.</li>
        </ol>
        <p><b>Note:</b> The program will process all images in the input folder and create multiple matrices if necessary.</p>
        <p><b>Warning:</b> This program can generate very large images. Be careful with your settings. For example, a 10x10 matrix of 1080x1920 images will result in a 10,800x19,200 pixel image per batch!</p>
        """
        instructions_label = QLabel(instructions)
        instructions_label.setWordWrap(True)
        instructions_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        instructions_label.setStyleSheet("""
            background-color: #f0f0f0; 
            padding: 15px; 
            border-radius: 5px;
            font-size: 12px;
        """)
        instructions_label.setTextFormat(Qt.RichText)
        layout.addWidget(instructions_label)

    def browse_input(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Input Folder", self.last_directory)
        if folder:
            self.input_folder_edit.setText(folder)
            self.output_folder_edit.setText(folder)
            self.save_last_directory(folder)

    def browse_output(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Output Folder", self.input_folder_edit.text())
        if folder:
            self.output_folder_edit.setText(folder)

    def load_last_directory(self):
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                return config.get('last_directory', '/')
        except (FileNotFoundError, json.JSONDecodeError):
            return '/'

    def save_last_directory(self, directory):
        config = {'last_directory': directory}
        with open(self.config_file, 'w') as f:
            json.dump(config, f)

    def generate_matrix(self):
        input_folder = self.input_folder_edit.text()
        output_folder = self.output_folder_edit.text()
        rows = int(self.rows_edit.text())
        cols = int(self.cols_edit.text())
        base_filename = self.base_filename_edit.text()
        border_thickness = int(self.border_thickness_edit.text())
        border_color = self.color_preview.styleSheet().split(":")[1].split(";")[0].strip()

        if not all([input_folder, output_folder, rows, cols, base_filename, border_thickness, border_color]):
            QMessageBox.critical(self, "Error", "All fields must be filled")
            return

        if not os.path.exists(input_folder):
            QMessageBox.critical(self, "Error", "Input folder does not exist")
            return

        if not os.path.exists(output_folder):
            QMessageBox.critical(self, "Error", "Output folder does not exist")
            return

        generator = ImageMatrixGenerator(input_folder, output_folder, rows, cols, base_filename, border_thickness, border_color)
        generator.generate_matrix()

        QMessageBox.information(self, "Success", "Image matrix generation complete!")
        self.open_output_folder(output_folder)

    def open_output_folder(self, path):
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":  # macOS
            subprocess.Popen(["open", path])
        else:  # Linux and other Unix-like
            subprocess.Popen(["xdg-open", path])

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color_preview.setStyleSheet(f"background-color: {color.name()}; border: 1px solid #cccccc;")

class ImageMatrixGenerator:
    def __init__(self, input_folder, output_folder, rows, cols, base_filename, border_thickness, border_color):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.rows = rows
        self.cols = cols
        self.base_filename = base_filename
        self.border_thickness = border_thickness
        self.border_color = border_color

    def generate_matrix(self):
        input_folder = self.input_folder
        output_folder = self.output_folder
        num_rows = self.rows
        num_cols = self.cols
        base_filename = self.base_filename

        if not os.path.exists(input_folder):
            print("Error: Input folder does not exist.")
            return

        if not os.path.exists(output_folder):
            print("Error: Output folder does not exist.")
            return

        # Collect image paths
        image_paths = [
            os.path.join(input_folder, filename)
            for filename in os.listdir(input_folder)
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))
        ]

        if not image_paths:
            print("Error: No images found in the input folder.")
            return

        # Get the size of the first image
        with Image.open(image_paths[0]) as first_image:
            image_width, image_height = first_image.size

        cell_size = (image_width, image_height)
        batch_size = num_rows * num_cols

        total_batches = (len(image_paths) + batch_size - 1) // batch_size
        print(f"Total batches to process: {total_batches}")

        # Use a ThreadPoolExecutor for parallel processing
        with ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
            futures = [executor.submit(self.load_and_resize_image, path, cell_size) for path in image_paths]
            images = [future.result() for future in futures]

        for batch_count, start_index in enumerate(range(0, len(images), batch_size)):
            batch_images = images[start_index:start_index + batch_size]
            output_filename = f"{base_filename}_{batch_count + 1}.jpg"
            output_path = os.path.join(output_folder, output_filename)
            self.process_batch(batch_images, num_rows, num_cols, cell_size, output_path)
            print(f"Batch {batch_count + 1}/{total_batches} completed: {output_path}")

        print("Image matrix generation complete!")

    def load_and_resize_image(self, path, target_size):
        with Image.open(path) as img:
            if img.format == 'GIF':
                img = img.convert('RGB')
            return img.resize(target_size)

    def process_batch(self, batch_images, num_rows, num_cols, cell_size, output_path):
        matrix_image = self.create_image_matrix(batch_images, num_rows, num_cols, cell_size)
        matrix_image.save(output_path)

    def create_image_matrix(self, image_list, rows, cols, cell_size):
        border_thickness = self.border_thickness
        border_color = self.border_color

        matrix_width = cols * cell_size[0] + (cols + 1) * border_thickness
        matrix_height = rows * cell_size[1] + (rows + 1) * border_thickness
        matrix_image = Image.new('RGB', (matrix_width, matrix_height), color=border_color)
        draw = ImageDraw.Draw(matrix_image)

        for r in range(rows):
            for c in range(cols):
                img_index = r * cols + c
                if img_index < len(image_list):
                    x = c * (cell_size[0] + border_thickness) + border_thickness
                    y = r * (cell_size[1] + border_thickness) + border_thickness
                    matrix_image.paste(image_list[img_index], (x, y))

        return matrix_image

if __name__ == "__main__":
    app = QApplication([])
    window = ImageMatrixGeneratorUI()
    window.show()
    app.exec_()
