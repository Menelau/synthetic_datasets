Synthetic datasets Generation
=============================
This project contains the code to generate synthetic classification datasets. They can be useful as illustrative examples to
analyze the performance of certain algorithms.

Currently the following datasets are available

- P2 dataset [1]_
- Circle square [2]_
- Banana [3]_
- Banana 2 [4]_

We also provide functions to plot the decision boundary of classification algorithms.

Installation:
--------------
The package can be installed using pip:

.. code-block:: bash

    pip install git+https://github.com/Menelau/synthetic_datasets

Dependencies:
-------------
The code is tested to work with Python 3.5 and 3.6. The dependency requirements is only: numpy

matplotlib and scikit-learn are only needed to run the different examples.

* numpy
* matplotlib (only for plotting the data)
* scikit-learn (required only to run the examples)

These dependencies are automatically installed using the pip commands above.

Examples:
---------
In this example we plot the P2 dataset with its decision border.

.. code-block:: python

    import matplotlib.pyplot as plt
    from plot_datasets import plot_decision_P2, plot_dataset
    from synthetic_datasets import generate_p2

    X, y = generate_p2([1000, 1000])
    title = ('P2 Dataset')
    ax = plot_dataset(X, y, title=title)
    plot_decision_P2(ax)

    plt.savefig('ExampleP2.pdf', format='pdf')
    plt.show()

.. figure:: ExampleP2.png

In this example we plot the four datasets as well as the decision border of a trained Support Vector Machine (SVM).

.. code-block:: python

    from plot_datasets import plot_dataset, plot_classifier_decision
    from synthetic_datasets import generate_p2, generate_circle_square, generate_banana, generate_banana2
    import matplotlib.pyplot as plt
    import numpy as np
    from sklearn.svm import SVC
    from sklearn.model_selection import train_test_split

    # Set-up 2x2 grid for plotting.
    fig, sub = plt.subplots(2, 2)
    plt.subplots_adjust(wspace=0.4, hspace=0.4)

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
        plot_classifier_decision(ax, svm, X)
        plot_dataset(X, y, ax, title)
        ax.set_xlim(np.min(X[:, 0]), np.max(X[:, 0]))
        ax.set_ylim(np.min(X[:, 1]), np.max(X[:, 1]))

    plt.savefig('Example.pdf', format='pdf')
    plt.show()

.. figure:: ExampleSubplots.png


References
----------
.. [1] :G. Valentini, An experimental bias-variance analysis of svm ensembles based on resampling techniques, IEEE Transactions on Systems, Man, and Cybernetics, Part B 35 (2005) 1252–1271.

.. [2] : P. Henniges, E. Granger, R. Sabourin, Factors of overtraining with fuzzy artmap neural networks, International Joint Conference on Neural Networks (2005) 1075–1080.

.. [3] : R.P.W. Duin, P. Juszczak, D.de Ridder, P. Paclik, E. Pekalska, D.M.Tax, Prtools, a matlab toolbox for pattern recognition, 2004. URL 〈http://www.prtools.org〉.

.. [4] : Kuncheva, Ludmila I. Combining pattern classifiers: methods and algorithms. John Wiley & Sons, 2004.
