import xml.etree.ElementTree as ET
data='''<person>
<name> saurav sagar</name>
<roll>1906057</roll>
<phone type=" intl">
7636157652
</phone>
<email hide=" yes"/>
</person>'''
tree=ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
print('roll:', tree.find('roll').text)
