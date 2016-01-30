# copyright 2016 Apache 2 sddekit authors

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

# kvl {{{
class KVL(object):

    def __init__(self, **kwds):
        self._kvl = [(k, v) for k, v in kwds.items()]

    def __len__(self):
        return len(self._kvl)

    def __setitem__(self, key, value):
        self._kvl.append((key, value))

    def __getitem__(self, key):
        matches = [v for k, v in self._kvl if k==key]
        if matches:
            return matches
        raise KeyError

    @property
    def _map(self):
        map = {}
        for k, v in self._kvl:
            if k not in  map:
                map[k] = []
            map[k].append(v)
        return map

    def __iter__(self):
        return iter(self._map)

    def __reversed__(self):
        return reversed(self._map)

    def __contains__(self, key):
        return any([k==key for k, v in self._kvl])

    def values(self):
        return self._map.values()

    def items(self):
        return self._map.items()

# kvl }}}

def dump(ifname):
    i = ConfigParser(defaults={}, dict_type=KVL, 
                     allow_no_value=True)
    i.read(ifname)
    return i

i = dump('template.ini')

# vim: sw=4 et foldmethod=marker
