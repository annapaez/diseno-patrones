class ApprovalHandler:
    def __init__(self, successor=None):
        self._successor = successor

    def set_successor(self, successor):
        self._successor = successor

    def process_document(self, document):
        if self._successor:
            self._successor.process_document(document)

class ApprovalHandlerA(ApprovalHandler):
    def process_document(self, document):
        if document == "Document1":
            print("Documento 1 ha sido aprobado por el Manejador de Aprobación A")
        else:
            super().process_document(document)

class ApprovalHandlerB(ApprovalHandler):
    def process_document(self, document):
        if document == "Document2":
            print("Documento 2 ha sido aprobado por el Manejador de Aprobación B")
        else:
            super().process_document(document)

class ApprovalHandlerC(ApprovalHandler):
    def process_document(self, document):
        if document == "Document3":
            print("Documento 3 ha sido aprobado por el Manejador de Aprobación C")
        else:
            print("El documento no pudo ser aprobado")