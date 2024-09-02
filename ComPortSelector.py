
import tkinter as tk
import tkinter.ttk as ttk
import serial.tools.list_ports as lp

class ComPortSelector(tk.Frame):
  def __init__(self, master=None, **kwargs):
    super().__init__(master, **kwargs)
    
    self.pack()
    
    self.label = ttk.Label(self, text='Select COM port:')
    self.label.pack(side=tk.LEFT)
    
    self.combobox = ttk.Combobox(self, state='readonly')
    self.combobox.pack(side=tk.LEFT)
    
    self.get_ports()
    self.combobox.current(0)
    
  def get_ports(self):
    ports = lp.comports()
    port_list = [port.device for port in ports]
    if not port_list:
      port_list = 'None found'
      
    self.combobox['values'] = port_list
    
def print_choice(label, combobox):
  choice = combobox.get()
  print(f"{label}: {choice}")


    
if __name__ == "__main__":
  app = tk.Tk()
  app.title('Com port selector test')
  
  com = ComPortSelector()
  com.combobox.bind("<<ComboboxSelected>>", 
                    lambda arg:
                    print_choice("Selected Com:", com.combobox))
  app.mainloop()
