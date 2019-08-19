def unique(lst: list) -> list:
    """Return a list containing only the first occurrence of each distinct
       element in list.  That is, all duplicates are omitted.

    Arguments:
        lst: a list of elements (not modified)
    Returns:
        a new list containing only distinct elements from list

    Examples:
    >>> unique([5])
    [5]
    >>> unique(["b","a","a","b","b","b","a","a"])
    ["b","a"]
    >>> unique([])
    []
    """
    if not isinstance(lst, list):
        raise TypeError(f"{str(lst.__class__)[7:-1]} is not a list")
    out = []
    for elem in lst:
        if elem not in out:
            out.append(elem)
    return out


if __name__ == "__main__":
    """Run the doctests in all methods."""
    import doctest
    doctest.testmod(verbose=True)
