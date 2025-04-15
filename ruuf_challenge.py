def cuantos_paneles_caben(pside_a, pside_b, roof_side_a, roof_side_b):
    if pside_a <= 0 or pside_b <= 0 or roof_side_a <= 0 or roof_side_b <= 0:
        return 0
    
    if pside_a < pside_b:
        p_height = pside_b
        p_width = pside_a
    else:
        p_height = pside_a
        p_width = pside_b

    if roof_side_a < roof_side_b:
        roof_height = roof_side_b
        roof_width = roof_side_a
    else:
        roof_height = roof_side_a
        roof_width = roof_side_b

    panel_area = p_height * p_width
    nro_paneles = 0

    while p_height <= roof_height and p_width <= roof_width or p_height <= roof_width and p_width <= roof_height:
        if p_height <= roof_height and p_width <= roof_width:
            roof_sub_area = p_height * roof_width
            nro_paneles += roof_sub_area // panel_area
            roof_height = roof_height - p_height
        else:
            roof_sub_area = p_width * roof_width
            nro_paneles += roof_sub_area // panel_area
            roof_height = roof_height - p_width
    return nro_paneles

tests = [
    ((2, 2, 4, 4), 4),
    ((1, 3, 3, 3), 3),
    ((2, 2, 3, 3), 1),
    ((3, 5, 6, 10), 4),
    ((2, 3, 6, 7), 6),
    ((4, 4, 5, 9), 2),
    ((3, 4, 10, 10), 6),
    ((5, 5, 20, 25), 20),
    ((7, 3, 20, 10), 8),
    ((1, 10, 2, 2), 0),
    ((2, 3, 4, 6), 4),
    ((1, 1, 1, 1), 1),
    ((1, 2, 3, 5), 7),
    ((2, 2, 3, 5), 2),
    ((3, 1, 8, 6), 16),
    ((2, 3, 7, 8), 8),
    ((5, 3, 16, 15), 15),
]

for i, ((a, b, h, w), expected) in enumerate(tests, 1):
    result = cuantos_paneles_caben(a, b, h, w)
    print(f"Test {i}: ({a}x{b}) en techo {h}x{w} → {result} (esperado: {expected}) {'✅' if result == expected else '❌'}")