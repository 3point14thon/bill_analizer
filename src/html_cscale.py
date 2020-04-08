def c_scale(num_val, lower_bound = 0 ,upper_bound = 1):
    '''
    Returns a tuble of rgb values and opacity based on the inputs.

    Inputs:
        num _val (float): The value of this instance on the scale.
        lower_bound (float):The lowest value on the numeric scale.
        upper_bound (float): The highest value on the numeric scale.

    Outputs: Tuple of rgba values
    '''
    c_max=255
    c_value = ((num_val-lower_bound)/(upper_bound-lower_bound))*c_max
    return (c_max - c_value, c_value, 0, 0.2)
