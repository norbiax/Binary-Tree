from statistics import median

def sum_in_node(root):
    if root is None:
        return 0
    return (root.key +
            sum_in_node(root.left) +
            sum_in_node(root.right))

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

    print("W wybranym poddrzewie znajdują się następujące węzły: ", tot_nodes(root))
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

    print('Wartości w poddrzewie uporzadkowane rosnąco: ', tot_nodes(root))
    return median(tot_nodes(root))
