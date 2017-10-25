import itertools
import csv

#global cols
#cols = 0

def coauthorship_edgelist(ap, dca):

	#global cols 

	reader = csv.reader(ap, delimiter=',')

	authors = []
	paper = ''
	first_paper = True
	first_row = True

	for row in reader:
		if first_row == True:
			first_row = False
			continue
		if first_paper == True:
			authors.append(int(row[0]))
			paper = row[1]
			first_paper = False
		elif row[1] == paper:
			authors.append(int(row[0]))
		else:
			if len(authors) > 1:
				author_combs = itertools.combinations(authors, 2)
				for a in author_combs:
					#cols += 1
					dca.write("{0} {1}".format(a[0], a[1]))
					dca.write('\n')
			authors = []
			paper = row[1]
			authors.append(int(row[0]))


for i in range(0, 15):
	si = str(i)
	with open("author-20" + si.zfill(2) + "-20" + si.zfill(2) + ".csv") as ap, \
			open("dblp_coauth_edglis_20" + si.zfill(2) + ".txt", 'w') as dca:

		coauthorship_edgelist(ap, dca)

	#print(cols)
