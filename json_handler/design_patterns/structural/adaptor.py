# Define incompatible interfaces
class USPlug:
    def use_with_us_outlet(self):
        print("Using device with US plug in US outlet")

class EuroPlug:
    def use_with_euro_outlet(self):
        print("Using device with Euro plug in Euro outlet")

# Define the Adapter
class EuroPlugToUSAdapter:
    def __init__(self, euro_device):
        self.euro_device = euro_device

    def use_with_us_outlet(self):
        # Adapt Euro plug to US outlet compatibility
        print("Using Euro plug adapter with US outlet")
        self.euro_device.use_with_euro_outlet()

# Usage example
euro_device = EuroPlug()
adapter = EuroPlugToUSAdapter(euro_device)
adapter.use_with_us_outlet()  # Output: Using Euro plug adapter with US outlet, Using device with Euro plug in Euro outlet


# The Adapter pattern acts as a bridge between two incompatible interfaces, allowing them to work together seamlessly.
# USPlug and EuroPlug represent incompatible interfaces with dedicated methods.
# EuroPlugToUSAdapter bridges the gap by implementing the USPlug method.
# It internally uses the adapted euro_device's use_with_euro_outlet method.
# Client code interacts solely with the adapter's use_with_us_outlet method, unaware of the internal adaptation.