class Node:
    def __init__(self, data, style='white'):
        self.data = data
        self.style = style
        self.next = None
        self.prev = None

class Dlinkedlist:
    def __init__(self):
        self.head = None
        self.cursor = Node('_','bold blink white')

    def left(self):
        if self.cursor.prev:
            current=self.cursor.next
            pre1=self.cursor.prev
            pre2=pre1.prev
            if(pre2!=None):
                pre2.next=self.cursor
                self.cursor.prev=pre2
                pre1.prev=self.cursor
                self.cursor.next=pre1
                pre1.next=current
                if(current!=None):
                    current.prev=pre1
            else:
                pre1.next=current
                current.prev=pre1
                self.cursor.next=pre1
                pre1.prev=self.cursor
                self.cursor.prev=None
                self.head=self.cursor

    def right(self):
        if self.cursor.next:
            next1 = self.cursor.next
            next2 = next1.next
            current = self.cursor.prev
            if(current!=None and next2!=None):
                next1.prev=current
                current.next=next1
                next1.next=self.cursor
                self.cursor.next=next2
                self.cursor.prev=next1
                next2.prev=self.cursor
                return
            elif(next2==None):
                next1.next=self.cursor
                current.next=next1
                next1.prev=current
                self.cursor.prev=next1
                self.cursor.next=None
                return
            next1.next=self.cursor
            self.cursor.prev=next1
            self.cursor.next=next2
            next2.prev=self.cursor
            next1.prev=None
            self.head=next1

    def CursorPosition(self, curent):
        curent.next = self.cursor
        self.cursor.prev = curent

    def insert(self, data):
        temp = Node(data)
        if (self.head == None):
            self.head = temp
            return self.head
        curr = self.head
        while (curr.next):
            curr = curr.next
        curr.next = temp
        temp.prev = curr
        return temp

    def insertBeforeCursor(self,data, style='white'):
        temp=Node(data, style)
        if(self.cursor.prev!=None):
            pre = self.cursor.prev
            pre.next = temp
            temp.next = self.cursor
            temp.prev = pre
            self.cursor.prev = temp
            return
        self.cursor.prev = temp
        temp.next = self.cursor
        self.head = temp
        return

    def backspace(self):
        pre1 = self.cursor.prev
        if (self.cursor.prev is None):
            return
        elif(pre1.prev==None):
            self.cursor.prev=None
            self.head=self.cursor
        else:
            pre2=pre1.prev
            pre2.next=self.cursor
            self.cursor.prev=pre2

    def delete(self):
        nex1 = self.cursor.next
        if (self.cursor.next is None):
            return
        elif(nex1.next==None):
            self.cursor.next=None
        else:
            nex2=nex1.next
            nex2.prev=self.cursor
            self.cursor.next=nex2

    def is_empty(self):
        return self.head is None 

    def printt(self):
        temp = self.head
        while (temp.next):
            print('['+temp.style+']'+temp.data,end='')
            temp = temp.next
        print(temp.data)


from rich.console import Console
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
import os

try:
        if not os.path.exists("TextFiles"):
            os.makedirs("TextFiles")
except OSError:
        pass

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

c = Console()
clear_screen()

