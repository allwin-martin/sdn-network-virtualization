"""Static topology check; does not execute Mininet."""
HOSTS = {"h1":"s1", "h2":"s1", "h3":"s2", "h4":"s2"}
LINKS = {("s1", "s2")}

def validate(hosts=HOSTS, links=LINKS):
    return len(hosts) == 4 and set(hosts.values()) == {"s1", "s2"} and ("s1", "s2") in links

if __name__ == "__main__":
    assert validate()
    print("Logical topology valid. Live Mininet test still required.")
