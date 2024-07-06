import fitz  # PyMuPDF

cleaner = ""
myfont = "C:/Windows/Fonts/arial.ttf"
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
            page.add_redact_annot(inst, cleaner, fontname="helv", fontsize=8.5)
            x1, y1, xx1, yy1 = inst
            page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)  # Nie zmieniaj obrazów
            page.insert_font(fontname="F0", fontfile=myfont)
            rect = fitz.Rect(x1, y1-1, 300, 200)  # Prostokąt
            page.insert_textbox(rect, nowytekst, fontname="F0", fontsize=8.519999504089355)
    # Zapisz zmieniony plik PDF
    document.save(output_pdf_path, garbage=3, deflate=True)

# Ścieżki do plików PDF
input_pdf_path = 'C:/CONV/OLD.pdf'
output_pdf_path = 'C:/CONV/NEW.pdf'

# Zamiana tekstu
replace_text_in_pdf(input_pdf_path, output_pdf_path, starytekst, cleaner)