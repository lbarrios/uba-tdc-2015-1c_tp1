protocol_title = {
    '2048': 'IPv4',
    '34525': 'IPv6',
    '2054': 'ARP'
}
def get_protocol_title(s):
  if s in protocol_title:
    return protocol_title[s]
  else:
    return 'unknown_%s'%s

