import numpy as np
import matplotlib.pyplot as plt


def generate_p2(size_classes):

    n_samples = size_classes * 6
    class_1 = np.zeros((size_classes, 2))
    class_2 = np.zeros((size_classes, 2))
    size_class1 = 0
    size_class2 = 0
    data = np.random.rand(n_samples, 2)
    for x in data:
        if (size_class1 + size_class2) >= size_classes * 2:
            break

        if x[1] > (-0.1 * (x[0] * 10) ** 2 + 0.6 * np.sin(4 * x[0] * 10) + 8.) / 10. and x[1] > (
                (x[0] * 10 - 2) ** 2 + 1) / 10 or \
                x[1] < (2 * np.sin(x[0] * 10) + 5) / 10 and x[1] > ((x[0] * 10 - 2) ** 2 + 1) / 10 or \
                x[1] < (-0.1 * (x[0] * 10) ** 2 + 0.6 * np.sin(4 * x[0] * 10) + 8) / 10 and x[1] < (
                (x[0] * 10 - 2) ** 2 + 1) / 10 and \
                x[1] > (2 * np.sin(x[0] * 10) + 5) / 10 or \
                x[1] > (-0.1 * (x[0] * 10) ** 2 + 0.6 * np.sin(4 * x[0] * 10) + 8) / 10 and x[1] < (
                2 * np.sin(x[0] * 10) + 5) / 10 or \
                x[1] > (((x[0] * 10 - 10) ** 2) / 2 + 7.902) / 10.:

            if size_class1 < size_classes:
                class_1[size_class1] = x
                size_class1 += 1
        elif size_class2 < size_classes:
            class_2[size_class2] = x
            size_class2 += 1

    y = np.hstack((np.zeros(size_class1), np.ones(size_class2)))
    X = np.vstack((class_1, class_2))

    return X, y


def gen_circle_square(size_classes):

    n_samples = size_classes * 2
    class_1 = np.zeros((size_classes, 2))
    class_2 = np.zeros((size_classes, 2))
    size_class1 = 0
    size_class2 = 0
    data = np.random.rand(n_samples*10, 2)
    r = 0.398942
    for x in data:
        test_class = ((x[0] - 0.5) ** 2) + ((x[1] - 0.5) ** 2)
        if test_class < (r ** 2):
            if size_class1 < size_classes:
                class_1[size_class1] = x
                size_class1 += 1

        elif size_class2 < size_classes:
            class_2[size_class2] = x
            size_class2 += 1

        if size_class2 + size_class1 > n_samples:
            break

    y = np.hstack((np.zeros(size_class1), np.ones(size_class2)))
    X = np.vstack((class_1, class_2))

    return X, y


def plot_dataset(X, y, title=None):
    plt.figure(figsize=(8, 8))
    plt.scatter(X[:, 0], X[:, 1], marker='o', c=y, s=25, edgecolor='k')
    plt.xlim((0, 1))
    plt.ylim((0, 1))
    if title is not None:
        plt.title(title)
    plt.show()


def make_meshgrid(x, y, h=.02):
    """Create a mesh of points to plot in

    Parameters
    ----------
    x: data to base x-axis meshgrid on
    y: data to base y-axis meshgrid on
    h: stepsize for meshgrid, optional

    Returns
    -------
    xx, yy : ndarray
    """
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    return xx, yy


def plot_decision_border():
    fig, sub = plt.subplots(2, 2)
    plt.subplots_adjust(wspace=0.4, hspace=0.4)
    xx, yy = make_meshgrid(X[:, 0], X[:, 1])


if __name__ == "__main__":
    size_classes = 1000
    X, y = generate_p2(size_classes)
    plot_dataset(X, y, 'P2 Dataset')
