import dns.resolver

servers_results=dns.resolver.resolve('google.com','MX')
for i in servers_results:
    print(f"mail server {i.exchange} has preference {i.preference}")
    print("\n")