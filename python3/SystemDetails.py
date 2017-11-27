import platform
import os
import socket

class SystemDetails:
    def getOs(self):
        #https://stackoverflow.com/questions/110362/how-can-i-find-the-current-os-in-python
        return platform.system() + " " + platform.release()

    def getIpAddress(self):
        return socket.gethostbyname(socket.gethostname())

    def get_hostname(self):
        return socket.gethostname()

# main
if __name__ == "__main__":
    sd = SystemDetails()
    print(sd.getOs())

    print(sd.getIpAddress())

    print(sd.get_hostname())