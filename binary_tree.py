from statistics import median


class NewNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


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


print('Struktura drzewa:')
print('')
print('')
print('     #                   |5|                     #')
print('     #                /       \                  #')
print('     #              |3|       |7|                #')
print('     #             /   \     /   \               #')
print('     #           |2|   |5| |1|   |0|             #')
print('     #                          /   \            #')
print('     #                        |2|   |8|          #')
print('     #                                 \         #')
print('     #                                 |5|       #')
print('')
print('')

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

nodes = {
    "root": 5,
    "root.left": 3,
    "root.right": 7,
    "root.left.left": 2,
    "root.left.right": 5,
    "root.right.left": 1,
    "root.right.right": 0,
    "root.right.right.left": 2,
    "root.right.right.right": 8,
    "root.right.right.right.right": 5
    }

print(list(nodes.keys()))
print('')

ch_node = input('Dla którego węzła wykonać obliczenia? \n')

print("Węzeł {} ma wartość {}".format(ch_node, nodes[ch_node]))

if ch_node == "root":
    x = root
if ch_node == "root.left":
    x = root.left
if ch_node == "root.right":
    x = root.right
if ch_node == "root.left.left":
    x = root.left.left
if ch_node == "root.left.right":
    x = root.left.right
if ch_node == "root.right.left":
    x = root.right.left
if ch_node == "root.right.right":
    x = root.right.right
if ch_node == "root.right.right.right":
    x = root.right.right.right
if ch_node == "root.right.right.left":
    x = root.right.right.left
if ch_node == "root.right.right.right.right":
    x = root.right.right.right.right

sum_in_node = sum_in_node(x)
print("Suma wartości w wybranym poddrzewie wynosi: ", sum_in_node)

avg = avg(x)
print("Średnia wartość wynosi: ", round(avg, 2))

med = med(x)
print("Stąd mediana wynosi: ", med)
