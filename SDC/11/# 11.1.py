# 11.1
adict={"abc":7,"def":11,"ghi":13,"jkl":17,"mno":19}
print(adict["def"])
keys=list(adict.keys())
print(adict.keys())
for key,value in (adict.items()):
    print(f'{key}:{adict[key]}')
if("pqr" in adict.keys()==True):
    print("contains")
else:
    print("not contains")
adict['abc']=23
print(adict.values())