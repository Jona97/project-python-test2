import os

def double(input1: int) -> int:
    """_summary_

    Args:
        input1 (int): _description_

    Returns:
        int: _description_
    """
    return input1 * input1

#result = double(13)
if __name__ == "__main__":
    current_folder = os.listdir()
    print(f"Current folder: {current_folder}")

