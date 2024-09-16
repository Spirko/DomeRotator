import tkinter as tk
import tkinter.ttk as ttk
import os, sys

import warnings
warnings.simplefilter('ignore')
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
warnings.resetwarnings()
import cv2

class CameraDisplay(tk.Frame):
  def __init__(self, master=None, camera_index=None, **kwargs):
    super().__init__(master, **kwargs)
    
    self.camera_index = None # Will be initialized by self.connect()
    self.cap = None
    self.running = False
    
    os.environ['SDL_WINDOWID'] = str(self.winfo_id())
    pygame.init()

    self.connect(camera_index)
    
  def connect(self, camera_index=None):
    self.disconnect()
      
    self.camera_index = camera_index
    if self.camera_index is not None:
      print(f'Connecting to camera {self.camera_index}')  
      self.cap = cv2.VideoCapture(self.camera_index, cv2.CAP_DSHOW)
      self.running = True

    if self.cap is not None:
      self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
      self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
      self.configure(width=self.width, height=self.height)
      self.pack_propagate(False)
      print(f'Screen size: {self.width},{self.height}')
      self.start_pygame_display()

  def start_pygame_display(self):
    self.screen = pygame.display.set_mode((self.width, self.height))
    pygame.display.init()
    self.after(0, self.update_frame)
    
  def pygame_quit(self):
    self.running = False
    if pygame.display.get_init():
      pygame.display.quit()
  

  def disconnect(self):
    if self.cap is not None and self.cap.isOpened():
      self.cap.release()
    self.pygame_quit()
    

  def update_frame(self):
    # Do nothing if not connected or halted.
    if ( not self.running ) or self.cap is None:
      return
    # print('Updating frame')
    ret, frame = self.cap.read()
    if ret:
      frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0,1))
      self.screen.blit(frame_surface, (0,0))
      pygame.display.flip()
      
    self.after(10, self.update_frame)

  def destroy(self):
    self.disconnect() # closes camera and pygame connection
    pygame.quit()
    super().destroy()

if __name__ == "__main__":
  root = tk.Tk()
  root.minsize(300,200)
  root.title("Camera in pygame in tkinter")
  
  webcam_frame = CameraDisplay(root)
  webcam_frame.pack(expand=True, fill=tk.BOTH)
  
  onoff_frame = ttk.Frame(root)
  onoff_frame.pack()
  off_btn = ttk.Button(onoff_frame, text='Off', command=lambda: webcam_frame.disconnect())
  off_btn.pack(side=tk.LEFT)
  on_btn = ttk.Button(onoff_frame, text='On Cam 0', command=lambda: webcam_frame.connect(0))
  on_btn.pack(side=tk.LEFT)
  
  
  
  root.mainloop()
