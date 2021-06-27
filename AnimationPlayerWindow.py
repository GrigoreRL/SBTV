import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from PyQt5 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import random
from SBPP.Packages import *
from matplotlib.animation import FuncAnimation
import mpl_toolkits.axes_grid1
import matplotlib.widgets

class Player(FuncAnimation):
### Class taken from Stack Oveflow:
### https://stackoverflow.com/questions/44985966/managing-dynamic-plotting-in-matplotlib-animation-module/44989063#44989063
### Answer by "ImportanceOfBeingErnest": https://stackoverflow.com/users/4124317/importanceofbeingernest
### Question by "LemurPwned":https://stackoverflow.com/users/3588442/lemurpwned
    def __init__(self, fig, func, frames=None, init_func=None, fargs=None,
                 save_count=None, mini=0, maxi=100, pos=(0.125, 0.92), **kwargs):
        self.i = 0
        self.min=mini
        self.max=maxi
        self.runs = True
        self.forwards = True
        self.fig = fig
        self.func = func
        self.setup(pos)
        FuncAnimation.__init__(self,self.fig, self.update, frames=self.play(), 
                                           init_func=init_func, fargs=fargs,
                                           save_count=save_count, **kwargs )    

    def play(self):
        while self.runs:
            self.i = self.i+self.forwards-(not self.forwards)
            if self.i > self.min and self.i < self.max:
                yield self.i
            else:
                self.stop()
                yield self.i

    def start(self):
        self.runs=True
        self.event_source.start()

    def stop(self, event=None):
        self.runs = False
        self.event_source.stop()

    def forward(self, event=None):
        self.forwards = True
        if self.i>self.max:
            self.i = self.max-1
        self.start()
    def backward(self, event=None):
        self.forwards = False
        if self.i<self.min:
            self.i = self.min+1
        self.start()
    def oneforward(self, event=None):
        self.forwards = True
        self.onestep()
    def onebackward(self, event=None):
        self.forwards = False
        self.onestep()

    def onestep(self):
        if self.i > self.min and self.i < self.max:
            self.i = self.i+self.forwards-(not self.forwards)
        elif self.i == self.min and self.forwards:
            self.i+=1
        elif self.i == self.max and not self.forwards:
            self.i-=1
        elif self.i>self.max:
            self.i-=1
        self.func(self.i)
        self.slider.set_val(self.i)
        self.fig.canvas.draw_idle()

    def setup(self, pos):
        playerax = self.fig.add_axes([pos[0],pos[1], 0.64, 0.04])
        divider = mpl_toolkits.axes_grid1.make_axes_locatable(playerax)
        bax = divider.append_axes("right", size="80%", pad=0.05)
        sax = divider.append_axes("right", size="80%", pad=0.05)
        fax = divider.append_axes("right", size="80%", pad=0.05)
        ofax = divider.append_axes("right", size="100%", pad=0.05)
        sliderax = divider.append_axes("right", size="500%", pad=0.07)
        self.button_oneback = matplotlib.widgets.Button(playerax, label='$\u29CF$')
        self.button_back = matplotlib.widgets.Button(bax, label='$\u25C0$')
        self.button_stop = matplotlib.widgets.Button(sax, label='$\u25A0$')
        self.button_forward = matplotlib.widgets.Button(fax, label='$\u25B6$')
        self.button_oneforward = matplotlib.widgets.Button(ofax, label='$\u29D0$')
        self.button_oneback.on_clicked(self.onebackward)
        self.button_back.on_clicked(self.backward)
        self.button_stop.on_clicked(self.stop)
        self.button_forward.on_clicked(self.forward)
        self.button_oneforward.on_clicked(self.oneforward)
        self.slider = matplotlib.widgets.Slider(sliderax, '', 
                                                self.min, self.max, valinit=self.i)
        self.slider.on_changed(self.set_pos)

    def set_pos(self,i):
        self.i = int(self.slider.val)
        self.func(self.i)

    def update(self,i):
        self.slider.set_val(i)
        
