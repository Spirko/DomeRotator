import tkinter as tk
import tkinter.ttk as ttk
import cv2
import PIL.Image as Image
import PIL.ImageTk as ImageTk

class CameraDisplay(tk.Frame):
  def __init__(self, master=None, camera_index=None, **kwargs):
    super().__init__(master, **kwargs)
    
    self.camera_index = camera_index
    
    # self.pack(fill=tk.BOTH, expand=True)
    
    # The image goes into a Label.
    self.video_label = tk.Label(self)
    self.video_label.pack(fill=tk.BOTH, expand=True)


  def connect(camera_index=None):
    if self.cap is not None and self.cap.isOpened():
      self.cap.release()
      
    self.camera_index = camera_index
    if camera_index is not None:
      print(f'Connecting to camera {self.camera_index}')  
      self.cap = cv2.VideoCapture(self.camera_index)
      self.update_frame()
    
    self.cap = cv2.VideoCapture(self.camera_index)
  
  def update_frame(self):
    ret, frame = self.cap.read()
    if ret:
      # Convert color order
      frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      
      img = Image.fromarray(frame)
      imgtk = ImageTk.PhotoImage(image=img)
      
      self.video_label.imgtk = imgtk
      self.video_label.configure(image=imgtk)
      
      self.master.after(10, self.update_frame)
  
    
  def __del__(self):
    if self.cap.isOpened():
      self.cap.release()
      
if __name__ == "__main__":
  app = tk.Tk()
  app.title('Camera Display Test')
  app.geometry('800x600')
  frm = CameraDisplay(master=app)
  frm.pack(fill=tk.BOTH, expand=True)
  app.mainloop()
