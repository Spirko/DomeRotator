import tkinter as tk
import tkinter.ttk as ttk
from ComPortSelector import ComPortSelector
from CameraSelector import CameraSelector
from CameraDisplay import CameraDisplay

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
    
    self.disp = CameraDisplay()
    self.disp.pack(fill=tk.BOTH, expand=True)
    
  def make_command_frame(self):
    self.cmd_frm = ttk.Frame(master=self)
    self.cmd_frm.pack(expand=True)

        
if __name__ == "__main__":
  app = DomeRotator()
  app.mainloop()