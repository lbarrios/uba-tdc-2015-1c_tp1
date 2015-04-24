# look at http://standards.ieee.org/develop/regauth/ethertype/eth.txt
protocol_title = {
    '802.3': '802.3',
    '2048': 'IPv4',
    '2054': 'ARP',
    '34525': 'IPv6',
    '34983': 'Huawei_88A7',
    '33079': 'IPX',
    '35020': 'LLDP',
    '34958': 'IEEE 802.1X'
}
def get_protocol_title(s):
  if s in protocol_title:
    return protocol_title[s]
  else:
    return 'unknown_%s'%s

