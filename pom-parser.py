import sys


class Dependency:
    def __init__(self, groupId, artifactId):
        self.groupId = groupId
        self.artifactId = artifactId

    def to_string(self):
        return self.groupId + "\n" + self.artifactId + "\n"

    def __eq__(self, other):
        if not isinstance(other, Dependency):
            return NotImplemented
        return self.groupId == other.groupId and self.artifactId == other.artifactId

    def __hash__(self):
        return hash(self.groupId + self.artifactId)


def parse_pom(path):
    deps = []
    with open(path, "r", encoding="UTF-8") as f:
        lines = f.readlines()

        rows = len(lines)
        for x in range(rows):
            if lines[x].strip().startswith("<dependency>"):
                deps.append(Dependency(lines[x+1].strip(), lines[x+2].strip()))
    return deps


def list_and_sort_deps(path):
    for d in parse_pom(path):
        print(d.to_string())


def check_duplicates(path):
    deps = parse_pom(path)
    if len(set(deps)) == len(deps):
        print("No duplicates found in: " + path)
    else:
        print("Possible duplicates found in: " + path)


def check_collisions(file_1, file_2):
    deps_1 = parse_pom(file_1)
    deps_1.sort(key=lambda x: x.groupId)

    if len(set(deps_1)) == len(deps_1):
        print("No duplicates found in: " + file_1)
    else:
        print("Possible duplicates found in: " + file_1)

    deps_2 = parse_pom(file_2)
    deps_2.sort(key=lambda x: x.groupId)

    if len(set(deps_2)) == len(deps_2):
        print("No duplicates found in: " + file_2 + "\n")
    else:
        print("Possible duplicates found in: " + file_2+ "\n")

    print("Dependency collisions: ")
    for d in deps_2:
        if d in deps_1:
            print(d.to_string())


def main():
    if len(sys.argv) < 2:
        print("No arguments, use --help for list of valid commands")
    elif len(sys.argv) == 2:
        if (sys.argv[1] == "--help"):
            print("Valid commands:" +
                  "\n" +
                  "list-and-sort-deps <pom>" +
                  " - Prints a list of dependencies in sorted order, only prints groupId and artifactId" +
                  "\n" +
                  "check_duplicates <pom>" +
                  " - Checks if the specified pom contains duplicate dependencies" +
                  "\n" +
                  "check-collisions <pom_1> <pom_2>" +
                  " - Prints a list of dependencies in pom_2 which already exist in pom_1" +
                  "\n")
        else:
            print("Invalid arguments, use --help for list of valid commands")
    elif len(sys.argv) == 3:
        if sys.argv[1] == "list-and-sort-deps":
            list_and_sort_deps(str(sys.argv[2]))
        elif sys.argv[1] == "check-duplicates":
            check_duplicates(str(sys.argv[2]))
        else:
            print("Invalid arguments, use --help for list of valid commands")
    elif len(sys.argv) == 4:
        if sys.argv[1] == "check-collisions":
            check_collisions(str(sys.argv[2]), str(sys.argv[3]))
        else:
            print("Invalid arguments, use --help for list of valid commands")
    else:
        print("Invalid arguments, use --help for list of valid commands")


if __name__ == "__main__":
    main()