import tkinter as tk
import time



class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Main Window")

    def set_title(self, title):
        self.root.title(title)

    def set_frame(self, frame):
        self.mainframe = frame
        self.mainframe.pack()

    def remove_frame(self):
        if hasattr(self, 'mainframe') and self.mainframe is not None:
            self.mainframe.pack_forget()
            del self.mainframe

    def switch_frame(self, new_frame):
        self.remove_frame()
        self.set_frame(new_frame)

    def show(self):
        index = 0
        red = tk.Frame(self.root, width=400, height=300, bg="red")
        blue = tk.Frame(self.root, width=400, height=300, bg="blue")
        try: 
            while True:
                index += 1
                print(f"Update count: {index}")
                print("Updating main window...")
                if index % 2 == 0:
                    self.switch_frame(red)
                else:
                    self.switch_frame(blue)
                time.sleep(1)
                self.root.update()
                self.root.update_idletasks()
                if not self.root.winfo_exists():
                    break
        except tk.TclError:
            self.root.mainloop()
            pass
        print("Main window closed.")

if __name__ == "__main__":
    main_window = MainWindow()


    main_window.show()
