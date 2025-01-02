class real_madrid:
    barcalona="nemar"
    
    def __init__(self,passing,dribbling,pace,shooting,phycical,defending):
      self.passing=passing
      self.dribbling=dribbling
      self.pace=pace
      self.shooting=shooting
      self.phycical=phycical
      self.defending=defending

fc=real_madrid(99,100,101,98,98,104)
print(fc.passing,)
print(fc.dribbling)
print(fc.pace)
print(fc.shooting)
print(fc.phycical)
print(fc.defending)

class student:
    stream="psg"

    def __init__(self,roll):
      self.roll=roll
    def set_adress(self,adress):
      self.adress=adress
    def get_adress(self):
      return self.adress

ea=student(25)
ea.set_adress("ks garden vadavalli")
print(ea.get_adress())