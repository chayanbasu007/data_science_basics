
import numpy as np
import matplotlib.pyplot as plt

A = np.array([[4,1],[2,3]],dtype=float)
eigvals,Q = np.linalg.eig(A)
Lambda = np.diag(eigvals)
Qinv = np.linalg.inv(Q)

x = np.array([2.,1.])

x_eig = Qinv @ x
y_eig = Lambda @ x_eig
y = Q @ y_eig

def draw_basis(ax, basis, colors=("purple","orange"), scale=3, label_prefix=""):
    for i,c in enumerate(colors):
        v=basis[:,i]
        ax.quiver(0,0,v[0]*scale,v[1]*scale,angles='xy',scale_units='xy',scale=1,
                  color=c,width=0.01,label=f"{label_prefix}Axis {i+1}")
        ax.text(v[0]*scale*1.05,v[1]*scale*1.05,f"e{i+1}",color=c)

def draw_std(ax):
    ax.axhline(0,color='lightgray'); ax.axvline(0,color='lightgray')
    ax.quiver(0,0,1,0,angles='xy',scale_units='xy',scale=1,color='gray')
    ax.quiver(0,0,0,1,angles='xy',scale_units='xy',scale=1,color='gray')

fig,axs=plt.subplots(1,4,figsize=(20,5))

#1
ax=axs[0]; draw_std(ax)
ax.quiver(0,0,*x,color='red',angles='xy',scale_units='xy',scale=1,width=0.012,label='Original vector x')
ax.set_title("1. Standard Basis")
ax.legend()

#2
ax=axs[1]; draw_std(ax); draw_basis(ax,Q,label_prefix="Eigen ")
ax.quiver(0,0,*x,color='red',angles='xy',scale_units='xy',scale=1,width=0.012,label='Same physical vector')
# projections
for i in range(2):
    v=Q[:,i]
    p=x_eig[i]*v
    ax.plot([0,p[0]],[0,p[1]],'--',color=['purple','orange'][i],alpha=.6)
ax.set_title("2. Change Basis (Q⁻¹)\nEigenvectors become new axes")
ax.legend(fontsize=8)

#3
ax=axs[2]; draw_std(ax); draw_basis(ax,Q,label_prefix="Eigen ")
before=Q@x_eig
after=Q@y_eig
ax.quiver(0,0,*before,color='blue',angles='xy',scale_units='xy',scale=1,width=0.012,label='Before scaling')
ax.quiver(0,0,*after,color='green',angles='xy',scale_units='xy',scale=1,width=0.012,label='After Λ scaling')
ax.set_title("3. Scale Along Eigen Axes (Λ)")
ax.legend(fontsize=8)

#4
ax=axs[3]; draw_std(ax); draw_basis(ax,Q,label_prefix="Eigen ")
ax.quiver(0,0,*x,color='red',alpha=.4,angles='xy',scale_units='xy',scale=1,width=0.01,label='Original')
ax.quiver(0,0,*y,color='darkgreen',angles='xy',scale_units='xy',scale=1,width=0.014,label='Final Ax')
ax.set_title("4. Rotate Back (Q)")
ax.legend(fontsize=8)

for ax in axs:
    ax.set_xlim(-1,8); ax.set_ylim(-1,8)
    ax.set_aspect('equal')
    ax.grid(alpha=.3)

plt.tight_layout()
plt.show()

print("Eigenvalues:",eigvals)
print("Q=\n",Q)
print("Q^-1 x =",x_eig)
print("Lambda(Q^-1x) =",y_eig)
print("Q Lambda Q^-1 x =",y)
