from returns.result import Result, Success, Failure
from rich.console import Console
import os

class ConsoleView:
    def __init__(self):
        self.console = Console(height = 45)
        self.clear()

    def clear(self):
        os.system("cls")

    def print(self, display_str):    
        self.console.print(display_str)

    def error(self, display_str):
        self.print("[red]Error[/red]"+ display_str)

    def debug(self, key, value):
        self.console.print(f"{key}: {value}")

    def ask(self, prompt:str = "") -> Result[list[str],str]:
        try:
            if prompt == "":
                raw_ask_resp = self.console.input("[yellow]Minerva[/yellow]> ")
            else:
                raw_ask_resp = self.console.input(f" {prompt}")
            ask_data = raw_ask_resp.strip().lower()
            return Success(ask_data)
        
        except BaseException as e:
            return Failure(str(e))

    def parse_command(self, new_input:str) -> Result[list[str], str]:
        try:
            if " " in new_input and \
                new_input.count(" ") > 0:
                raw_data = new_input.split(" ", 1)
                return Success(raw_data)
            else:
                return Success([new_input, None])
        except BaseException as e:
            return Failure(str(e))

    def request(self) -> Result[list[str], str]:
        try:
            ask_resp = self.ask()
            if isinstance(ask_resp, Failure):
                return ask_resp
            new_input = ask_resp.unwrap()
            if new_input == "exit" or new_input == "bye":
                return [-1]
            return self.parse_command(new_input)
        except BaseException as e:
            return Failure(str(e))

if __name__ == "__main__":
    cv = ConsoleView()

    cv.print("ConsoleView Test")
    samp = cv.ask("Sample?")
    cv.debug("NextLine", samp)
    cv.request()