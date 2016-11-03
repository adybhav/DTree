import sys 
import csv
from Node import  Node

global data_file, n_record, n_attr, input_data, visited

# Function used for input data configuration
def config(args = "golf_processed.csv"):
    print(args)
    global data_file, n_record, n_attr, input_data, visited
    data_file = args
    input_data = []
    m_data = 0
    n_data = 0
    with open(data_file, 'r') as f:
        f = csv.reader(f, delimiter = ',')
        for line in f:
            m_data += 1
            vec = [int(i) for i in line]
            input_data.append(vec)
            n_data = len(vec)

    n_record = m_data
    n_attr = n_data - 1
    visited = [0] * n_attr


# Main function
def execute():
    root = Node()
    build_tree(input_data,root)
    traverse_tree(root, 0)

# Function to build Tree
    # @param data   Data of passed in Node including Attribute data and label data
    # @param parent passed in Node
def build_tree(data, parent):
        # **-------------------Fill in here------------------------**/        
        # Note: You should break down data to matrix of attribute and array of records corresponding label 

        # Check if all records belong to one label -> add leaf node
        # To add a node by: 
        # - Update parent's children list (parent.addChild())
        # - Update children node's parent (child.setParent(parent))

        # Find attribute not visited with minimum gini index using findGini

        # If not found any attribute -> all attribute are visited -> find majority label and add leaf node
        # Else
        # - Creat new Node with found attribute
        # - Add new Node to parent
        # - Mark visited[min Gini attribute] = 1
        
        # Continue to build tree by building node for each value of new created node

# Find gini index of given attribute data and corresponding Labels
    # @param  att Attribute data
    # @param  lab Label data
    # @return gini index of an attribute
def find_gini(att, lab):
        # **-------------------Fill in here------------------------**/      
        # These steps might help you:
        #  - Find number of different values in attribute, number of different labels
        #  - For each value i, find number of occurrences and number of corresponding labels to calculate ginisplit
        #  - gini = sum of all ginisplit


# Use DFS to traverse tree and print nicely with appropriate indent
    # @param node traversing Node
    # @param indent appropriate indent for each level
def traverse_tree(node, indent):
    # Print out current node with appropriate indent
    for i in range(indent):
        print('\t', end="")
    if (node.get_parent() is None):
        print("root")
    else:
        print("-/", node.get_data())

    # Recursive call all the children nodes
    children = []
    children = node.get_children()
    for i in range(node.get_n_child()):
        traverse_tree(children[i], indent + 1)

def main():
    arg = sys.argv[1:]
    if len(arg) > 0:
        config(arg)
    else:
        config()
    execute()

main()


