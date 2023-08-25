import argparse
import uuid

def generate_uuids(version, count=10, name=None):
    # Preface based on UUID version
    prefaces = {
        1: ("UUIDv1 (Time-based UUID): "
            "Generated based on the timestamp, clock sequence, and the MAC address of the computer."),
        3: ("UUIDv3 (Name-based UUID using MD5): "
            "Generated by hashing a namespace identifier with a name using MD5."),
        4: ("UUIDv4 (Random UUID): "
            "Generated using random numbers."),
        5: ("UUIDv5 (Name-based UUID using SHA-1): "
            "Generated by hashing a namespace identifier with a name using SHA-1.")
    }
    
    # Print the chosen UUID version's explanation
    print(prefaces[version])
    
    # If UUIDv3 or UUIDv5 is selected and no name is provided, prompt for a name
    if version in [3, 5] and not name:
        name = input("Please provide a name for the name-based UUID: ")
    
    for _ in range(count):
        if version == 1:
            print(uuid.uuid1())
        elif version == 3:
            print(uuid.uuid3(uuid.NAMESPACE_DNS, name))
        elif version == 4:
            print(uuid.uuid4())
        elif version == 5:
            print(uuid.uuid5(uuid.NAMESPACE_DNS, name))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate different versions of UUIDs and print to stdout.")
    parser.add_argument('-v', '--version', type=int, choices=[1, 3, 4, 5], default=4, 
                        help="Version of UUID to generate. Options are: "
                             "1 (Time-based), "
                             "3 (Name-based using MD5), "
                             "4 (Random), "
                             "5 (Name-based using SHA-1). Default is 4 (Random).")
    parser.add_argument('-c', '--count', type=int, default=10, 
                        help="Count of UUIDs to generate (default is 10).")
    parser.add_argument('-n', '--name', type=str, default=None, 
                        help="Name for the name-based UUID (used with versions 3 and 5). If not provided, will prompt for input.")
    args = parser.parse_args()

    generate_uuids(args.version, args.count, args.name)
