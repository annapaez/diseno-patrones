from concrete_builder import ConcreteBuilder
from builder_coordinator import Builder_coordinator

if __name__ == "__main__":
    builder = ConcreteBuilder()
    director = Builder_coordinator(builder)

    director.construct()
    product = builder.get_product()

    print(product)