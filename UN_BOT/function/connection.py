import socket



class connection:

  def __init__(self):
    self.server = "www.google.com"

  def is_connected(self):
    try:
      # see if we can resolve the host name -- tells us if there is
      # a DNS listening
      host = socket.gethostbyname(self.server)
      # connect to the host -- tells us if the host is actually
      # reachable
      s = socket.create_connection((host, 80), 2)
      return True
    except:
       pass
    return False