class Ui_PlayerWindow(QDialog):
    def __init__(self, parent=None,figsize=(10,7.5)):
        super(Ui_PlayerWindow, self).__init__(parent)
        
        # a figure instance to plot on
        self.fig = plt.figure(figsize=figsize)

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.fig)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.button = QPushButton('Plot')
        self.ani = None
        self.button.clicked.connect(self.plot)
        self.animatebutton = QPushButton('Animate')
        self.animatebutton.clicked.connect(self.animate)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        layout.addWidget(self.animatebutton)
        self.setLayout(layout)
        self.setWindowTitle("Plotting Interface")
    def closeEvent(self,event):
    
        if self.ani !=None:
            self.ani.stop()
            self.ani = None
            print("Deleted animation")
        plt.close(self.fig)
        self.qs = None
        self.dqs = None
        self.ts = None
        print("Closed")
        event.accept()
    def set_data(self,qs,dqs,ts = None,frequency = 1):
        self.frequency = frequency
        self.qs = np.array(qs)
        self.dqs = np.array(dqs)
        self.qs=self.qs[::self.frequency]
        self.iterations = np.array([i for i in range(len(self.qs[:,0,0]))])
        self.ts = ts
        self.ts = self.ts[::self.frequency]
        self.n_part = len(self.qs[0,:,0])
    def set_options(self,plot_field = False, plot_grid = True,dimension = '3d',time=False,plot_traj = True
    , particles_to_plot = 'all',interval = 10):
        self.plot_field = plot_field
        self.plot_grid = plot_grid
        self.dimension = dimension
        self.time = time
        self.plot_traj = plot_traj
        self.particles_to_plot = particles_to_plot
        self.interval = interval
    def set_frequency(self,frequency):
        self.frequency = frequency
    def plot(self):
        dataXs = self.qs[:,:,0]
        dataYs = self.qs[:,:,1]
        dataZs = self.qs[:,:,2]
        dataTs = self.ts
       
        self.fig.clear()

        self.frame = self.fig.add_subplot(111,projection='3d')
        self.frame.mouse_init(pan_btn=3,zoom_btn=2,rotate_btn = 1)

        self.canvas.draw()
        self.x = dataXs
        self.y = dataYs
        self.z = dataZs
        #self.frame.grid(self.plot_grid)
        self.frame.set_xlabel("x[m]")
        self.frame.set_ylabel("y[m]")
        self.frame.set_zlabel("z[m]")
        if self.plot_traj:
            for i in range(self.n_part):
                self.frame.plot(self.x[:,i],self.y[:,i],self.z[:,i])
        self.point, = self.frame.plot([],[],[],marker='o', linestyle = 'None',color="crimson", ms=5)
        self.timerText = self.frame.text2D(0.05,0.95,'',transform=self.frame.transAxes)
        self.xs = []
        self.ys=[]
        self.zs = []
        self.canvas.draw()
    def animate(self):
        self.plot()
        self.animatebutton.setEnabled(False)
        self.ani = Player(self.fig, self.update, maxi=len(self.y)-1,interval=self.interval)
    def update(self,i):
        #self.xs.append(self.x[i])
        #self.ys.append(self.y[i])
        #self.zs.append(self.z[i])
        Xpos=[]
        Ypos=[]
        Zpos=[]
        if i>len(self.y)-1:
            i = len(self.y)-1
        for j in range(self.n_part):
            Xpos.append(self.x[i,j])
            Ypos.append(self.y[i,j])
            Zpos.append(self.z[i,j])
        if (i<len(self.y)-1 and i>=0):
            self.timerText.set_text("t={:e}s".format(self.ts[i]))
            
        self.point.set_data_3d(Xpos,Ypos,Zpos)
        

    plt.show()
class Ui_PlayerWindow2D(QDialog):
    def __init__(self,parent = None,figsize=(10,7.5)):
        super(Ui_PlayerWindow2D,self).__init__(parent)
        self.fig = plt.figure(figsize=figsize)
        self.canvas = FigureCanvas(self.fig)
        self.toolbar = NavigationToolbar(self.canvas,self)
        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)
        self.animatebutton = QPushButton('Animate')
        self.animatebutton.clicked.connect(self.animate)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        # set the layout
        self.ani = None
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        layout.addWidget(self.animatebutton)
        self.setLayout(layout)
        self.setWindowTitle("Plotting Interface")
    def closeEvent(self,event):
        if self.ani !=None:
            self.ani.stop()
            self.ani = None
            print("Deleted animation")
        plt.close(self.fig)
        self.qs = None
        self.dqs = None
        self.ts = None
        print("Closed")
        event.accept()
    def set_data(self,qs,dqs,frequency=1,ts=None):
        self.frequency = frequency
        self.xs = np.array(qs)
        self.ys = np.array(dqs)
        self.xs = self.xs[::self.frequency]
        self.ys = self.ys[::self.frequency]
        self.ts = ts
        self.ts = self.ts[::self.frequency]
        self.iterations = np.array([i for i in range(len(self.ts))])
        if np.all(self.ts == self.ys):
            self.plotagT = True
        else:
            self.plotagT = False
        self.n_part = len(self.xs[0,:])
    def set_frequency(self,frequency):
        self.frequency = frequency
    def set_options(self,plot_field = False, plot_grid = True,dimension = '3d',time=False,plot_traj = True
    , particles_to_plot = 'all',axis_labels=('a','b'),interval = 10):
        self.plot_field = plot_field
        self.plot_grid = plot_grid
        self.dimension = dimension
        self.time = time
        self.plot_traj = plot_traj
        self.particles_to_plot = particles_to_plot
        self.axis_labels=axis_labels
        self.interval = interval
    def plot(self):
        self.fig.clear()
        self.frame = self.fig.add_subplot(1,1,1)
        self.canvas.draw()
        self.frame.grid(self.plot_grid)
        self.frame.set_xlabel(self.axis_labels[0])
        self.frame.set_ylabel(self.axis_labels[1])
        print(self.plotagT)
        if self.plot_traj:
            if self.plotagT == True:
                for i in range(self.n_part):
                    self.frame.plot(self.ts,self.xs[:,i])
            else:
                for i in range(self.n_part):
                    self.frame.plot(self.xs[:,i],self.ys[:,i])
        self.point, = self.frame.plot([],[],marker='o', linestyle = 'None',color="crimson", ms=5)
        self.timerText = self.frame.text(0.0,1.0,'',transform=self.frame.transAxes)
        self.canvas.draw()
    def animate(self):
        self.plot()
        self.animatebutton.setEnabled(False)
        self.ani = Player(self.fig, self.update, maxi=len(self.ys)-1,interval=self.interval)
    def update(self,i):
        #self.xs.append(self.x[i])
        #self.ys.append(self.y[i])
        #self.zs.append(self.z[i])
        XPos = []
        YPos = []
        if i>len(self.ys)-1:
            i = len(self.ys)-1
        if self.plotagT == True:
            for j in range(self.n_part):
                XPos.append(self.ts[i])
                YPos.append(self.xs[i,j])
        else:
            for j in range(self.n_part):
                XPos.append(self.xs[i,j])
                YPos.append(self.ys[i,j])
        if (i<len(self.ys)-1 and i>=0):
            self.timerText.set_text("t={:e}s".format(self.ts[i]))
        self.point.set_data(XPos,YPos) 
if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())