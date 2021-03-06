from tkinter import *
from tkinter.ttk import * 
  
class PING: 
    def __init__(self, master = None): 
        self.master = master
        self.canvas = Canvas(master)
        self.newgame()

    def newgame(self):
        self.x = 1.5
        self.y = 1.5
        self.job = None
  
        self.rectangle_bar1 = self.canvas.create_rectangle(0, 0, 100, 5, fill = "black") 
        self.rectangle_bar2 = self.canvas.create_rectangle(275, 263, 375, 267, fill = "black") 
        self.rectangle = self.canvas.create_rectangle(15, 15, 35, 35, fill = "orange") 
        self.canvas.pack() 
        self.movement()

    def game_over(self):
        if self.job is not None:
            self.canvas.after_cancel(self.job)
            self.job = None
      
    def movement(self): 
        a,b,c,d = self.canvas.coords(self.rectangle)
        self.check_bound(a,b,c,d)
        self.canvas.move(self.rectangle, self.x, self.y)
        self.x += self.x * 0.001
        self.y += self.x * 0.001

        self.job = self.canvas.after(25 , self.movement) 

    def bar1left(self, event): 
        a1,b1,c1,d1 = self.canvas.coords(self.rectangle_bar1)
        if not a1 < 0:
            self.canvas.move(self.rectangle_bar1, -10, 0) 
      
    def bar1right(self, event): 
        a1,b1,c1,d1 = self.canvas.coords(self.rectangle_bar1)
        if not c1 > 375:
            self.canvas.move(self.rectangle_bar1, 10, 0) 

    def bar2left(self, event): 
        a2,b2,c2,d2 = self.canvas.coords(self.rectangle_bar2)
        if not a2 < 0:
            self.canvas.move(self.rectangle_bar2, -10, 0) 
      
    def bar2right(self, event): 
        a2,b2,c2,d2 = self.canvas.coords(self.rectangle_bar2)
        if not c2 > 375:
            self.canvas.move(self.rectangle_bar2, 10, 0) 
    
    def space(self, event):
        self.endgame()
        self.canvas.delete("all")
        self.newgame() 

    def check_bound(self,x1,y1,x2,y2):
        a1,b1,c1,d1 = self.canvas.coords(self.rectangle_bar1)
        a2,b2,c2,d2 = self.canvas.coords(self.rectangle_bar2)
        if x1 < 0 or x2 > 375:
            self.x = self.x * -1
        if y1 < 7:
            if x1 + 19 > a1 and x1 -19 < c1:
                self.y = self.y * -1
            else: 
                self.endgame('2')
        elif y2 > 260:
            if x1 + 19 > a2 and x2 - 19 < c2:
                self.y = self.y * -1
            else: 
                self.endgame('1')
    
    def endgame(self, winner=None):
        self.x = 0
        self.y = 0
        if winner:
            canvas_txt = self.canvas.create_text(180, 100)
            self.canvas.itemconfig(canvas_txt, text="Game Over!\nPlayer %s Wins!\n\nPress 'Space' to retry" % winner)
        self.game_over()

if __name__ == "__main__": 
  
    master = Tk()
    pong = PING(master) 
  
    master.bind("<KeyPress-Left>", lambda e: pong.bar2left(e)) 
    master.bind("<KeyPress-a>", lambda e: pong.bar1left(e)) 
    master.bind("<KeyPress-A>", lambda e: pong.bar1left(e)) 
    master.bind("<KeyPress-Right>", lambda e: pong.bar2right(e)) 
    master.bind("<KeyPress-d>", lambda e: pong.bar1right(e)) 
    master.bind("<KeyPress-D>", lambda e: pong.bar1right(e)) 
    master.bind("<KeyPress-space>", lambda e: pong.space(e)) 
       
    mainloop()