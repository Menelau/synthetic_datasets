# coding=utf-8

# Author: Rafael Menelau Oliveira e Cruz <rafaelmenelau@gmail.com>
#
# License: MIT

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from syndata.plot_tools import plot_decision_P2, plot_dataset
    from syndata.synthetic_datasets import generate_p2

    X, y = generate_p2([1000, 1000])
    title = ('P2 Dataset')
    ax = plot_dataset(X, y, title=title, cmap=plt.cm.RdBu)
    plot_decision_P2(ax)

    plt.show()
