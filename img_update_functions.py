from tkinter import filedialog, colorchooser, Toplevel, Label, Entry, Button, Radiobutton, StringVar, DoubleVar, Scale, \
    PhotoImage
from PIL import Image, ImageTk, ImageFont, ImageDraw, ImageEnhance
import os

# Load the default image
default_image = Image.open("./media/default.png").convert("RGBA")

# Constants of picture parameters
IMG_STACK = [default_image]
WATERMARK_TEXT = "Watermark"
WATERMARK_TRANSPARENCY = 40
WATERMARK_COLOR = (0, 0, 0, WATERMARK_TRANSPARENCY)


def file_open(image_lab, size_label):
    """
    Open a file dialog to select an image, then load and display it.
    :param image_lab: tkinter.Label object to place image
    :param size_label: tkinter.Label object where original size of the image will be shown
    :return: None
    """
    file_path = filedialog.askopenfilename(
        title="Select an Image File", filetypes=[("Image files", ["*.jpg", "*.png"])]
    )
    if file_path:
        image = Image.open(file_path).convert("RGBA")
        IMG_STACK.append(image)
        image.thumbnail((500, 500), Image.Resampling.LANCZOS)
        test = ImageTk.PhotoImage(image)
        image_lab.configure(image=test)
        image_lab.image = test
        size_label.config(text=f"Original size: {test.width()}x{test.height()}")


def undo(image_lab, stack=None):
    """
     Undo the last image operation by popping the last image off the stack.
    :param image_lab: tkinter.Label object to place image
    :param stack: list of tkinter.PhotoImage objects where every step of customized photo is saved
    :return: None
    """
    if stack is None:
        stack = IMG_STACK
    if len(stack) <= 2:
        pass
    else:
        stack.pop()
        test = ImageTk.PhotoImage(stack[-1])
        image_lab.configure(image=test)
        image_lab.image = test


def adjust_brightness(image_lab, adjust_type: str):
    """
    Adjust the brightness of the image.
    :param image_lab: tkinter.Label object to place image
    :param adjust_type: str where one parameter 'increase' or 'decrease' will be given
    :return: None
    """
    image = IMG_STACK[-1]
    img_enhancer = ImageEnhance.Brightness(image)

    if adjust_type == "increase":
        img_enhanced = img_enhancer.enhance(1.1)
    elif adjust_type == "decrease":
        img_enhanced = img_enhancer.enhance(0.9)
    else:
        img_enhanced = img_enhancer.enhance(1.0)

    test = ImageTk.PhotoImage(img_enhanced)
    image_lab.configure(image=test)
    image_lab.image = test
    IMG_STACK.append(img_enhanced)


def adjust_contrast(image_lab, adjust_type):
    """
    Adjust the contrast of the image.
    :param image_lab: tkinter.Label object to place image
    :param adjust_type: str where one parameter 'increase' or 'decrease' will be given
    :return: None
    """
    image = IMG_STACK[-1]
    img_enhancer = ImageEnhance.Contrast(image)

    if adjust_type == "increase":
        img_enhanced = img_enhancer.enhance(1.1)
    elif adjust_type == "decrease":
        img_enhanced = img_enhancer.enhance(0.9)
    else:
        img_enhanced = img_enhancer.enhance(1.0)

    test = ImageTk.PhotoImage(img_enhanced)
    image_lab.configure(image=test)
    image_lab.image = test
    IMG_STACK.append(img_enhanced)


def resize_image(image_lab, width: int, height: int):
    """
    Resize the image to the specified width and height.
    :param image_lab: tkinter.Label object to place image
    :param width: int value of image width in pixels
    :param height: int value of image height in pixels
    :return: None
    """
    image = IMG_STACK[-1]
    image = image.resize((width, height))
    test = ImageTk.PhotoImage(image)
    image_lab.configure(image=test)
    image_lab.image = test
    IMG_STACK.append(image)


def add_icon(image_lab):
    """
    Add an icon to the image.
    :param image_lab: tkinter.Label object to place image
    :return: None
    """
    file_path = filedialog.askopenfilename(
        title="Select an Watermark Image File", filetypes=[("Image files", ["*.jpg", "*.png"])]
    )
    if file_path:
        icon_image = Image.open(file_path).convert("RGBA")
        current_image = IMG_STACK[-1]
        new_image = Image.new(mode="RGBA", size=current_image.size)
        icon_image.thumbnail(((int(current_image.width * 0.15)), int(current_image.height * 0.15)))
        new_image.paste(current_image, mask=current_image)
        new_image.paste(icon_image,
                        (int(0.98 * current_image.width) - icon_image.width,
                         int(0.98 * current_image.height) - icon_image.height), icon_image)
        test = ImageTk.PhotoImage(new_image)
        image_lab.configure(image=test)
        image_lab.image = test
        IMG_STACK.append(new_image)


def add_watermark(image_lab):
    """
     Add a watermark to the image.
    :param image_lab: tkinter.Label object to place image
    :return: None
    """
    image = IMG_STACK[-1]
    width, height = image.size
    txt = Image.new("RGBA", (width, height), (255, 255, 255, 0))

    text_font = ImageFont.truetype("arial.ttf", 20)
    text_to_add = WATERMARK_TEXT

    edit_image = ImageDraw.Draw(txt)
    size = width * height
    x = 0
    y = 0
    while size > 0:
        edit_image.text((x, y), text_to_add, fill=WATERMARK_COLOR, font=text_font)
        edit_image.text((x, y - 0.5 * height), text_to_add, fill=WATERMARK_COLOR, font=text_font)
        edit_image.text((x, y + 0.5 * height), text_to_add, fill=WATERMARK_COLOR, font=text_font)
        edit_image.text((x, y + 0.9 * height), text_to_add, fill=WATERMARK_COLOR, font=text_font)
        x += width * 0.15
        y += height * 0.15
        size -= 0.1 * width * height

    new_img = Image.alpha_composite(image, txt)

    test = ImageTk.PhotoImage(new_img)
    image_lab.configure(image=test)
    image_lab.image = test
    IMG_STACK.append(new_img)


