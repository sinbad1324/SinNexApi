def get_data(data):
    default_curves = {
        "linear": [{"X": 0, "Y": 0}, {"X": 0, "Y": 0}, {"X": 1, "Y": 1}, {"X": 1, "Y": 1}],
        "inSine": [{"X": 0, "Y": 0}, {"X": 0.12, "Y": 0}, {"X": 0.39, "Y": 0}, {"X": 1, "Y": 1}],
        "outSine": [{"X": 0, "Y": 0}, {"X": 0.61, "Y": 1}, {"X": 0.88, "Y": 1}, {"X": 1, "Y": 1}],
        "inOutSine": [{"X": 0, "Y": 0}, {"X": 0.37, "Y": 0}, {"X": 0.63, "Y": 1}, {"X": 1, "Y": 1}],
        "inCubic": [{"X": 0, "Y": 0}, {"X": 0.32, "Y": 0}, {"X": 0.67, "Y": 0}, {"X": 1, "Y": 1}],
        "outCubic": [{"X": 0, "Y": 0}, {"X": 0.33, "Y": 1}, {"X": 0.68, "Y": 1}, {"X": 1, "Y": 1}],
        "inOutCubic": [{"X": 0, "Y": 0}, {"X": 0.65, "Y": 0}, {"X": 0.35, "Y": 1}, {"X": 1, "Y": 1}],
        "inQuad": [{"X": 0, "Y": 0}, {"X": 0.55, "Y": 0.085}, {"X": 0.68, "Y": 0.53}, {"X": 1, "Y": 1}],
        "outQuad": [{"X": 0, "Y": 0}, {"X": 0.25, "Y": 0.46}, {"X": 0.45, "Y": 0.94}, {"X": 1, "Y": 1}],
        "inOutQuad": [{"X": 0, "Y": 0}, {"X": 0.455, "Y": 0.03}, {"X": 0.515, "Y": 0.955}, {"X": 1, "Y": 1}],
        "inQuint": [{"X": 0, "Y": 0}, {"X": 0.64, "Y": 0}, {"X": 0.78, "Y": 0}, {"X": 1, "Y": 1}],
        "outQuint": [{"X": 0, "Y": 0}, {"X": 0.22, "Y": 1}, {"X": 0.36, "Y": 1}, {"X": 1, "Y": 1}],
        "inOutQuint": [{"X": 0, "Y": 0}, {"X": 0.83, "Y": 0}, {"X": 0.17, "Y": 1}, {"X": 1, "Y": 1}],
        "inEXpo": [{"X": 0, "Y": 0}, {"X": 0.7, "Y": 0}, {"X": 0.84, "Y": 0}, {"X": 1, "Y": 1}],
        "outEXpo": [{"X": 0, "Y": 0}, {"X": 0.16, "Y": 1}, {"X": 0.3, "Y": 1}, {"X": 1, "Y": 1}],
        "inOutEXpo": [{"X": 0, "Y": 0}, {"X": 0.87, "Y": 0}, {"X": 0.13, "Y": 1}, {"X": 1, "Y": 1}],
        "inElastic": [{"X": 0, "Y": 0}, {"X": 0.42, "Y": 0}, {"X": 0.58, "Y": 0}, {"X": 1, "Y": 1}],
        "outElastic": [{"X": 0, "Y": 0}, {"X": 0.22, "Y": 1}, {"X": 0.58, "Y": 1}, {"X": 1, "Y": 1}],
        "inOutElastic": [{"X": 0, "Y": 0}, {"X": 0.42, "Y": 0}, {"X": 0.58, "Y": 1}, {"X": 1, "Y": 1}],
        "inBack": [{"X": 0, "Y": 0}, {"X": 0.6, "Y": -0.28}, {"X": 0.735, "Y": -0.17}, {"X": 1, "Y": 1}],
        "outBack": [{"X": 0, "Y": 0}, {"X": 0.175, "Y": 1.68}, {"X": 0.36, "Y": 1.54}, {"X": 1, "Y": 1}],
        "inOutBack": [{"X": 0, "Y": 0}, {"X": 0.68, "Y": -0.55}, {"X": 0.735, "Y": 1.55}, {"X": 1, "Y": 1}],
    }

    default_names = [
        "linear",
        "inSine",
        "outSine",
        "inOutSine",
        "inCubic",
        "outCubic",
        "inOutCubic",
        "inQuad",
        "outQuad",
        "inOutQuad",
        "inQuint",
        "outQuint",
        "inOutQuint",
        "inExpo",
        "outExpo",
        "inOutExpo",
        "inElastic",
        "outElastic",
        "inOutElastic",
        "inBack",
        "outBack",
        "inOutBack",
    ]

    if data:
        for i, name in enumerate(data["interpolationName"]):
            if name not in default_names:
                default_names.append(name)
                default_curves[name] = [
                    {"X": 0, "Y": 0},
                    {"X": data["interpolationCurves"][name][0]["X"], "Y": data["interpolationCurves"][name][0]["Y"]},
                    {"X": data["interpolationCurves"][name][1]["X"], "Y": data["interpolationCurves"][name][1]["Y"]},
                    {"X": 1, "Y": 1},
                ]

    return default_names, default_curves

def curve_bezier(x, p0, p1, p2, p3):
    t = 1 - x
    t2 = t * t
    t3 = t2 * t
    x2 = x * x
    x3 = x2 * x
    result_x = (
        t3 * p0["X"] +
        3 * t2 * x * p1["X"] +
        3 * t * x2 * p2["X"] +
        x3 * p3["X"]
    )
    result_y = (
        t3 * p0["Y"] +
        3 * t2 * x * p1["Y"] +
        3 * t * x2 * p2["Y"] +
        x3 * p3["Y"]
    )
    return {"X": result_x, "Y": result_y}


def convert_to_number_sequence(points: list[int], seq: int, ev: float):
    number_sequence = []
    
    if seq > 17:
        seq = 17
    if seq < 2:
        seq = 2
    for i in [x / seq for x in range(seq + 1)]:
        curve_points = curve_bezier(i, points[0], points[1], points[2], points[3])
        new_seq = {
            "time": curve_points["X"],
            "value": curve_points["Y"],
            "ev": ev
        }
        number_sequence.append(new_seq)

    return number_sequence
