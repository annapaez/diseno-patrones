from document_handlers import ApprovalHandlerA, ApprovalHandlerB, ApprovalHandlerC

def main():
    handlerA = ApprovalHandlerA()
    handlerB = ApprovalHandlerB()
    handlerC = ApprovalHandlerC()

    handlerA.set_successor(handlerB)
    handlerB.set_successor(handlerC)

    document_list = ["Document1", "Document2", "Document3", "Document4"]

    for doc in document_list:
        print(f"Procesando: {doc}")
        handlerA.process_document(doc)

if __name__ == "__main__":
    main()