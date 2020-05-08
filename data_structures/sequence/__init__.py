"""
The custom implementations of the common sequence-like data structures.

This packages includes the custom implementations of the common sequence-like
data structures like arrays and linked lists. These implementations are only for
learning purpose and have no practical usage.

All the implemented classes are flatly imported here so that one can easily
import them by `data_structure.sequence.ClassName` instead of adding the module
file name before the class name in the path.
"""
# array
from .custom_sequence import CustomSequence
from .fixed_array import FixedArray
from .dynamic_array import DynamicArray
# linked list
from .custom_linked_list import LinkedListMixin
from .singly_linked_list import SinglyLinkedList
from .doubly_linked_list import DoublyLinkedList
# stack
from .custom_stack import CustomStack
from .linked_stack import LinkedStack
from .array_stack import ArrayStack
# queue
from .custom_queue import CustomQueue
from .linked_queue import LinkedQueue
from .array_queue import ArrayQueue
