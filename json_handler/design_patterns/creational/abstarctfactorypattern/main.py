from pdf_doc_factroy import PDFdocumentfactory
from word_doc_factory import Worddocumentfactory

def process_doc(factory):
    document = factory.create_document()
    paragraph = factory.create_paragraph()
    image =factory.create_image()

    document.render()
    paragraph.add_text("abstarct factory method")
    image.insert_image("image.png")


if __name__ =="__main__":
    pdf_factory= PDFdocumentfactory()
    process_doc(pdf_factory)
    word_factory = Worddocumentfactory()
    process_doc(word_factory)