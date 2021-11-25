#5
def handshake(self):
    version = VersionMessage()
    self.send(version)
    self.wait_for(VerAckMessage)
