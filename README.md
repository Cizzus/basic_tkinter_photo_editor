# Basic Tkinter Photo Editor

A simple photo editing application built using Tkinter and Pillow. This application allows users to perform basic photo editing tasks such as resizing images, adjusting brightness and contrast, adding watermarks, and more.

## Features

- **Load and Display Images**: Open and display images in the application.
- **Resize Images**: Resize images to specified dimensions.
- **Adjust Brightness**: Increase or decrease the brightness of images.
- **Adjust Contrast**: Increase or decrease the contrast of images.
- **Add Icons**: Overlay an icon on the image.
- **Add Watermarks**: Add customizable text watermarks to images.
- **Undo Changes**: Undo the last change made to the image.
- **Save Images**: Save the edited image in JPEG or PNG format.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Cizzus/basic_tkinter_photo_editor.git
    ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```bash
    python main.py
    ```

## Usage

1. **Load an Image**:
    - Click the "Find Image" button to open a file dialog and select an image file.

2. **Resize the Image**:
    - Enter the desired width and height in the entry fields and click the "Resize Image" button.

3. **Adjust Brightness and Contrast**:
    - Use the "+" and "-" buttons next to the Brightness and Contrast labels to increase or decrease these properties.

4. **Add an Icon**:
    - Click the "Add Icon" button to overlay an icon onto the image.

5. **Add a Watermark**:
    - Click the "Add Watermark" button to add a customizable text watermark to the image.
    - Configure watermark options through the "Watermark Options" menu item or the Ctrl+W shortcut.

6. **Undo Changes**:
    - Click the "↩Undo" button or use the Ctrl+Z shortcut to undo the last change.

7. **Save the Edited Image**:
    - Select "Save" from the Options menu or use the Ctrl+S shortcut to open the save dialog.
    - Choose the image format (JPEG or PNG), specify the file name, and save the image.

## Keyboard Shortcuts

- **Ctrl+S**: Save the image.
- **Ctrl+W**: Open watermark options.
- **Ctrl+Z**: Undo the last change.

## Project Structure

- **main.py**: Initializes the Tkinter window, sets up the UI, and binds functions to UI elements.
- **img_update_functions.py**: Contains functions for image manipulation (e.g., resizing, adjusting brightness and contrast, adding watermarks and icons, saving).

## Dependencies

- **Tkinter**: Standard GUI library for Python.
- **Pillow**: Python Imaging Library (PIL) fork for image processing.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](https://en.wikipedia.org/wiki/MIT_License) file for details.

## Contacts 

If you have any questions or need further assistance, contact Ernestas Čižus at ernestas.cizus@gmail.com.