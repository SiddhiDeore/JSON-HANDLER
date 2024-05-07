class TV:
    def turn_on(self):
        print("Turning on TV")

    def turn_off(self):
        print("Turning off TV")

    def set_volume(self, volume):
        print(f"Setting volume to {volume}")

class Command:
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        raise NotImplementedError

class TurnOnCommand(Command):
    def execute(self):
        self.receiver.turn_on()

class TurnOffCommand(Command):
    def execute(self):
        self.receiver.turn_off()

class SetVolumeCommand(Command):
    def __init__(self, receiver, volume):
        super().__init__(receiver)
        self.volume = volume

    def execute(self):
        self.receiver.set_volume(self.volume)

class RemoteControl:
    def __init__(self):
        self.commands = dict()
        self.on_button = None
        self.off_button = None
        self.set_volume_button = None

    def set_command(self, button, command):
        self.commands[button] = command

    # def set_command(self, button, command):
    #     if button == "on":
    #         self.on_button = command
    #     elif button == "off":
    #         self.off_button = command
    #     elif button == "set_volume":
    #         self.set_volume_button = command

    def press_button(self, button):
        if button in self.commands:
            self.commands[button].execute()
    # def press_button(self, button):
    #     if button in ["on", "off", "set_volume"]:
    #         command = getattr(self, f"{button}_button")
    #         command.execute()
        

# Set up remote and receiver
tv = TV()
remote = RemoteControl()
remote.set_command("on", TurnOnCommand(tv))
remote.set_command("off", TurnOffCommand(tv))
remote.set_command("set_volume", SetVolumeCommand(tv, 20))

# Use the remote
remote.press_button("on")
remote.press_button("set_volume")
remote.press_button("off")
print(remote.commands)


# TV represents the receiver object that performs actions (turning on/off, changing volume).
# Command defines the interface for commands, requiring an execute method.
# Concrete commands (TurnOnCommand, TurnOffCommand, SetVolumeCommand) implement execute to interact with the receiver.
# RemoteControl holds references to different command objects based on buttons.
# When a button is pressed, the remote retrieves the corresponding command and calls its execute method, ultimately triggering actions on the receiver.