import common

def flatten(obj):
    for el in obj:
        if hasattr(el, "__iter__") and not isinstance(el, basestring):
            for i in flatten(el):
                yield i
        else:
            yield el


def Iterator(obj, group, name, is_list):
    f = list(flatten(obj))
    if len(f)%group:
        if is_list:
            m = "Extra items in %s list (expect multiples of %s)."
        else:
            m = "Too few items in %s list (expect %s)."
        raise common.Exception(m%(name, group))
    for i in range(0, len(f), group):
        yield tuple(f[i:i+group])
    
