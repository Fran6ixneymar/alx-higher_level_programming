#!/usr/bin/python3

if __name__ == "__main__":
    """Display names defined by hidden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for s in names:
        if s[:2] != "__":
            print(s)
