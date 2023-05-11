#!/usr/bin/python3

if __name__ == "__main__":
    """Display names defined by hidden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for fig in names:
        if fig[:2] != "__":
            print(fig)
