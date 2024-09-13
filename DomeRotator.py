import tkinter as tk
import tkinter.ttk as ttk
from ComPortSelector import ComPortSelector
from CameraSelector import CameraSelector
from CameraDisplay2 import CameraDisplay
from DomeCommands import DomeCommands

class DomeRotator(tk.Tk):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.title('Dome Rotator')
    self.geometry('800x600')
    
    self.make_config_frame()
    self.make_camera_frame()
    self.make_command_frame()
    
  def make_config_frame(self):
    self.cfg_frm = ttk.Frame(master=self, borderwidth=2, relief='sunken')
    self.cfg_frm.pack(expand=True)
    
    self.com = ComPortSelector(self.cfg_frm)
    self.com.pack(side=tk.LEFT, fill=tk.X, padx=20)
    
    self.cam = CameraSelector(self.cfg_frm)
    self.cam.pack(side=tk.LEFT, padx=20)
    
  def make_camera_frame(self):
    self.cam_frm = ttk.Frame(master=self)
    self.cam_frm.pack(expand=True)
    
    self.disp = CameraDisplay(master=self.cam_frm)
    self.disp.pack(fill=tk.BOTH, expand=True)
    
    self.cam.connect = lambda : \
      self.disp.connect(int(self.cam.combobox.current()))
    self.cam.disconnect = lambda : \
      self.disp.disconnect()
    
  def make_command_frame(self):
    self.cmd_frm = ttk.Frame(master=self)
    self.cmd_frm.pack(expand=True)

    self.dome = DomeCommands(self.cmd_frm)
    self.dome.pack()
  
    self.com.combobox.bind("<<ComboboxSelected>>", 
        lambda arg: self.dome.open(self.com.combobox.get()))

        
if __name__ == "__main__":
  app = DomeRotator()
  app.mainloop()