import csv
from pkg_resources import resource_filename as rscfn

def read(fn):
	fn = rscfn(__name__, fn)
	with open(fn, mode='r') as f:
		d = {}
		for row in csv.reader(f, delimiter='|'):
			d[row[0].replace('.', '')] = row[1].replace('.', '')
		return d