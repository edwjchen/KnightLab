import qiime2
import random
import networkx as nx
import matplotlib.pyplot as plt
q2methods = qiime2.sdk.util.actions_by_input_type('PCoAResults')



#############testing##################

first_elem = q2methods[0]
first_method = first_elem[1][0]

print()
print("params: "+str(first_method.signature.parameters))
print("input: "+str(first_method.signature.inputs))
print("output: "+str(first_method.signature.outputs))
print()
print(list(first_method.signature.inputs.items())[0][1].qiime_type)


#input_type = next(iter(first_method.signature.inputs))
#print(input_type)

#output_type = next(iter(first_method.signature.outputs))
#print(output_type)

print()
for method in first_method.signature.inputs:
    print(method)
    print()

for k,v in first_method.signature.inputs.items():
    print("printing:")
    print(k)
    print(v)
    print(v.qiime_type)
    print(v.default)
    if not v.default:
        print("v is false")
    else:
        print("hehe xd")

#q2p = qiime2.sdk.PluginManager
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
            param_req = v.default
            if not param_req:
                req.append(v.qiime_type)
            else:
                non_req.append(v.qiime_type)
    else:
        for k,v in method.signature.outputs.items():
            param_req = v.default
            if not param_req:
                req.append(v.qiime_type)
            else:
                non_req.append(v.qiime_type)
    return req, non_req

c_map = []
def buildGraph():
    for plugin in q2methods:
        method_list = plugin[1]
        for method in method_list:
            if not G.has_node(method):
                G.add_node(method,value=method, color='red')
            req_in, non_req_in = getNextParam(method,1)
            print(req_in)
            print(non_req_in)
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
                G.add_edge(key, method)

buildGraph()
c_map = [n[1]['color'] for n in list(G.nodes(data=True))]
print(c_map)
print()
nx.draw(G, node_color=c_map, with_labels=True)
plt.draw()
plt.show()
plt.savefig('graph.png')


