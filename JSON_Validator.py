import simplejson
import json
import sys

#usage
#python JSON_formatter.py src_file.txt result.json

print "Validating file:{}".format(sys.argv[1])

with open(sys.argv[1], "r") as f:
    src_file_contents = f.read()

try:
    simplejson.loads(src_file_contents)
    print "JSON Valid"
except Exception as e:
    print "Invalid JSON: {}".format(e.message)

