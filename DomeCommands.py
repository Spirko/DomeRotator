import tkinter as tk
import tkinter.ttk as ttk
import serial

class DomeCommands(ttk.Frame):
  def __init__(self, master=None, ser=None, port=None, **kwargs):
    super().__init__(master, **kwargs)
    
    if ser is not None:
      self.ser = ser
    else:
      self.open_serial(port)

    # When sent, each command should be preceeded and followed by \n
    # This is handled by send_command()
    # These movement commands tell MDrive to keep going until otherwise instructed.
    self.buttons_info = [
      {'label': 'Left', 'press': 'AMR -1000000,1,1'},
      {'label': 'Stop', 'press': 'ASL 0'},
      {'label': 'Right', 'press': 'AMR 1000000,1,1'}
    ]
    
    for btn_info in self.buttons_info:
      button = ttk.Button(self, text=btn_info['label'])
      button.bind('<ButtonPress-1>', lambda e,s=btn_info['press']: self.send_command(s))
      button.bind('<ButtonRelease-1>', lambda e,s='ASL 0': self.send_command(s))
      button.pack(side=tk.LEFT, anchor='center', padx=5, pady=5)
      
  def send_command(self, command):
    data = f'\n{command}\n'
    if self.ser and self.ser.is_open:
      try:
        self.ser.write(data.encode())
      except serial.SerialException as e:
        print(f'Failed to write: {e}')
        
    else:
      print(f'Command to serial: {command}')

  def open_serial(self, port='COM3', baudrate=9600):
    try:
      self.ser = serial.Serial(port, baudrate, timeout=1)
      print(f'Connected to {port} at {baudrate} baud.')
    except serial.SerialException as e:
      print('Connecting to stdout.')
      self.ser = None


if __name__ == '__main__':
  root = tk.Tk()
  root.title('Serial Button test')
  root.geometry('300x100')

  frm = DomeCommands(master=root,port='COM5')
  frm.pack()

  root.mainloop()
  