
from cmx import doc

if __name__ == '__main__':
    doc @ """
    # How to debug in pycharm
    
    For Ram
    """
    with doc:
        from pathlib import Path
        import torch
        import numpy as np
        import matplotlib.pyplot as plt

        x = torch.linspace(0, 10, 101)
        y = x.sin()
        y2 = torch.sin(x + 0.5 * np.pi)

    r = doc.table().figure_row()

    plt.plot(x, y)
    r.savefig(f"{Path(__file__).stem}/sin.png", title="$sin(x)$")

    plt.plot(x, y)
    plt.plot(x, y2)
    r.savefig(f"{Path(__file__).stem}/sin_cos.png",
              title=r"$sin(x)$ and $sin(x+\frac 1 2 \pi)$")

    doc.flush()