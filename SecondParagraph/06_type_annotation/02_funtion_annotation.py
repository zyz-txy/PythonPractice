def calc(scores:list[int]) -> float:
    #           参数注解       返回值注解
    return sum(scores) / len(scores)

def calc_data(scores: list[int]) -> tuple[int ,int,float]:
    max_v = max(scores)
    min_v = min(scores)
    avg_v = sum(scores) / len(scores)
    return max_v,min_v,avg_v

def circle_area_len(r=0.0) -> tuple[float, float]:
    return round(3.14 * r ** 2,1), round(2 * 3.14 * r,1)

print(circle_area_len(3))


