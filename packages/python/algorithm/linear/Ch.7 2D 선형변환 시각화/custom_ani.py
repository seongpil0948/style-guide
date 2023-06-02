from scipy import linalg
import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from skimage import io as imgio
import os.path

def tsvd_frame(i,U, s, VT, mn, sh, fig, title):
    #global plt
    #plt.axis('off')
    comp_rate =  i*(1+U.shape[0]+VT.shape[1])/mn*100 
    U_t = U[ :, 0:i ]
    s_t = s[ 0:i ]
    V_t = VT[ 0:i, : ]    
    # reconstruction
    recon_img =  U_t * s_t @ V_t 
    # add dummy date for text
    #print(recon_img.shape)
    dummy_arr = np.ones((int(recon_img.shape[0]*0.2),recon_img.shape[1]))
    recon_img = np.vstack((dummy_arr,recon_img))
    # imshow is slow, use set_array
    sh.set_array(recon_img)
    # text update
    title.set_text(u"t = %i, compressed (%%) = %.2f"%(i,comp_rate))
    # save each frame
    fig.savefig("svd_out/tsvd "+str(i)+".jpg")
    return sh, title,

def tsvd_img_ani(f_name,reverse=False,speed=5):
    # read image as gray
    imgmat = imgio.imread(f_name, as_gray=True)
    # svd
    U, s, VT = linalg.svd(imgmat)
    #fig = plt.figure()
    fig, ax = plt.subplots()
    # skimage, gray 0 to 1
    dummy_arr = np.ones((int(imgmat.shape[0]*0.2),imgmat.shape[1]))
    recon_img = np.vstack((dummy_arr,imgmat))
    sh = plt.imshow(recon_img, cmap='gray', vmin=0, vmax=1)
    plt.axis('off')
    ax.set_aspect('equal', 'box')
    # for text
    ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8], facecolor='#cfd98c')
    title = ax1.text(0.5,0.9, "original", bbox={'facecolor':'w', 'alpha':0.0, 'pad':1},
                transform=ax.transAxes, ha="center")
    ax1.axis('off')
    ax1.set_aspect('equal', 'box')
    
    # save foler set
    current_directory = os.getcwd()
    save_directory = os.path.join(current_directory, 'svd_out')
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    fig.savefig("svd_out/tsvd_original.jpg")
    t_max = len(s)
    mn = imgmat.shape[0]*imgmat.shape[1]
    if reverse:
        ani = animation.FuncAnimation(fig, tsvd_frame, fargs=(U, s, VT, mn, sh, fig, title)
            , frames=np.arange(t_max, 0, -1), interval=1*speed, blit=True, repeat_delay=500)
    else:
        ani = animation.FuncAnimation(fig, tsvd_frame, fargs=(U, s, VT, mn, sh, fig, title)
            , frames=np.arange(1, t_max), interval=1*speed, blit=True, repeat_delay=500)
    # if you install imagemagick, then you can save this animation as gif file
    #ani.save('test.gif', dpi=100, writer='imagemagick')
    plt.show()

def lin_tran_ani(lin_tran,xlim,ylim):
    # color dots [-1,-1] to [1,1]
    def colorizer(x, y):
        if y<=0.5:
            r = 1
            g = (0.5+y)
        else:
            r = 1.5-y
            g = 1
        b = x
        return (r, g, b)
    # Create a grid of points in x-y space 
    xvals = np.linspace(0, 1, 6)
    yvals = np.linspace(0, 1, 6)
    xygrid = np.column_stack([[x, y] for x in xvals for y in yvals])

    # Apply linear transform
    uvgrid = lin_tran @ xygrid

    current_directory = os.getcwd()
    save_directory = os.path.join(current_directory, 'lin_trans_out')
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # Map grid coordinates to colors
    colors = list(map(colorizer, xygrid[0], xygrid[1]))
    last_frame = 50
    fig, ax = plt.subplots()
    im = ax.scatter([], [], edgecolor="black")
    ax.set_aspect('equal', 'box')
    def step_animation(i,last_frame,ax):
        ax.clear()
        plt.grid(True,linestyle='--',zorder=0)
        
        ax.axis([xlim[0], xlim[1], ylim[0], ylim[1]])
        # interpolation
        xx = xygrid[0]+ (uvgrid[0]-xygrid[0])*i/last_frame
        yy = xygrid[1]+ (uvgrid[1]-xygrid[1])*i/last_frame
        ax.scatter(xx,yy,c=colors,edgecolor="black",zorder=10)
        if i == 0:
            fig.savefig('trans_before.jpg')
        if i == last_frame:
            fig.savefig('trans_after.jpg')
    ani = animation.FuncAnimation(fig, step_animation, frames=np.arange(0, last_frame+1), 
          fargs=(last_frame,ax), interval=1, blit=False, repeat_delay=500)
    #ani.save('b.gif', dpi=100, writer='imagemagick')
    plt.show()