def disp_main_menu():
    width = os.get_terminal_size().columns
    space = ' '*(width//2 - 39)
    logotxt = f"""{space}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{space}░░░░█████╗░░█████╗░██╗░░░░░░█████╗░██████╗░░░░████████╗██╗░░██╗████████╗░░░
{space}░░░██╔══██╗██╔══██╗██║░░░░░██╔══██╗██╔══██╗░░░╚══██╔══╝╚██╗██╔╝╚══██╔══╝░░░
{space}░░░██║░░╚═╝██║░░██║██║░░░░░██║░░██║██████╔╝░░░░░░██║░░░░╚███╔╝░░░░██║░░░░░░
{space}░░░██║░░██╗██║░░██║██║░░░░░██║░░██║██╔══██╗░░░░░░██║░░░░██╔██╗░░░░██║░░░░░░
{space}░░░╚█████╔╝╚█████╔╝███████╗╚█████╔╝██║░░██║░░░░░░██║░░░██╔╝╚██╗░░░██║░░░░░░
{space}░░░░╚════╝░░╚════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░░░░
{space}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    """
    start_screen_text = f"{logotxt}\n   [bold red][1] [white]New File [/bold red]    [bright_green italic]← Create a brand new file to write your colorful & amazing text![/bright_green italic]\n   [bold red][2] [white]Open File[/bold red]    [bright_green italic]← Open a file that already exists (of the format .ctxt)[/bright_green italic]\n   [bold red][3] [white]About[/bold red]        [bright_green italic]← About the developers of this colorful TextEditor![/bright_green italic]\n   [bold red][4] [white]Exit[/bold red]         [bright_green italic]← To exit the application!"
    print(Panel(start_screen_text, title="[bold blue]Main Menu", expand=True, padding=1))


help_text = """[white]● [light_cyan1]'insert' or 'i' [light_steel_blue]→ [grey66] to insert a character or string of characters
[white]● [light_cyan1]'print' or 'p' [light_steel_blue] → [grey66] to display the file contents
[white]● [light_cyan1]'style' or 's' [light_steel_blue] → [grey66] to change the text style
[white]● [light_cyan1]'quit or 'q' [light_steel_blue]   → [grey66] to exit the edit mode and return to main menu
[white]● [light_cyan1]'l' [light_steel_blue]            → [grey66] to move the cursor left
[white]● [light_cyan1]'r' [light_steel_blue]            → [grey66] to move the cursor right
[white]● [light_cyan1]'b' [light_steel_blue]            → [grey66] to remove the char before the cursor
[white]● [light_cyan1]'d' [light_steel_blue]            → [grey66] to remove the char after the cursor
[white]● [light_cyan1]'save' [light_steel_blue]         → [grey66] to save the text file
[white]● [light_cyan1]'cursor' [light_steel_blue]       → [grey66] to change the cursor indicator"""


def main_menu():
    disp_main_menu()

    choice = Prompt.ask(" Enter Your Choice",choices=['1','2','3','4'])

    if choice == '1':
        filename = Prompt.ask(" Enter New Filename")
        clear_screen()
        edit_page(filename,Dlinkedlist())

    elif choice == '2':
        text_lst = Dlinkedlist()
        while True:
            filename = Prompt.ask(" Enter Filename to Open")
            try:
                f = open(f'TextFiles/{filename}.ctxt','r',encoding="utf-8")
                try:
                    
                    content = f.read()
                    lst = content.split(' ')
                    for i in lst:
                        style = i.split('›')[0][1:]
                        char = i.split('›')[1]
                        text_lst.insertBeforeCursor(char,style)
                    break

                except:
                    print("[red] There was a problem opening your file, try again...")
            except:
                print("[red] File doesn't exist! Check your file name and try again...")

        clear_screen()
        edit_page(filename, text_lst)

    elif choice == '3':
        width = os.get_terminal_size().columns
        space = ' '*(width//2 - 27)
        about_text = f"""
        {space}[thistle1]This application was developed by
            {space}[white]● [light_cyan1]Gokulram A [honeydew2](205002033)
            {space}[white]● [light_cyan1]Mithran K  [honeydew2](205002049)
            {space}[white]● [light_cyan1]Guhan S    [honeydew2](205002034)
        """
        clear_screen()
        print(Panel(about_text, title="[bold blue]About", expand=True, padding=1))
        a = input("Press Enter key to return to the main menu...")
        clear_screen()
        main_menu()

    elif choice == '4':
        print("[orange_red1]Exiting...")

# Edit page functions

def save(filename, text):
    try:
        f = open(f'TextFiles/{filename}.ctxt','w',encoding="utf-8")
        save_text = ""
        temp = text.head
        while temp:
            if temp.data != text.cursor.data:
                char = temp.data
                style = temp.style
                save_text += f"‹{style}›{char+' '}"
            temp = temp.next

        f.write(save_text[:-1])
        f.close()
        print("[green4] Save successful!")
    except:
        print("[bright_red] Save unsucessful! Try again...")

def edit_page(filename, text):
    c.rule(f"[bold red]{filename}.ctxt")
    default_style = "white"
    current_style = default_style
    while True:
        print("[bold italic green] >>> ", end = '')
        input_text = input()
        command = input_text.split(' ')[0].lower()
        
        if command == 'i' or command == 'insert':
            chars = input_text[2:] if command == 'i' else input_text[7:]
            for char in chars:
                text.insertBeforeCursor(char,current_style)

        elif command == 'p' or command == 'print':
            
            print_text = ""
            
            temp = text.head
            while temp:
                if temp.data == '\\' and temp.next.data == 'n':
                    print_text += '\n'
                elif temp.data == 'n' and temp.prev.data == '\\':
                    pass
                else:
                    char = temp.data
                    style = temp.style
                    print_text += f"[{style}]{char}[/{style}]"
                temp = temp.next         

            print(Panel(print_text))

        elif command == 's' or command == 'style':
            current_style = input_text[2:]
            print(f"[purple italic bold]Style:[/purple italic bold] [green  italic]'[light_green]{current_style}[green]'")
            print()

        elif command == 'save':
            save(filename, text)
        
        elif command == 'l':
            input_text = input_text.strip()
            if input_text == 'l':
                text.left()
            else:
                try:
                    n = int(input_text[2:].strip())
                    for i in range(n):
                        text.left()
                except:
                    print("[bold bright_red] Please enter a valid number after 'l' ")


        elif command == 'r':
            input_text = input_text.strip()
            if input_text == 'r':
                text.right()
            else:
                try:
                    n = int(input_text[2:].strip())
                    for i in range(n):
                        text.right()
                except:
                    print("[bold bright_red] Please enter a valid number after 'r' ")

        elif command == 'b':
            input_text = input_text.strip()
            if input_text == 'b':
                text.backspace()
            else:
                try:
                    n = int(input_text[2:].strip())
                    for i in range(n):
                        text.backspace()
                except:
                    print("[bold bright_red] Please enter a valid number after 'b' ")
        
        elif command == 'd':
            input_text = input_text.strip()
            if input_text == 'd':
                text.delete()
            else:
                try:
                    n = int(input_text[2:].strip())
                    for i in range(n):
                        text.delete()
                except:
                    print("[bold bright_red] Please enter a valid number after 'd' ")

        elif command == 'cursor':
            cur = input_text.split()[1]
            text.cursor.data = cur

        elif command == 'q' or command == 'quit':
            break

        elif command == 'help':
            print(help_text)
        else:
           print("[bold bright_red] Command doesn't exist! Try 'help' to list all the available commands.")

    clear_screen()
    main_menu()   

main_menu()