from rich import print
import time

class Book:

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        self.current_page = 1 

        print(f":open_book: [blue]You have started reading [red]{self.title}[/red] with {self.pages} pages. You are on [yellow]page {self.current_page}[/yellow].[/blue]")

    def advance_page(self, qtd = 1):
        cont = 0

        for pg in range(0, qtd, 1):
            if not self.end_book():
                self.current_page += 1

                print(f"Page {self.current_page} :arrow_forward: ", end="")

                time.sleep(0.1)
                cont += 1

        print(f"[blue] You advanced {cont} pages and you are on [yellow]page {self.current_page}[/yellow].[/blue]")

        if self.end_book():
            print(f":tada: [green]Congratulations! You have finished reading [red]{self.title}![/red][/green] :tada:")


    def end_book(self):
        if self.current_page == self.pages:
            return True
        else:
            return False


b1 = Book("The Great Gatsby", 50)
b1.advance_page(15)
b1.advance_page(30)
b1.advance_page(10)