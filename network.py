import qiime2
import random
from itertools import combinations
import networkx as nx
import matplotlib.pyplot as plt


#q2methods = qiime2.sdk.util.actions_by_input_type('PCoAResults')
q2methods = qiime2.sdk.util.actions_by_input_type('FeatureTable[Frequency]')

#############testing##################
q2p = qiime2.sdk.PluginManager()

#for plugin, value in q2p.plugins.items():
#    print(value.methods.keys())
##############testing#################

G=nx.DiGraph()

def getNextParam(method, b):
    '''
        description: given an input method, return a tuple of parameter types
        input: method object
        output: tuple of parameter types
    '''
    req = []
    non_req = []
    if b:
        for k,v in method.signature.inputs.items():
            if not v.has_default():
                req.append(v.qiime_type)
            else:
                non_req.append(v.qiime_type)
    else:
        for k,v in method.signature.outputs.items():
            if not v.has_default():
                req.append(v.qiime_type)
            else:
                non_req.append(v.qiime_type)
    #print("req: "+str(req))
    #print("non_req: "+str(non_req))
    return req, non_req

def getCombinations(no_req):
    if not no_req:
        return no_req
    no_req_comb = []
    for i in range(len(no_req)+1):
        combs = combinations(no_req, i)
        for c in combs:
            no_req_comb.append(list(c))
    return no_req_comb

c_map = [] #color map

def buildGraph():
    for plugin in q2methods:
        method_list = plugin[1]
        for method in method_list:
            if not G.has_node(method):
                G.add_node(method,value=method, color='red')
            req_in, non_req_in = getNextParam(method,1)
            if non_req_in:
                print("COMBINATIONS: ")
                print(getCombinations(non_req_in))
            for key in req_in:
                if not G.has_node(key):
                    G.add_node(key, value=key, color='blue')
                G.add_edge(key, method)
            for key in req_in:
                if not G.has_node(key):
                    G.add_node(key, value=key, color='blue')
                G.add_edge(key, method)

            req_out, non_req_out = getNextParam(method,0)
            for key in req_out:
                if not G.has_node(key):
                    G.add_node(key, value=key, color='blue')
                G.add_edge(method, key)
            for key in non_req_out:
                if not G.has_node(key):
                    G.add_node(key, value=key, color='blue')
                G.add_edge(method, key)

buildGraph()
c_map = [n[1]['color'] for n in list(G.nodes(data=True))]
print(c_map)
print()
nx.draw(G, node_color=c_map, with_labels=True)
plt.draw()
plt.show()



