from statistics import median


class NewNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


if __name__ == '__main__':
    root = NewNode(5)
    root.left = NewNode(3)
    root.right = NewNode(7)
    root.left.left = NewNode(2)
    root.left.right = NewNode(5)
    root.right.left = NewNode(1)
    root.right.right = NewNode(0)
    root.right.right.left = NewNode(2)
    root.right.right.right = NewNode(8)
    root.right.right.right.right = NewNode(5)


def addBT(root):
    if root == None:
        return 0
    return (root.key +
            addBT(root.left) +
            addBT(root.right))


def avg(root):
    def tot_nodes(root):

        def list_of_child_for_root(root):
            lst = []
            if root is None:
                return []
            if root.left:
                lst.append(root.left.key)
            if root.right:
                lst.append(root.right.key)

            return (lst +
                    list_of_child_for_root(root.right) +
                    list_of_child_for_root(root.left))

        return [root.key] + list_of_child_for_root(root)

    print(tot_nodes(root))
    return sum(tot_nodes(root)) / len(tot_nodes(root))


def med(root):
    def tot_nodes(root):

        def list_of_child_for_root(root):
            lst = []
            if root is None:
                return []
            if root.left:
                lst.append(root.left.key)
            if root.right:
                lst.append(root.right.key)

            return (lst +
                    list_of_child_for_root(root.right) +
                    list_of_child_for_root(root.left))

        return sorted([root.key] + list_of_child_for_root(root))

    print(tot_nodes(root))
    return median(tot_nodes(root))

tot_sum = addBT(root)

print("Sum of all the nodes is:", tot_sum)

avg1 = avg(root)
print("Total avg", round(avg1, 2))

med = med(root)
print("Med of node: ", med)
