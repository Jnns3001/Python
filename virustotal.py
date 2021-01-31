from virustotal_python.virustotal import Virustotal
from pprint import pprint

total = Virustotal("")

resp = total.file_scan("")
pprint(resp)