def watermark_options():
    """
    Open a popup window for watermark options.
    :return: None
    """
    top = Toplevel()
    top.title("Watermark Options")
    top.geometry("300x200")

    icon_image = PhotoImage(file=r"./media/water--pencil.png")
    top.iconphoto(False, icon_image)

    # Entries
    watermark_text_entry = Entry(top)
    watermark_text_entry.insert(0, WATERMARK_TEXT)

    # Color converter
    r, g, b, a = WATERMARK_COLOR
    hex_color = '#%02x%02x%02x' % (r, g, b)

    # Buttons
    color_button = Button(top, bg=hex_color, width=10, command=lambda: pick_color(hex_color, color_button))
    ok_button = Button(top, text="OK",
                       command=lambda: submit_watermark(watermark_text_entry.get(), top, color_button, scale))
    cancel_button = Button(top, text="Cancel", command=top.destroy)

    # Scale
    var = DoubleVar()
    scale = Scale(top, variable=var, orient="horizontal")
    watermark_perc = int(100 * WATERMARK_TRANSPARENCY / 255)
    scale.set(watermark_perc)

    # Label
    watermark_text_label = Label(top, text="Watermark name:")
    color_label = Label(top, text="Watermark color:")
    scale_label = Label(top, text="Watermark transparency: ")

    # Grid layout
    watermark_text_label.grid_configure(column=0, row=0)
    watermark_text_entry.grid_configure(column=1, row=0)
    color_label.grid_configure(column=0, row=1, pady=10)
    color_button.grid_configure(column=1, row=1)
    scale_label.grid_configure(column=0, row=2, pady=10)
    scale.grid_configure(column=1, row=2)
    ok_button.grid_configure(column=0, row=3, pady=20)
    cancel_button.grid_configure(column=1, row=3)


def submit_watermark(watermark_entry: str, top_window, color_button, scale):
    """
    Submit the watermark options.
    :param watermark_entry: str value of watermark title given from watermark options entry
    :param top_window: tkinter.Toplevel object of watermark options window
    :param color_button: tkinter.Button object with watermark color
    :param scale: tkinter.Scale object with watermark transparency value
    :return: None
    """
    global WATERMARK_TEXT, WATERMARK_COLOR, WATERMARK_TRANSPARENCY
    # Watermark text
    WATERMARK_TEXT = watermark_entry.get()

    # Watermark transparency
    transparency = scale.get()
    convert_to_alpha = transparency * 255 / 100
    WATERMARK_TRANSPARENCY = int(convert_to_alpha)

    # Watermark color
    hex_color = color_button.cget("bg")[1:]
    r, g, b = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
    WATERMARK_COLOR = (r, g, b, WATERMARK_TRANSPARENCY)

    top_window.destroy()


def pick_color(color: str, color_button):
    """
    Pick a color for the watermark.
    :param color: str value of initial watermark hex color
    :param color_button: tkinter.Button object of colored button in watermark options window
    :return: None
    """
    chosen_color = colorchooser.askcolor(initialcolor=color, title="Select Color")
    if chosen_color[1]:
        hex_color = chosen_color[1]
        color_button.configure(bg=hex_color)


def save():
    """
     Save the current image with specified options.
    :return: None
    """
    save_pop = Toplevel()
    save_pop.title("Saving Options")
    save_pop.geometry("300x100")

    icon_image = PhotoImage(file=r"./media/disk--pencil.png")
    save_pop.iconphoto(False, icon_image)

    # Labels
    image_format_label = Label(save_pop, text="Select image format: ")
    image_name_label = Label(save_pop, text="Select image name: ")

    # Buttons
    var = StringVar(save_pop, "jpeg")
    jpeg_button = Radiobutton(save_pop, text="JPEG", value="jpeg", variable=var)
    png_button = Radiobutton(save_pop, text="PNG", value="png", variable=var)
    ok_button = Button(save_pop, text="Save",
                       command=lambda: save_ok(save_pop, file_name=image_name_entry.get(), file_format=var.get()))
    cancel_button = Button(save_pop, text="Cancel", command=save_pop.destroy)

    # Entries
    image_name_entry = Entry(save_pop)

    # Grid layout
    image_format_label.grid_configure(column=0, row=0)
    jpeg_button.grid_configure(column=1, row=0)
    png_button.grid_configure(column=2, row=0)
    image_name_label.grid_configure(column=0, row=1)
    image_name_entry.grid_configure(column=1, row=1, columnspan=2)
    ok_button.grid_configure(column=1, row=2, sticky="e", pady=10)
    cancel_button.grid_configure(column=2, row=2)


def save_ok(window, file_name: str, file_format: str):
    """
    Handle the save operation.
    :param window: tkinter.Toplevel object of 'save' window that will be destroyed after saving the parameters
    :param file_name: str value of image file name
    :param file_format: str value of image file format - 'png', 'jpeg'
    :return: None
    """
    directory = filedialog.askdirectory(initialdir=os.getcwd())
    image = IMG_STACK[-1]
    if not file_name:
        file_name = f"new_image_{id(image)}"
    if file_format == "jpeg":
        image = image.convert("RGB")
    image.save(f"{directory}/{file_name}.{file_format}", file_format)
    window.destroy()
