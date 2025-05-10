                                                  QR Code Generator 
Overview
--------
This script creates a GUI-based QR Code Generator using Python. Users can input any text or URL,
and the application generates a QR code for that input. The QR code is displayed within the
interface and automatically saved with a unique filename in the current directory.

Dependencies
------------
- tkinter: For GUI creation
- qrcode: For generating QR codes
- PIL (Pillow): For image processing and display
- io: For handling in-memory image data
- os: For checking existing filenames
Modules and Functions
---------------------
1. draw_gradient(canvas, width, height, r1, g1, b1, r2, g2, b2)
 Draws a vertical gradient background on the canvas.
 Parameters:
 - canvas: Tkinter canvas widget
 - width, height: Canvas dimensions
 - r1, g1, b1: Starting RGB color
 - r2, g2, b2: Ending RGB color
2. get_next_filename()
 Generates a unique filename (qr_code_X.png) that does not already exist in the directory.
 Returns: A string representing the next available filename.
3. generate_qr()
 Main function triggered by the "Generate QR Code" button.
 Performs the following:
 - Retrieves user input
 - Validates input
 - Generates the QR code
 - Displays the QR code in the GUI
 - Saves the QR code image with a unique name
 - Notifies the user of success or error
GUI Components
--------------
- Tkinter root window (400x400)
- Gradient canvas background
- Label: "Enter text or URL:"
- Entry widget: To input data
- Button: "Generate QR Code"
- Label: To display the generated QR code
The canvas layout is used to place all widgets with exact positioning for better control.
QR Code Saving
--------------
QR codes are saved as qr_code_1.png, qr_code_2.png, etc., ensuring no overwriting of previous
files.
Design Aesthetics
-----------------
- Light blue to purple gradient background using rectangles
- Labels and buttons styled with pastel colors for a soft look
- Images resized for consistent display within the GUI
How to Run
----------
1. Ensure you have all dependencies installed:
 pip install qrcode[pil] pillow
2. Save the script to a .py file and run it using Python:
 python qr_generator.py
Output
------
- Visual display of generated QR code in the application window
- PNG image of the QR code saved in the script's directory


![Screenshot 2025-05-10 202729](https://github.com/user-attachments/assets/044278fa-6931-4fb0-8486-7b1842a5d86e)
