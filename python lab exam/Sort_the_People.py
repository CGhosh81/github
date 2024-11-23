def sort_people(names, heights):
    """
    Sorts an array of names based on the corresponding heights in descending order.

    Args:
        names (list): An array of strings representing the names of people.
        heights (list): An array of integers representing the heights of people.

    Returns:
        list: The sorted array of names based on the corresponding heights in descending order.
    """
    height_name_dic = dict(zip(heights, names))
    sorted_heights = sorted(heights, reverse=True)
    sorted_names = [height_name_dic[height] for height in sorted_heights]
    return sorted_names


names = ["Mary", "John", "Emma"]
heights = [165, 180, 155]
sorted_names = sort_people(names, heights)
print(sorted_names)