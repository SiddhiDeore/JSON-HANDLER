from document_factory import documentfactory

class PDFdocumentfactory(documentfactory):
    def create_document(self):
        return PDFdocument()
    
    def create_paragraph(self):
        return PDFparagraph()

    def create_image(self):
        return PDFimage()
    
class PDFdocument():
    def render(self):
        print("Rendering pdf document")

class PDFparagraph():
    def add_text(self,text):
        print(f"Adding paragrpah to pdf document : {text}")

class PDFimage():
    def insert_image(self,image_path):
        print(f"Adding image to pdf document : {image_path}")

