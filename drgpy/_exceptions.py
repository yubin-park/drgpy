import csv
import re
import json
from pkg_resources import resource_filename as rscfn

def read_mdc08(fn="data/_mdc08.json"):
    fn = rscfn(__name__, fn)
    return json.load(open(fn, "r"))




