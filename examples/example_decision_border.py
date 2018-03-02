# coding=utf-8

# Author: Rafael Menelau Oliveira e Cruz <rafaelmenelau@gmail.com>
#
# License: MIT

if __name__ == "__main__":
    from syndata.plot_tools import plot_dataset, plot_classifier_decision
    from syndata.synthetic_datasets import generate_p2, generate_circle_square, generate_banana, generate_banana2
    import matplotlib.pyplot as plt
    import numpy as np
    from sklearn.svm import SVC
    from sklearn.model_selection import train_test_split

    # Set-up 2x2 grid for plotting.
    fig, sub = plt.subplots(2, 2)
    plt.subplots_adjust(wspace=0.4, hspace=0.4)
    cmap = plt.cm.RdBu

    X_P2, y_P2 = generate_p2([1000, 1000])
    X_cs, y_cs = generate_circle_square([1000, 1000])
    X_banana, y_banana = generate_banana([1000, 1000])
    X_banana2, y_banana2 = generate_banana2([1000, 1000])
    X_list = list([X_P2, X_cs, X_banana, X_banana2])
    y_list = list([y_P2, y_cs, y_banana, y_banana2])

    # title for the plots
    titles = ('P2 Dataset',
              'Circle Square Dataset',
              'Banana Dataset',
              'Banana 2 Dataset')

    for X, y, title, ax in zip(X_list, y_list, titles, sub.flatten()):

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
        svm = SVC()
        svm.fit(X_train, y_train)
        plot_classifier_decision(ax, svm, X_train, cmap=cmap)
        plot_dataset(X_test, y_test, ax, title, cmap=cmap)
        ax.set_xlim(np.min(X[:, 0]), np.max(X[:, 0]))
        ax.set_ylim(np.min(X[:, 1]), np.max(X[:, 1]))

    plt.show()
