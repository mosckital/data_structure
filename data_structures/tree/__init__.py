
"""
The custom implementations of the common tree data structure.

This package includes the custom implementations of the common tree data
structures like binary tree, binary search tree, n-ary tree etc. These
implementations are only for learning purpose and have no practical usage.

All the implemented classes are flatly imported here so that one can easily
import them by `data_structure.tree.ClassName` instead of adding the module file
name before the class name in the path
"""
from .tree import Tree
# binary tree
from .binary_tree import BinaryTree
from .array_binary_tree import ArrayBinaryTree
from .linked_binary_tree import LinkedBinaryTree
from .doubly_linked_binary_tree import DoublyLinkedBinaryTree
# binary search tree
from .binary_search_tree import BinarySearchTree
from .array_binary_search_tree import ArrayBinarySearchTree
from .linked_binary_search_tree import LinkedBinarySearchTree
from .doubly_linked_binary_search_tree import DoublyLinkedBinarySearchTree
# balanced binary tree
from .balanced_binary_search_tree import BalancedBinarySearchTree
from .red_black_tree import RedBlackTree
