from abstract_products import AbstractProductA, AbstractProductB

class ProductoA1(AbstractProductA):
    def operation_a(self):
        return "Operación A1 en ProductoA1"

class ProductoA2(AbstractProductA):
    def operation_a(self):
        return "Operación A2 en ProductoA2"

class ProductoB1(AbstractProductB):
    def operation_b(self):
        return "Operación B1 en ProductoB1"

class ProductoB2(AbstractProductB):
    def operation_b(self):
        return "Operación B2 en ProductoB2"
    
    