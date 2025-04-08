def cuantos_paneles(p_height, p_width, roof_height, roof_width):
    if p_height <= roof_height and p_width <= roof_width or p_height <= roof_width and p_width <= roof_height:
        panel_area = p_height * p_width
        roof_area = roof_height * roof_width
        return roof_area // panel_area
    return 0
    

print(cuantos_paneles(2, 2, 1, 10))