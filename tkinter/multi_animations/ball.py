class Ball:
    def __init__(self, canvas, x, y, diameter, xVelocity, yVelocity, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter, diameter, fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        coords = self.canvas.coords(self.image)
        print(coords)
        if(coords[2]>=(self.canvas.winfo_width())) or coords[0]<0:
            self.xVelocity = -self.xVelocity
        if(coords[3]>=(self.canvas.winfo_height())) or coords[1]<0:
            self.yVelocity = -self.yVelocity
        self.canvas.move(self.image, self.xVelocity, self.yVelocity)

