import qiime2
q2methods = qiime2.sdk.util.actions_by_input_type('FeatureTable[Frequency]')


#testing

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


#method to get all input and output types from all methods, pipelines, visualizers
#return list of methods
class Node:
    def __init__(self,method, inputs, outputs, params):
        self.method = method
        self.inputs = inputs
        self.outputs = outputs
        self.params = params


    def __str__(self):
        return 'Method: '+str(self.method)+',\n\n Inputs: '+str(self.inputs)+',\n\n Outputs: '+str(self.outputs)+',\n\n Params: '+str(self.params)


#create an adjacency list of input types -> methods

graph = {}
edges = {}

#have to change methods to tuples starting with method, then int
#dictionary of method and node.
def buildgraph():
    for plugin in q2methods:
        method_list = plugin[1]
        for method in method_list:
            #inputs = []
            #for input_type in method.signature.inputs:
            #    inputs.append(input_type)
            #inputs = tuple(sorted(inputs))
            inputs = method.signature.inputs

            #outputs = []
            #for output_type in method.signature.outputs:
            #    outputs.append(output_type)
            #outputs = tuple(sorted(outputs))
            outputs = method.signature.outputs

            params = method.signature.parameters

            key = []
            for i in range(len(method.signature.inputs)):
                key.append(list(method.signature.inputs.items())[i][1].qiime_type)
            key = tuple(key)
            node = Node(method, inputs, outputs, params)
            if key not in graph:
                graph[key] = [node]
            else:
                graph[key].append(node)

buildgraph()
print(graph)
for l in graph.values():
    for node in l:
        print(str(node))

for k in graph.keys():
    print(k)
(qiime2-2018.11) qiime2@ip-172-31-38-69:~$ cat tgraph.py
import qiime2
q2methods = qiime2.sdk.util.actions_by_input_type('FeatureTable[Frequency]')


#testing
for method in q2methods:
    print(method)
    print()
    pass

first_elem = q2methods[0]
first_method = first_elem[1][0]

print()
print(first_method)
print()
print(first_method.signature.inputs)
print(first_method.signature.outputs)

print(str(first_method)[1:7])
print()

for method in q2methods[0][1]:
    #isolate lists
    #print(method)
    #print(method.signature.inputs)
    #print(method.signature.outputs)
    #print()
    pass


input_type = next(iter(first_method.signature.inputs))
print(input_type)

output_type = next(iter(first_method.signature.outputs))
print(output_type)




#method to get all input and output types from all methods, pipelines, visualizers
#return list of methods
class Node:
    def __init__(self,initType):
        self.type = initType
        self.methods = []

    def getType(self):
        return self.type

    def addMethod(self, method):
        self.methods.append(method)

    def getMethods(self):
        return self.methods

    def setType(self, otherType):
        self.type = otherType

    def removeMethod(self, method):
        if method in self.methods:
            self.methods.remove(method)
    def __str__(self):
        return 'Type: '+str(self.type)+', Methods: '+str(self.methods)

graph = {}
edges = {}

#have to change methods to tuples starting with method, then int
#dictionary of method and node.
def buildgraph():
    input_types = []
    output_types = []

    for plugin in q2methods:
        method_list = plugin[1]
        for method in method_list:
            for input_type in method.signature.inputs:
                if input_type not in graph:
                    node = Node(input_type)
                    node.addMethod(method)
                    graph[input_type] = node
                    input_types.append(input_type)
                else:
                     graph[input_type].addMethod(method)
            for output_type in method.signature.outputs:
                if output_type not in graph:
                    node = Node(output_type)
                    node.addMethod(method)
                    graph[input_type] = node
                    output_types.append(output_type)
                else:
                    graph[output_type].addMethod(method)

    #print(input_types)
    #print(output_types)
    print('graph: ')
    print(graph)
    for v in graph.values():
        print(v)

    print()
#    print('edges:')
#    for v in edges.values():
#        print(v)
#    return graph


buildgraph()
