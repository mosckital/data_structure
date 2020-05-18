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
# abstract base classes for stack and queue
from .stack_queue.custom_stack_queue import CustomStackQueue
from .stack_queue.custom_stack_queue import CustomStack, CustomQueue
# stack
from .stack_queue.linked_stack import LinkedStack
from .stack_queue.array_stack import ArrayStack
from .stack_queue.queued_stack import QueuedStack
# queue
from .stack_queue.linked_queue import LinkedQueue
from .stack_queue.array_queue import ArrayQueue
from .stack_queue.stacked_queue import StackedQueue
