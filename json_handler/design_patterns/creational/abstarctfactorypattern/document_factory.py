from abc import ABC,abstractclassmethod

class documentfactory(ABC):
    @abstractclassmethod
    def create_document(self):
        self
    
    def create_paragraph(self):
        self
    
    def create_image(self):
        self