import tkinter as tk
import tkinter.ttk as ttk
import cv2
import itertools
import warnings

class CameraSelector(tk.Frame):
  def __init__(self, master=None, **kwargs):
    super().__init__(master, **kwargs)
    
    # self.pack()
        
    self.label = ttk.Label(self, text='Select Camera:')
    self.label.pack(side=tk.LEFT)
    
    self.combobox = ttk.Combobox(self, state='readonly')
    self.combobox.pack(side=tk.LEFT)
    self.detect_cameras()
    
    style = ttk.Style()
    style.theme_use('winnative')

    self.connected = False
    self.button = ttk.Button(self, text='Connect', state=['raised'], command=self.toggle_button)
    self.button.pack(side=tk.LEFT, padx=20)
  
  def toggle_button(self):
    if not self.connected:
      if self.combobox.get():
        self.connect()
        self.button.state(['pressed'])
        #self.button.configure(style='sunken.TButton')
        self.combobox.state(['disabled'])
        self.connected = True
    else:
      self.disconnect()
      self.button.state(['!pressed'])
      #self.button.configure(style='raised.TButton')
      self.combobox.state(['!disabled'])
      self.connected = False
  
  def connect(self):
    selected_camera = self.combobox.get()
    if selected_camera:
      print(f'Simulating connection to {selected_camera}.')
  
  def disconnect(self):
    print(f'Simulating disconnection from camera.')
  
  def detect_cameras(self):
    print('detecting cameras')
    available_cameras = []
    
    for i in itertools.count(start=0):
      try:
        print(f'trying camera {i}')
        warnings.simplefilter('ignore')
        cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
        warnings.resetwarnings()
        # print(f'Maybe connected.')
        if cap.isOpened():
          print(f'Camera works.')
          available_cameras.append(f'Camera {i}')
          cap.release()
        else:
          cap.release()
          break
      except:
        cap.release()
        break
    
    if not available_cameras:
      available_cameras.append("No cameras found")
      
    self.combobox['values'] = available_cameras

    self.combobox.set(available_cameras[0])

    print('done detecting cameras')
    

def print_choice(combobox):
  selected_camera = combobox.get()
  print(f"selected camera: {selected_camera}")

if __name__ == "__main__":
  app = tk.Tk()
  app.title('Camera Selector test')
  
  cam = CameraSelector(app)
  cam.pack()
  cam.combobox.bind("<<ComboboxSelected>>", lambda arg: print_choice(cam.combobox))
  app.mainloop()
