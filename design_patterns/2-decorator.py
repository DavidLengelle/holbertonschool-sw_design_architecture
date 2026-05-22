#!/usr/bin/env python3
"""Decorator pattern: add toppings to a beverage by wrapping it."""


class Coffee:
    """A plain coffee beverage."""

    def cost(self):
        """Return the base price of the coffee."""
        return 50

    def description(self):
        """Return the base description of the coffee."""
        return "Coffee"


class MilkDecorator:
    """Wrap a beverage to add milk."""

    def __init__(self, inner):
        """Store the wrapped beverage."""
        self._inner = inner

    def cost(self):
        """Return the wrapped cost plus the milk price."""
        return self._inner.cost() + 10

    def description(self):
        """Return the wrapped description plus the milk label."""
        return self._inner.description() + " + milk"


class SugarDecorator:
    """Wrap a beverage to add sugar."""

    def __init__(self, inner):
        """Store the wrapped beverage."""
        self._inner = inner

    def cost(self):
        """Return the wrapped cost plus the sugar price."""
        return self._inner.cost() + 5

    def description(self):
        """Return the wrapped description plus the sugar label."""
        return self._inner.description() + " + sugar"


class CaramelDecorator:
    """Wrap a beverage to add caramel."""

    def __init__(self, inner):
        """Store the wrapped beverage."""
        self._inner = inner

    def cost(self):
        """Return the wrapped cost plus the caramel price."""
        return self._inner.cost() + 15

    def description(self):
        """Return the wrapped description plus the caramel label."""
        return self._inner.description() + " + caramel"


def main():
    """Build stacked beverages and print their description and cost."""
    drink1 = MilkDecorator(Coffee())
    print(drink1.description(), drink1.cost())

    drink2 = MilkDecorator(SugarDecorator(Coffee()))
    print(drink2.description(), drink2.cost())

    drink3 = CaramelDecorator(MilkDecorator(SugarDecorator(Coffee())))
    print(drink3.description(), drink3.cost())


if __name__ == "__main__":
    main()
