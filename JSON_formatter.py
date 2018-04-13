import json
import sys

#usage
#python JSON_formatter.py src_file.txt result.json

print sys.argv[1]
print sys.argv[2]

with open(sys.argv[1], "r") as f:
    src_file_contents = f.read()

parsed = json.loads(src_file_contents)
result = json.dumps(parsed, indent=4)

with open(sys.argv[2],"wt") as f:
    f.write(result)

print "done"

