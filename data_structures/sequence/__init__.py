"""
The custom implementations of the common sequence-like data structures.

This packages includes the custom implementations of the common sequence-like
data structures like arrays and linked lists. These implementations are only for
learning purpose and have no practical usage.

All the implemented classes are flatly imported here so that one can easily
import them by `data_structure.sequence.ClassName` instead of adding the module
file name before the class name in the path.
"""
from .custom_sequence import CustomSequence
from .fixed_array import FixedArray
from .dynamic_array import DynamicArray
from .custom_linked_list import LinkedListMixin
from .singly_linked_list import SinglyLinkedList
from .doubly_linked_list import DoublyLinkedList
