s = '{"name"="hari","age"=25}'
import json
s=s.replace('=',':')
print(json.loads(s))
