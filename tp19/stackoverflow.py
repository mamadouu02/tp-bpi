#!/usr/bin/env python3

"""Mystery code for recursivity."""

def mystery_function(first, second):
    """a mystery function"""
    print("mystery_function called with first =", first,
          "and second =", second)
    mystery_function(first + 1, "first")
    mystery_function(first + 1, "second")

def main():
    """Program's entry point."""
    mystery_function(23, "init")

if __name__ == "__main__":
    main()
