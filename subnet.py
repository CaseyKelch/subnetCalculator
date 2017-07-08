#!/usr/bin/python3
"""
Subnet Calculator
"""


def subnet_calculator(ip, mask):

    ip_split = ip.split(".")
    mask_split = mask.split(".")
    network = []
    broadcast = []
    first = []
    last = []
    for i, m in zip(ip_split, mask_split):
        network.append(str(int(i) & int(m)))
        first.append(str(int(i) & int(m)))
        broadcast.append(str(int(i) | (255-int(m))))
        last.append(str(int(i) | (255 - int(m))))

    first[3] = str(int(first[3]) + 1)
    last[3] = str(int(last[3]) - 1)

    return "Network Address: " + ".".join(network) + "\nBroadcast Address: " + ".".join(broadcast) + \
           "\nFirst Host: " + ".".join(first) + "\nLast Host: " + ".".join(last)


if __name__ == "__main__":
    separator = "*" * 60
    print(separator)
    print("IP SUBNET CALCULATOR")
    print(separator)
    ip_addr = input("\nIP Address: ")
    sub_mask = input("Subnet Mask: ")
    while ip_addr != "" or sub_mask != "":
        print("{3}\nNetwork Info for {0} {1}...\n{3}\n{2}\n{3}\n"
              .format(ip_addr, sub_mask, subnet_calculator(ip_addr, sub_mask), separator))
        ip_addr = input("IP Address: ")
        sub_mask = input("Subnet Mask: ")
    print("\nGoodbye!\n")

