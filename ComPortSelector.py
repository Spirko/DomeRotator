
import tkinter as tk
import tkinter.ttk as ttk
import serial.tools.list_ports as lp

class ComPortSelector(tk.Tk):
  def __init__(self):
    super().__init__()
    
    self.title('Select COM port')
    
    self.label = ttk.Label(self, text='Select COM port:')
    self.label.pack(pady=10)
    
    self.combobox = ttk.Combobox(self, state='readonly')
    self.combobox.pack(pady=10)
    
    self.get_ports()
    
  def get_ports(self):
    ports = lp.comports()
    port_list = [port.device for port in ports]
    if not port_list:
      port_list = 'None found'
      
    self.combobox['values'] = port_list
    
    
if __name__ == "__main__":
  app = ComPortSelector()
  app.mainloop()
