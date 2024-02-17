from LinkedList import LinkedList
from Stack import Stack

linked_list = LinkedList(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)

print("Linked List:")
current = linked_list.head
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")

linked_list.remove()

print("Linked List after removing the last element:")
current = linked_list.head
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:")
while not stack.is_empty():
    print(stack.pop(), end=" ")
print("(bottom)")
