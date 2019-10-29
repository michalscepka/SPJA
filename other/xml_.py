import xml.etree.ElementTree as ET

root = ET.parse('menza.xml') #ElementTree instance

datums = root.findall('datum') #list of Elements

for datum in datums:
    print(datum.attrib['den'])
    jidla = datum.getiterator('jidlo')
    for jidlo in jidla:
        print('\t' + jidlo.attrib['nazev'])
        for ingredience in jidlo.getiterator('ingredience'):
            print('\t\t' + ingredience.attrib['nazev'])


def xml2py(node):
    name = node.tag

    pytype = type(name, (object, ), {})
    pyobj = pytype()

    for attr in node.attrib.keys():
        setattr(pyobj, attr, node.get(attr))

    if node.text and node.text != '' and node.text != ' ' \
                 and node.text != '\n':
        setattr(pyobj, 'text', node.text)

    for cn in node:
        if not hasattr(pyobj, cn.tag):
            setattr(pyobj, cn.tag, [])
        getattr(pyobj, cn.tag).append(xml2py(cn))

    return pyobj

xml_string = ''
with open('menza.xml', 'rt') as f:
    xml_string = f.read()

menza_xml_tree = ET.fromstring(xml_string)

obj = xml2py(menza_xml_tree)

for datum in obj.datum:
    print(datum.den)
    for jidlo in datum.jidlo:
        print('\t' + jidlo.nazev)
        for ingredience in jidlo.ingredience:
            print('\t\t' + ingredience.nazev)
