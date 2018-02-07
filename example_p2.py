if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from plot_tools import plot_decision_P2, plot_dataset
    from synthetic_datasets import generate_p2

    X, y = generate_p2([1000, 1000])
    title = ('P2 Dataset')
    ax = plot_dataset(X, y, title=title)
    plot_decision_P2(ax)

    plt.savefig('ExampleP2.png', format='png')
    plt.show()
