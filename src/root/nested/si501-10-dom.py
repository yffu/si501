'''
Created on Oct 19, 2013

@author: Yuan-Fang
'''
#object and properties of all html documents.

# and the methods to access the html documents.

# get, change, add or delete xml elements

# at the end of the trees are the elements nodes, but further beneath are the text nodes that hold the text.

# xml dom contains methods to traverse xml trees, access, insert, and delete nodes.

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement

'''
the element type is a container object, designed to store hierarchical data. element is a cross between a python list and and python dictionary.

ElementTree is a wrapper that loads xml files as trees of Element objects, and saves them back again: analogy is the json loads and dumps

this is all data structures: can try to do some of the java review, plus some of the data structure algorithms.

'''

# data structures review!

root=ET.Element('html')

head=ET.SubElement(root, 'head')

title=ET.SubElement(head, 'title')

title.text='page title'

body=ET.SubElement(root, 'body')

body.set('bgcolor', '#ffffff')

body.text='Hello, world!'

tree=ET.ElementTree(root)

# tree.write('page.xhtml')

# now parse the tree back out

tree=ET.parse('page.xhtml')
 
print tree.findtext('head/title')
 
# root=tree.getroot()

# tree.write('out.xml')

'''
an element has a number of properties associated with it (variables and methods)

a tag: a string of the element type

a number of attributes: stored in a python dictionary

text string to hold text content, tail string to hold trailing text

a number of child elements, stored in a python list
'''
root.append(Element("one"))
root.append(Element("two"))
root.append(Element("three"))

# for node in root:
#     print node

for node in root[1:3]:
    print node
    
# append, insert, and remove are also supported
    
# any element without subelements tests as false, even if it has attributes or text. In these cases a method or function will return None instead of the object

# the element strucuture has no parent pointer. you can try to stay at the parent level instead of going to the child

# each element can have one or more attributes, such as in xml. 

# use the getiterator function for the tree to access all the children of the root node. 

elem=Element('tag')
elem.attrib['first']='1'
elem.attrib['second']='2'
