from document_factory import documentfactory

class Worddocumentfactory(documentfactory):
    def create_document(self):
        return Worddocument()
    
    def create_paragraph(self):
        return Wordparagraph()

    def create_image(self):
        return Wordimage()
    
class Worddocument():
    def render(self):
        print("Rendering word document")

class Wordparagraph():
    def add_text(self,text):
        print(f"Adding paragrpah to word document : {text}")

class Wordimage():
    def insert_image(self,image_path):
        print(f"Adding image to word document : {image_path}")

