import numpy as np
import matplotlib.pyplot as plt
import dct

if __name__ == '__main__':
    N = 10
    original_img = np.array([
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,1,1,1,1,0,0,0],
		[0,0,1,1,0,0,1,1,0,0],
		[0,1,1,1,0,0,1,1,1,0],
		[0,1,0,0,1,1,0,0,1,0],
		[0,1,0,0,1,1,0,0,1,0],
		[0,1,1,1,0,0,1,1,1,0],
		[0,0,1,1,0,0,1,1,0,0],
		[0,0,0,1,1,1,1,0,0,0],
		[0,0,0,0,0,0,0,0,0,0]
	])
    base = dct.base(N)
    transed_img = dct.dct(original_img,N)
    resorted_img = dct.idct(transed_img, N)
 
    plt.subplot(1,2,1)
    plt.imshow(original_img,cmap="Greys")
    plt.title("original")
    plt.xticks([])
    plt.subplot(1,2,2)
    plt.imshow(resorted_img,cmap="Greys")
    plt.title("restored")
    plt.xticks([])
    plt.savefig("img/test.png")
'''
    fig, axi = plt.subplots(N,N)
    for i in range(N):
        for j in range(N):
            axi[i,j].imshow(hoge[i,j],cmap="Greys")
            axi[i,j].set_xticklabels([])
            axi[i,j].set_yticklabels([])
    plt.savefig("img/base.png")
'''


