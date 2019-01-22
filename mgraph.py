import qiime2
q2methods = qiime2.sdk.util.actions_by_input_type('FeatureTable[Frequency]')


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


##############testing#################


class Node:
    '''
    description: Node class used to hold input, output, and parameter
        information for each defined method.
    input:
        method - method signature
        inputs - OrderedDict of method inputs
        outputs - OrderedDict of method outputs
        params - OrderedDict of method parameters
    '''
    def __init__(self,method, inputs, outputs, params):
        self.method = method
        self.inputs = inputs
        self.outputs = outputs
        self.params = params


    def __str__(self):
        '''
            description: to string method for each node
        '''
        return 'Method: '+str(self.method)+',\n\n Inputs: '+str(self.inputs)+',\n\n Outputs: '+str(self.outputs)+',\n\n Params: '+str(self.params)


#create an adjacency list of input types -> methods
graph = {}
edges = {}

def buildGraph():
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

buildGraph()
print(graph)
for l in graph.values():
    for node in l:
        print(str(node))

for k in graph.keys():
    print(k)

def getNextParam(method):
    '''
        description: given an input method, return a tuple of parameter types
        input: method object
        output: tuple of parameter types
    '''
    key = []
    for i in range(len(method.signature.inputs)):
      key.append(list(method.signature.inputs.items())[i][1].qiime_type)
    key = tuple(key)
    return key

def randomPath():
    '''
        description: generate a random path
        *currently just printing through stdout
    '''
    #get first key
    count = 0
    print()
    print("Generating Random Path:")
    key = list(graph.keys())[0]
    while((key in graph)):
        print(key)
        method = graph[key][0].method
        print(method)
        print()
        newKey = []
        key = getNextParam(graph[key][0].method)
        print("New key: "+str(key))
        print(key in graph)
        count += 1
        if (count > 10):
            break


randomPath()



#Questions
'''
1. should i be inputting all types and where can I get that or would i need to call on the get_action funciton for all types
2. what should the key be?
3. frozen-set for tuple key pairing?
4. Not sure if my current code contains flags for each node, but it is holding onto the input parameters
5. I have tested the random testing path and that seems to work (as in each node does point back to itself)

'''


PCoAResults
(really simple plot)

FeatureTable - midsize

1. create graph based off of passed into method - 
- given a semantic type -


create unit tests

create method nodes, semantic type notes, parameter nodes

semantic1 -> method -> semantic1, semantic2, semantic3 
                \
                parameter 

glyphs - optimize later 
alternatives to dictionary (numpy)


graph - visualition possibility