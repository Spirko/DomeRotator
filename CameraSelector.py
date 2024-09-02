import tkinter as tk
import tkinter.ttk as ttk
import cv2
import itertools


class CameraSelector(tk.Frame):
  def __init__(self, master=None, **kwargs):
    super().__init__(master, **kwargs)
    
    self.pack()
        
    self.label = ttk.Label(self, text='Select Camera:')
    self.label.pack(pady=10)
    
    self.combobox = ttk.Combobox(self, state='readonly')
    self.combobox.pack(pady=10)
    self.detect_cameras()
    self.combobox.current(0)
    
  def detect_cameras(self):
    available_cameras = []
    
    for i in itertools.count(start=0):
      cap = cv2.VideoCapture(i)
      if cap.isOpened():
        available_cameras.append(f'Camera {i}')
        cap.release()
      else:
        break
    
    if not available_cameras:
      available_cameras.append("No cameras found")
      
    self.combobox['values'] = available_cameras

def print_choice(combobox):
  selected_camera = combobox.get()
  print(f"selected camera: {selected_camera}")

if __name__ == "__main__":
  app = tk.Tk()
  app.title('Camera Selector test')
  
  cam = CameraSelector(app)
  cam.combobox.bind("<<ComboboxSelected>>", lambda arg: print_choice(cam.combobox))
  app.mainloop()
