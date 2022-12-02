#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4
    for n in dir(hidden_4):
        if n[:2] != "__":
            print(n)
#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
