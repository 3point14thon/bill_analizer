def mk_color_span(vals, txts, lower_bound=0, upper_bound=1):
    span_start = '<span style="background-color:rgba'
    color_doc = [span_start +
                 f'{c_scale(val, lower_bound, upper_bound)};">' +
                 str(txt) +
                 '</span>' for txt, val in zip(txts, vals)]
    return ''.join(color_doc)


def c_scale(num_val, lower_bound=0, upper_bound=1):
    '''
    Returns a tuble of rgb values and opacity based on the inputs.

    Inputs:
        num _val (float): The value of this instance on the scale.
        lower_bound (float):The lowest value on the numeric scale.
        upper_bound (float): The highest value on the numeric scale.

    Outputs: Tuple of rgba values
    '''
    c_max = 255
    c_value = ((num_val-lower_bound)/(upper_bound-lower_bound))*c_max
    return (c_max - c_value, c_value, 0, 0.2)
