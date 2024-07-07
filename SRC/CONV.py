import fitz  # PyMuPDF

cleaner = ""
#myfont = "C:/Windows/Fonts/arial.ttf"
starytekst = input("\nPodaj stary tekst: ")
nowytekst = input("\nPodaj nowy tekst: ")

def replace_text_in_pdf(input_pdf_path, output_pdf_path, search_text, replace_text):
    # Otwórz istniejący plik PDF
    document = fitz.open(input_pdf_path)

    # Przejdź przez wszystkie strony
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text_instances = page.search_for(search_text)
        #print(page.get_fonts(full=False))
        
        # Zamień każdą znalezioną instancję
        for inst in text_instances:
            bbox = fitz.Rect(inst)
            font_size = page.get_text("dict", clip=bbox)["blocks"][0]["lines"][0]["spans"][0]["size"]
            font_name = page.get_text("dict", clip=bbox)["blocks"][0]["lines"][0]["spans"][0]["font"]
            print(f"Rozmiar czcionki: {font_size}")
            print(f"Rozmiar czcionki: {font_name}")
            page.add_redact_annot(inst, cleaner, fontname="helv", fontsize=font_size)
            x1, y1, xx1, yy1 = inst
            if font_name == "ArialRegular":
                myfont = "C:/Windows/Fonts/arial.ttf"
                y1 = y1-1
            if font_name == "ConsolasRegular":
                myfont = "C:/Windows/Fonts/consola.ttf"
            if font_name == "ConsolasBold":
                myfont = "C:/Windows/Fonts/consolab.ttf"
            page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)  # Nie zmieniaj obrazów
            page.insert_font(fontname="F0", fontfile=myfont)
            rect = fitz.Rect(x1, y1, 300, 200)  # Prostokąt
            page.insert_textbox(rect, nowytekst, fontname="F0", fontsize=font_size)
    # Zapisz zmieniony plik PDF
    document.save(output_pdf_path, garbage=3, deflate=True)

# Ścieżki do plików PDF
input_pdf_path = 'C:/CONV/OLD.pdf'
output_pdf_path = 'C:/CONV/NEW.pdf'

# Zamiana tekstu
replace_text_in_pdf(input_pdf_path, output_pdf_path, starytekst, cleaner)