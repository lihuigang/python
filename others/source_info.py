import json

def json_test():
  d = {'first': 'One', 'second': 2}
  json.dump(d, open('file/result.txt','w'))
def json_load():
  d = json.load(open('file/result.txt', 'r'))
  print (d)
json_test()
json_load()


source_info=json.load(open('file/source_info.json','r'))
print (source_info)

for key in source_info['PVList'][0]:
    print  (key,source_info['PVList'][0][key])
