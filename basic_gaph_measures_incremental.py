import networkx as nx

import matplotlib.pylab as plt
import collections
from networkx.algorithms import approximation as apxa


def basic_measures(g, i):
	# degree frequency plot
	degree_list = sorted(nx.degree_histogram(g), reverse=True)
	n = len(degree_list)
	sum_degree = sum(degree_list)
	plot_title = "Degree Distribution plot" + "_20" + str(i).zfill(2)
	plt.loglog(degree_list, 'b-', marker='o')
	plt.title(plot_title)
	plt.ylabel("Frequency")
	plt.xlabel("Degree")
	plot_name = "Degree Distribution" + "_20" + str(i).zfill(2) + ".png"
	plt.savefig(plot_name)
	plt.close()

	# degree cumulative distribution
	'''probab = []
	for j in range((len(degree_list))):
		probab.append(sum(degree_list[j:])/sum_degree)
	plot_title = "Cumulative Degree Distribution plot" + "_20" + str(i).zfill(2)
	plt.plot(range(len(degree_list)), probab)
	plt.title(plot_title)
	plt.ylabel("P(x>=d)")
	plt.xlabel("Degree (d)")
	plot_name = "Cumulative Degree Distribution" + "_20" + str(i).zfill(2) + ".png"
	plt.savefig(plot_name)
	plt.close()'''

	# distance distribution
	'''p = nx.shortest_path_length(g)
	distancee = []
	for jj in range(g.number_of_nodes()):
		if 
		distancee.append(max(list(p.values())[jj].values()))
	counter = collections.Counter(distancee)
	#counter = collections.OrderedDict(counter)
	distance = list(counter.keys())
	dis_freq = list(counter.values())
	dis_freq = [x for _, x in sorted(zip(distance, dis_freq))]
	distance = sorted(distance)
	sum_dis = sum(dis_freq)
	probab = []
	for j in range((len(dis_freq))):
		probab.append(sum(dis_freq[j:]) / sum_dis)
	plot_title = "Distance Distribution plot" + "_20" + str(i).zfill(2)
	plt.plot(distance, probab)
	plt.title(plot_title)
	plt.ylabel("P(x>=d)")
	plt.xlabel("Distance (d)")
	plot_name = " Distance Distribution" + "_20" + str(i).zfill(2) + ".png"
	plt.savefig(plot_name)
	plt.close()'''
	# degree centrality plot
	'''plot_title = "G=Degree Centrality plot" + "_20" + str(i).zfill(2)
	plt.plot(sorted(list(nx.degree_centrality(g).values())))
	plt.title(plot_title)
	plt.ylabel("Degree Centrality")
	plt.xlabel("rank")
	plot_name = " Degree Centrality" + "_20" + str(i).zfill(2) + ".png"
	plt.savefig(plot_name)
	plt.close()'''

	# nx.draw(g, pos=nx.circular_layout(g), nodecolor='r', edge_color='b')

	# general_info_in_textfile
	'''density = nx.density(g)
	nodes = nx.number_of_nodes(g)
	edges = nx.number_of_edges(g)
	avg_degree = edges / nodes
	Fill = edges / (nodes * nodes)
	# avg_shortest_path=nx.average_shortest_path_length(g)
	# diameter = nx.diameter(g)
	len_max_clique = len(apxa.max_clique(g))
	avg_clustring = apxa.average_clustering(g, trails=1000)
	file_name = "General_info" + "_20" + str(i).zfill(2) + ".txt"
	with open(file_name) as info:
		info.write("density :" + str(density) + "\n")
		info.write("nodes :" + str(nodes) + "\n")
		info.write("avg_degree  :" + str(avg_degree) + "\n")
		info.write("Fill :" + str(Fill) + "\n")
		info.write("len_max_clique :" + str(len_max_clique) + "\n")
		info.write("avg_clustring :" + str(avg_clustring) + "\n")'''



fname = "dblp_coauth_edglis_2000_2014.txt"
g = nx.read_edgelist(fname, delimiter=" ", create_using=nx.Graph(), nodetype=int)
g = nx.create_empty_copy(g)
for i in range(0, 15):
	fname = "dblp_coauth_edglis_20" + str(i).zfill(2) + ".txt"

	with open(fname) as edl:
		for line in edl:
			g.add_edge(int(line.split(" ")[0]), int(line.split(" ")[1]))
	print(nx.number_of_nodes(g))
	print(nx.number_of_edges(g))
	basic_measures(g, i)

