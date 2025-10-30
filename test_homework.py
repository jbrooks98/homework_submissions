def calculate_area(length, width):
    """
    Calculates the area of a rectangle.
    Args:
        length (int/float): The length of the rectangle.
        width (int/float): The width of the rectangle.
    Returns:
        int/float: The area (length * width).
        Raises ValueError: If length or width is negative.
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative.")
    return length * width
