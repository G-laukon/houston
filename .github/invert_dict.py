def invert_dict(d):
  '''倒转字典映射'''
    inverse = dict()
    for key in d:
        if d[key] in inverse:
            inverse[d[key]].append(key)
        inverse.setdefault(d[key],[key])
    return inverse
