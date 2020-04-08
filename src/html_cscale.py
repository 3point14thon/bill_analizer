def c_scale(num_val, c_max=255):
    '''
    Returns a tuble of rgb values and opacity based on the inputs.

    Inputs:
        num _val (float): The value of this instance on the scale.
        c_max (int): Determins how quickly the scale increases.

    Outputs: Tuple of rgba values
    '''
    c_value = num_val*c_max
    return (c_max - c_value, c_value, 0, 0.2)
