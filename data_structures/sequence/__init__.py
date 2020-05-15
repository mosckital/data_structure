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
from .array.fixed_array import FixedArray
from .array.dynamic_array import DynamicArray
# linked list
from .linked_list.custom_linked_list import LinkedListMixin
from .linked_list.singly_linked_list import SinglyLinkedList
from .linked_list.doubly_linked_list import DoublyLinkedList
# stack
from .queue_stack.custom_stack import CustomStack
from .queue_stack.linked_stack import LinkedStack
from .queue_stack.array_stack import ArrayStack
from .queue_stack.queued_stack import QueuedStack
# queue
from .queue_stack.custom_queue import CustomQueue
from .queue_stack.linked_queue import LinkedQueue
from .queue_stack.array_queue import ArrayQueue
from .queue_stack.stacked_queue import StackedQueue
