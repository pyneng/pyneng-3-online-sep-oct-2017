import sys
import textfsm
from tabulate import tabulate
from pprint import pprint

template = sys.argv[1]
output_file = sys.argv[2]

with open(template) as f, open(output_file) as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    pprint([header]+result)
    print(tabulate(result, headers=header))
