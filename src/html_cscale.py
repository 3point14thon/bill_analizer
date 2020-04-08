def c_scale(num_val, c_max=255):
    c_value = num_val*c_max
    return (c_max - c_value, c_value, 0, 0.2)
