class Command:
    def execute(self):
        pass

class StartServerCommand(Command):
    def __init__(self, server):
        self.server = server

    def execute(self):
        self.server.start()

class StopServerCommand(Command):
    def __init__(self, server):
        self.server = server

    def execute(self):
        self.server.stop()

class RestartServerCommand(Command):
    def __init__(self, server):
        self.server = server

    def execute(self):
        self.server.restart()
