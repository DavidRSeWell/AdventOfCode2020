
class Tree:
    def __init__(self):
        self.tree = {} # nodes: [children]
        self.edges = {} # nodes: [edges]

    def add_line(self,line):

        line = line.split(" ")
        type = " ".join(line[:2])
        if type not in self.tree:
            self.add_node(None,type,None)

        contain_index = line.index("contain")
        child_text = line[contain_index + 1:]
        if "no other bags" in " ".join(child_text):
            return
        else:
            bags = " ".join(child_text).split(",")
            self.process_bags(bags,type)

    def add_node(self,child,parent,q):
        if child is None:
            self.tree[parent] = []
            self.edges[parent] = []
        else:
            self.tree[parent].append(child)
            self.edges[parent].append(q)

    def count_bag(self,node,bag):

        count = 0
        children = self.tree[node]
        edges = self.edges[node]
        for child_bag in children:
            if child_bag == bag:
                count += edges[children.index(bag)]
            else:
                count += self.count_bag(child_bag,bag)

        return count

    def count_contains(self,type,part="1"):

        tot_count = 0
        for node in self.tree.keys():
            count = self.count_bag(node,type)
            if part == "1":
                if count > 0:
                    tot_count += 1


        return tot_count

    def get_total_edges(self,type):
        """
        For part 2
        :return:
        """
        chidren = self.tree[type]
        edges = self.edges[type]
        count = 1
        for child in chidren:
            child_edge_value = edges[chidren.index(child)]
            count += child_edge_value*self.get_total_edges(child)

        return count

    def process_bags(self,bags,parent):
        for bag in bags:
            bag = bag.split()
            q = int(bag[0])
            type = " ".join(bag[1:3])
            self.add_node(type,parent,q)


def clean_line(line):
    line = line.replace("\n","")
    line = line.replace(".","")
    return line


def run(data_path,query,part="1"):
    tree = Tree()
    lines = open(data_path).readlines()
    for line in lines:
        tree.add_line(clean_line(line))

    if part == "1":
        count = tree.count_contains(query,part=part)
        print(f"Part 1 answer is {count}")
    elif part == "2":
        count = tree.get_total_edges(query) - 1
        print(f"Part 2 answer is {count}")

    else:
        print(f"Illegal part {part}")


if __name__ == "__main__":
    data_path = "data/day7.txt"
    run(data_path,"shiny gold",part="1")
    run(data_path,"shiny gold",part="2")