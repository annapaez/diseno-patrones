from abstract_factory import AbstractFactory
from concrete_products import ProductoA1, ProductoB1, ProductoA2, ProductoB2

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ProductoA1()

    def create_product_b(self):
        return ProductoB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ProductoA2()

    def create_product_b(self):
        return ProductoB2()