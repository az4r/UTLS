import fitz
from tkinter import *
from tkinter import filedialog

root = Tk()
root.withdraw()

cleaner = ""
input_pdf_path = filedialog.askopenfilename(title="Wybierz plik PDF", filetypes=[("Pliki PDF", "*.pdf")])
output_pdf_path = input_pdf_path[:-4] + "_N" + input_pdf_path[-4:]
if (input_pdf_path == ""):
    exit()
old_text = input("\nPodaj istniejacy tekst lub nacisnij enter: ")

def replace_text_in_pdf(input_pdf_path, output_pdf_path, search_text, replace_text):
    document = fitz.open(input_pdf_path)
    while (search_text != ""):
        new_text = input("\nPodaj nowy tekst: ")
        for page_num in range(document.page_count):
            page = document.load_page(page_num)
            text_instances = page.search_for(search_text)
            #print(page.get_fonts(full=False))
            for inst in text_instances:
                bbox = fitz.Rect(inst)
                font_size = page.get_text("dict", clip=bbox)["blocks"][0]["lines"][0]["spans"][0]["size"]
                font_name = page.get_text("dict", clip=bbox)["blocks"][0]["lines"][0]["spans"][0]["font"]
                #print(f"Rozmiar czcionki: {font_size}")
                #print(f"Nazwa czcionki: {font_name}")
                page.add_redact_annot(inst, cleaner, fontname="helv", fontsize=font_size)
                x1, y1, xx1, yy1 = inst
                page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)
                
                if font_name == "ArialRegular":
                    y1 = y1-1
                    font_name_textbox = "FX0"
                if font_name == "ConsolasRegular":
                    font_name_textbox = "FX1"
                if font_name == "ConsolasBold":
                    font_name_textbox = "FX2"
                page.insert_font(fontname="FX0", fontfile="C:/Windows/Fonts/arial.ttf")
                page.insert_font(fontname="FX1", fontfile="C:/Windows/Fonts/consola.ttf")
                page.insert_font(fontname="FX2", fontfile="C:/Windows/Fonts/consolab.ttf")
                
                rect = fitz.Rect(x1, y1, page.mediabox.width, page.mediabox.height)
                page.insert_textbox(rect, new_text, fontname=font_name_textbox, fontsize=font_size)
        search_text = input("\nPodaj istniejacy tekst lub nacisnij enter: ")
    document.save(output_pdf_path, garbage=3, deflate=True)

replace_text_in_pdf(input_pdf_path, output_pdf_path, old_text, cleaner)