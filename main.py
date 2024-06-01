from tkinter import Tk, Label, Button, Entry, Menu, PhotoImage
from PIL import Image, ImageTk
from img_update_functions import file_open, resize_image, add_icon, add_watermark, watermark_options, undo, \
    default_image, adjust_brightness, adjust_contrast, save

# Initialize the main application window
app = Tk()
app.title("Image Editor")

# Set the window icon
icon_image = PhotoImage(file=r"./media/photo-album--pencil.png")
app.iconphoto(False, icon_image)

# Load the default image and set it as a thumbnail
default_image.thumbnail(size=(9999, 9999), resample=Image.Resampling.LANCZOS)
default_image_test = ImageTk.PhotoImage(default_image)
image_label = Label(app, image=default_image_test)

# Labels for various UI elements
x_label = Label(text="x")
size_label = Label(text="")
brightness_label = Label(text="Brightness:")
contrast_label = Label(text="Contrast:")

# Create a Menubar
menubar = Menu()
file_menu = Menu(menubar, tearoff=False)

# File menu with options

# Save a photo option
menubar.add_cascade(menu=file_menu, label="Options")
file_menu.add_command(
    label="Save",
    accelerator="Ctrl+S",
    command=save
)

# Binding shortcut keys to save a photo
app.bind("<Control-s>", lambda event: save())
app.bind("<Control-S>", lambda event: save())

# Watermark options
file_menu.add_command(
    label="Watermark Options",
    accelerator="Ctrl+W",
    command=watermark_options
)

# Binding shortcut keys for watermark options
app.bind("<Control-w>", lambda event: watermark_options())
app.bind("<Control-W>", lambda event: watermark_options())

file_menu.insert_separator(2)

# Exit option in menubar
file_menu.add_command(
    label="Exit",
    command=app.destroy
)

# Entry widgets for image resizing

resize_img_width = Entry(width=5)
resize_img_width.insert(0, str(default_image.width))
resize_img_height = Entry(width=5)
resize_img_height.insert(0, str(default_image.height))

# Buttons for various functions

# First layer buttons
undo_button = Button(text="↩Undo", command=lambda: undo(image_label))
# Shortcuts to use undo function
app.bind("<Control-z>", lambda event: undo(image_label))
app.bind("<Control-Z>", lambda event: undo(image_label))

# Second layer buttons

add_brightness_button = Button(text="+", width=2, command=lambda: adjust_brightness(image_label, "increase"))
reduce_brightness_button = Button(text="-", width=2, command=lambda: adjust_brightness(image_label, "decrease"))

add_contrast_button = Button(text="+", width=2, command=lambda: adjust_contrast(image_label, "increase"))
reduce_contrast_button = Button(text="-", width=2, command=lambda: adjust_contrast(image_label, "decrease"))

# Third layer buttons

find_img_button = Button(text="Find Image", command=lambda: file_open(image_label, size_label))
icon_button = Button(text="Add Icon", command=lambda: add_icon(image_label))
watermark_button = Button(text="Add Watermark", command=lambda: add_watermark(image_label))

# Fourth layer buttons

resize_button = Button(text="Resize Image", command=lambda: resize_image(image_label, int(resize_img_width.get()),
                                                                         int(resize_img_height.get())))

# Place UI elements on the grid

# Image
image_label.grid_configure(column=0, row=0)

# First layer of options

undo_button.grid_configure(column=0, row=1, sticky="w", pady=5, padx=5)
brightness_label.grid_configure(column=0, row=1, sticky="w", padx=55)
contrast_label.grid_configure(column=0, row=1, sticky="w", padx=120)

# Second layer of options

brightness_label.grid_configure(column=0, row=2, sticky="w", padx=5)
add_brightness_button.grid_configure(column=0, row=2, sticky="w", padx=70)
reduce_brightness_button.grid_configure(column=0, row=2, sticky="w", padx=95)

contrast_label.grid_configure(column=0, row=2, sticky="w", pady=10, padx=140)
add_contrast_button.grid_configure(column=0, row=2, sticky="w", pady=10, padx=205)
reduce_contrast_button.grid_configure(column=0, row=2, sticky="w", pady=10, padx=230)

# Third layer of options

find_img_button.grid_configure(column=0, row=3, sticky="w", pady=10, padx=5)
icon_button.grid_configure(column=0, row=3, sticky="w", padx=75)
watermark_button.grid_configure(column=0, row=3, sticky="w", padx=135)

# Fifth layer of options

resize_img_width.grid_configure(column=0, row=4, pady=4, sticky="w", padx=5)
resize_img_height.grid_configure(column=0, row=4, sticky="w", padx=50)
resize_button.grid_configure(column=0, row=4, sticky="w", padx=85)
x_label.grid_configure(column=0, row=4, sticky="w", padx=38)
size_label.grid_configure(column=0, row=4, sticky="w", padx=165)

# Set the menubar and start the application
if __name__ == "__main__":
    app.config(menu=menubar)
    app.mainloop()
