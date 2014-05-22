# -*- coding: utf-8 -*-
_author__ = 'HuCC'

import xml.dom.minidom
import xml.etree.ElementInclude


input_xml_string='''
<root>
    <item>
        <data version="1.0" url="http://***"/>
        <data version="2.0" url="http://***"/>
    </item>
    <other>
        <data version="1.0" url="http://***"/>
        <data version="2.0" url="http://***"/>
    </other>
</root>
'''

doc = xml.dom.minidom.parseString(input_xml_string)
for node in doc.getElementsByTagName("data"):
    if node.parentNode.tagName == "other":
        print (node, node.tagName, node.getAttribute("version"))

doc = xml.etree.ElementTree.parse('./test.xml')
for node in doc.findall("//item/data"):
        print (node, node.tag, (node.items()))





