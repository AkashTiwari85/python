from collections import namedtuple
point=namedtuple('point','x,y')
pt=point(1,-4)
print(pt.x,pt.y)


# from collections import orderedDict
# orderedDict={}
# orderedDict['a']=1
# orderedDict['b']=4
# orderedDict['c']=2
# orderedDict['d']=30
# print(orderedDict)

from collections import defaultdict
d=defaultdict(float)
d['a']=1
d['b']=2
print(d['a'])
print(d['b'])
print(d['c'])