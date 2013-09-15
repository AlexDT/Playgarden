class className:
  """docstring for ClassName"""
  def createName(self, name):
    self.name = name
  def displayName(self):
    return self.name
  def saying(self):
    print 'Hello %s' % self.name

class Bird:
  def __init__(self, kind, call):
    self.call = call
    self.kind = kind
  def do_call(self):
    print 'a %s goes %s' % (self.kind, self.call)

class Parrot(Bird):
  def __init__(self):
    Bird.__init__(self, "Parrot", "Kah!")

class Cuckoo(Bird):
  def __init__(self):
    Bird.__init__(self, "Cuckoo", "Cuckoo!")

if __name__ == "__main__":
  parrot = Parrot()
  cuckoo = Cuckoo()

parrot.do_call()
cuckoo.do_call()