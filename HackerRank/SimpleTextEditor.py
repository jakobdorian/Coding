class SimpleTextEditor():
    def __init__(self):
        self.text = ""  # an empty string to store the current text
        self.history = []  # a list to store the history of text states
        
    def append(self, w):
        self.history.append(self.text)  # save the current state of text to history before making changes
        self.text += w  # append the given string w to the current text
    
    def delete(self, k):
        self.history.append(self.text)  # save the current state of text to history before making changes
        self.text = self.text[:-k]  # delete the last k characters from the current text
        
    def print_kth(self, k):
        if 1 <= k <= len(self.text):  # check if k is within the valid range
            print(self.text[k - 1])  # orint the k-th character (1-based index)
        else:
            raise IndexError("Index out of range")  # raise an error if k is out of range
    
    def undo(self):
        if self.history:  # check if there is any history to undo
            self.text = self.history.pop()  # restore the last saved state of text
# read input
if __name__ == "__main__":  
    import sys
    input = sys.stdin.read  # read all input from standard input
    
    editor = SimpleTextEditor()  # create an instance of the SimpleTextEditor class
    data = input().strip().split('\n')  # read input and split it into lines
    q = int(data[0])  # the first line contains the number of operations
    
    for i in range(1, q + 1):
        command = data[i].split()  # split each line into command parts
        op_type = int(command[0])  # the first part of the command determines the operation type
        
        if op_type == 1:
            editor.append(command[1])  # append operation
        elif op_type == 2:
            editor.delete(int(command[1]))  # delete operation
        elif op_type == 3:
            try:
                editor.print_kth(int(command[1]))  # print operation
            except IndexError:
                print("Error: Index out of range")
        elif op_type == 4:
            editor.undo()  # undo operation
