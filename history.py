import xml.etree.ElementTree as ET

# uses xml file as input, in this case 'messages.xml', to the Element Tree parsing function
tree = ET.parse('messages.xml')
root = tree.getroot()
# finds tag where the root is situated, can see root if you use print(root.tag)

class bcolors:
    OKWHITE = '\u001b[37m'
    OKMAGENTA = '\u001b[35m'
    OKGREEN = '\u001b[32m'

# for a child element of the root tag, take the child's attribute and parse through/output certain data fields associated with an address's value.
def msg_history(root):
    for child in root:
        menu = child.attrib
        if menu['address'] == '+17036389773':
            print('{} - Mason: {}\n'.format(bcolors.OKGREEN + menu['readable_date'], bcolors.OKWHITE + menu['body']))
        else:
            print('{} - Olivia: {}\n'.format(bcolors.OKMAGENTA + menu['readable_date'], bcolors.OKWHITE + menu['body']))

msg_history(root)

print("\n \n \033[91m {}\033[00m" .format("!!! Here are your messages (: !!! \n \n \n"))