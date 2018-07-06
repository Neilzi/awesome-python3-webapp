#! /usr/bin/env python3

mdn = 'handlers'
mod = __import__(mdn, globals(), locals())
for attr in dir(mod):
    print(attr)
    if attr.startswith('_'):
        continue
    fn = getattr(mod, attr)
    if callable(fn):
        print('Callable fun %s ' % fn)

