#!/usr/bin/env python3
"""Factory pattern: create vehicles from a registry of kinds."""


class Bus:
    """A bus that travels on the road."""

    def mode(self):
        """Return the travel mode of this vehicle."""
        return "road"


class Train:
    """A train that travels on rails."""

    def mode(self):
        """Return the travel mode of this vehicle."""
        return "rails"


class Bike:
    """A bike that travels on a lane."""

    def mode(self):
        """Return the travel mode of this vehicle."""
        return "lane"


class Scooter:
    """A scooter that travels on a scooter lane."""

    def mode(self):
        """Return the travel mode of this vehicle."""
        return "scooter_lane"


class VehicleFactory:
    """Create vehicles by name using a registry of classes."""

    def __init__(self):
        """Initialize the factory with an empty registry."""
        self._registry = {}

    def register_kind(self, name, cls):
        """Map a name to a vehicle class in the registry."""
        self._registry[name] = cls

    def create(self, kind):
        """Build and return a vehicle for the given name."""
        cls = self._registry[kind]
        return cls()


def main():
    """Register vehicle kinds and print each travel mode."""
    factory = VehicleFactory()
    factory.register_kind("bus", Bus)
    factory.register_kind("train", Train)
    factory.register_kind("bike", Bike)
    factory.register_kind("scooter", Scooter)

    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
