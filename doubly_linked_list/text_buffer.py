# Tuesday lecture notes
from doubly_linked_list import DoublyLinkedList

class TextBuffer:
    def __init__(self, init=None):
        self.contents = DoublyLinkedList()
        if init:
            for char in init:
                self.contents.add_to_tail(char)
    
    def __str__(self):
        s = ""
        current = self.contents.head
        while current:
            s += current.value
            current = current.next
        return s
    
    def append(self, char):
        self.contents.add_to_tail(char)

    def prepend(self, char):
        self.contents.add_to_head(char)

    def delete_front(self):
        self.contents.remove_from_head()

    def delete_back(self):
        self.contents.remove_from_tail()

    def join(self, other_buffer):
        self.contents.tail.next = other_buffer.contents.head
        other_buffer.contents.head.prev = self.contents.tail
        other_buffer.contents.head = self.contents.head
        self.contents.tail = other_buffer.contents.tail

    def join_string(self, string_to_join):
        new_buffer = TextBuffer(string_to_join)
        self.join(new_buffer)

if __name__ == '__main__':    
    text = TextBuffer("Super")
    print(text)