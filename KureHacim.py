import math
yaricap = float (input("Kürenin yarıçap uzunluğunu giriniz: "))
hacim = 4/3*math.pi*yaricap*yaricap*yaricap
hacim = round(hacim,4)
print("Yarıçapı {} kürenin hacmi = {}".format(yaricap,hacim))
