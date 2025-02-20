import sys

class App:
    def __init__ (self, filePath):
        self.filePath = filePath
        self.data = ""
        
    def storeText(self):
        self.data = '''
                      TRY IT YOURSELF
1. Number Eight: Write addition, subtraction, multiplication, and division 
operations that each result in the number 8. Be sure to enclose your operations 
in print() calls to see the results. You should create four lines that look like this:
print(5+3)
Your output should be four lines, with the number 8 appearing once on 
each line.
2. Favorite Number: Use a variable to represent your favorite number. Then, 
using that variable, create a message that reveals your favorite number. Print 
that message.'''
    
    def writeFile(self):
        try:
            file = open(self.filePath, 'w') # Open a file in write mode
            file.write(self.data) # Write data to the file
            file.close() # Close the file when done
            print("File write complete")
            sys.exit(0)
            
        # Catch any exceptions raised
        except FileExistsError as error:
            print(f"File does not exist: {error}")
            sys.exit(1)
        except FileNotFoundError as error:
            print(f"File not found: {error}")
            sys.exit(1)
        

if(__name__ == "__main__"):
    app = App("./Lesson4/Exercises.txt")
    app.storeText()
    app.writeFile()