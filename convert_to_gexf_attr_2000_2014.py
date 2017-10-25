import networkx as nx

for i in range(14, -1, -1):

	g = nx.Graph()
	si = str(i)
	fname = "dblp_coauth_edglis_20" + si.zfill(2) + ".txt"

	g = nx.read_edgelist(fname)

	year = int("20" + si.zfill(2))

	nx.set_edge_attributes(g, 'year', year)

	fname = "dblp_coauth_edglis_with_attr_20" + si.zfill(2) + ".gexf"
	nx.write_gexf(g, fname)
	