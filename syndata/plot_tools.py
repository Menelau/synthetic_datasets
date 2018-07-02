# coding=utf-8

# Author: Rafael Menelau Oliveira e Cruz <rafaelmenelau@gmail.com>
#
# License: MIT

import matplotlib.pyplot as plt
import numpy as np


def plot_decision_P2(ax=None):
    """Plot the decision of the P2 dataset.

    Parameters
    ----------
    ax: The axis used to plot the decision boundaries.

    """
    if ax is None:
        ax = plt.gca()
    x = np.linspace(0, 1, 1000)
    exp1 = (2*np.sin(x*10) + 5)/10
    exp2 = ((x*10-2)**2 + 1)/10
    exp3 = (-0.1*(10*x)**2 + 0.6*np.sin(4*x*10) + 8)/10
    exp4 = (((x*10-10)**2)/2 + 7.902)/10
    ax.plot(x, exp1, linewidth=3.0, color='k')
    ax.plot(x, exp2, linewidth=3.0, color='k')
    ax.plot(x, exp3, linewidth=3.0, color='k')
    ax.plot(x, exp4, linewidth=3.0, color='k')
    ax.set_xlim((0, 1))
    ax.set_ylim((0, 1))


def plot_decision_circle_square():
    """Plot the decision of the circle square dataset.

    Parameters
    ----------
    ax: The axis used to plot the decision boundaries.

    """
    r = 0.398942
    circle = plt.Circle((0.5, 0.5), r)
    return circle


def plot_dataset(X, y, ax=None, title=None, **params):
    """Plot a two dimensional dataset.

    Parameters
    ----------
    X : The data to be plotted

    y : Class label associated with each data point

    ax : Axis used to plot the data (Default = None)

    title : Title of the plot (Default = None)

    """
    if ax is None:
        ax = plt.gca()
    ax.scatter(X[:, 0], X[:, 1], marker='o', c=y, s=25, edgecolor='k', **params)
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    if title is not None:
        ax.set_title(title)
    return ax


def make_grid(x, y, h=.02):
    """Create a mesh of points to plot in

    Parameters
    ----------
    x: data to base x-axis grid

    y: data to base y-axis grid

    h: float, (Default = 0.02)
       step size to create the grid

    Returns
    -------
    xx, yy : ndarray
    """
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    return xx, yy


def plot_classifier_decision(ax, clf, X, mode='line', **params):
    """Plot the decision border of a trained classifier.

    Parameters
    ----------
    ax : The axis use to plot the decision border

    clf : Classifier used in the plot. The classifier needs to implement the method predict(X) from sklearn

    X : array of shape = [n_samples, 2]
        The classification dataset considered in the plot

    mode : String, (Default = line)
           Weather to plot the decision boundary as a line or as colors

    **params : Other parameters used to change the plot

    Returns
    -------
    xx, yy : ndarray
    """
    xx, yy = make_grid(X[:, 0], X[:, 1])

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    if mode == 'line':
       ax.contour(xx, yy, Z, **params)
    else:
       ax.contourf(xx, yy, Z, **params)
    ax.set_xlim((np.min(X[:, 0]), np.max(X[:, 0])))
    ax.set_ylim((np.min(X[:, 1]), np.max(X[:, 0])))


def plot_classifier_probability_map(ax, clf, X, **params):
    """Plot the decision border of a trained classifier.

    Parameters
    ----------
    ax : The axis use to plot the decision border

    clf : Classifier used in the plot. The classifier needs to implement the method predict(X) from sklearn

    X : array of shape = [n_samples, 2]
        The classification dataset considered in the plot

    **params : Other parameters used to change the plot

    Returns
    -------
    xx, yy : ndarray
    """
    xx, yy = make_grid(X[:, 0], X[:, 1])

    if hasattr(clf, "decision_function"):
        Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
    else:
        Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]

    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, alpha=0.8, **params)
    ax.set_xlim((np.min(X[:, 0]), np.max(X[:, 0])))
    ax.set_ylim((np.min(X[:, 1]), np.max(X[:, 0])))
