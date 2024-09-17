import tkinter as tk
import tkinter.ttk as ttk
from ComPortSelector import ComPortSelector
from CameraSelector import CameraSelector
from CameraDisplay2 import CameraDisplay
from DomeCommands import DomeCommands

# Requires conda packages:
#  python=3.12, pyserial, opencv, pygame

class DomeRotator(tk.Tk):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.title('Dome Rotator')
    self.geometry('800x600')
    
    self.make_bluetooth_frame()
    self.make_camera_frame()
    self.make_command_frame()
  
  def make_bluetooth_frame(self):
    self.blue_frm = ttk.Frame(master=self, borderwidth=2, relief='raised')
    self.blue_frm.pack(side=tk.TOP)
    
    blue_lbl = ttk.Label(self.blue_frm, text='Connect Bluetooth to "ESP32 MDrive"')
    blue_lbl.pack(side=tk.TOP)
  
  def make_camera_frame(self):
    self.cam_frm = ttk.Frame(master=self, borderwidth=2, relief='sunken')
    self.cam_frm.pack(expand=True)
    
    self.cam = CameraSelector(self.cam_frm)
    self.cam.pack(side=tk.TOP)
    
    self.disp = CameraDisplay(master=self.cam_frm)
    self.disp.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    self.cam.connect = lambda : \
      self.disp.connect(int(self.cam.combobox.current()))
    self.cam.disconnect = lambda : \
      self.disp.disconnect()
    
  def make_command_frame(self):
    self.cmd_frm = ttk.Frame(master=self, borderwidth=2, relief='sunken')
    self.cmd_frm.pack()

    self.com = ComPortSelector(self.cmd_frm)
    self.com.pack(side=tk.LEFT, fill=tk.X, padx=20)
    
    self.dome = DomeCommands(self.cmd_frm)
    self.dome.pack()
  
    self.com.combobox.bind("<<ComboboxSelected>>", 
        lambda arg: self.dome.open(self.com.combobox.get()))


if __name__ == "__main__":
  app = DomeRotator()
  app.mainloop()