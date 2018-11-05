import dns.resolver

def resolve_ip(name):
    answers = dns.resolver.query(name, 'A')
    print answers.response

file = open("sitelist", "r")

for line in file.readlines():
    resolve_ip(line.strip())
