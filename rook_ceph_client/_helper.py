import logging
try:
    from typing import List, Dict, Any, Optional
except ImportError:
    pass

logger = logging.getLogger(__name__)

# Tricking mypy to think `_omit`'s type is NoneType
# To make us not add things like `Union[Optional[str], OmitType]`
NoneType = type(None)
_omit = None  # type: NoneType
_omit = object()  # type: ignore


def _property_from_json(data, breadcrumb, name, py_name, typ, required, nullable):
    if not required and name not in data:
        return _omit
    obj = data[name]
    if nullable and obj is None:
        return obj
    if issubclass(typ, CrdObject) or issubclass(typ, CrdObjectList):
        return typ.from_json(obj, breadcrumb + '.' + name)
    return obj


class CrdObject(object):
    _properties = []  # type: List

    def _property_impl(self, name):
        obj = getattr(self, '_' + name)
        if obj is _omit:
            raise AttributeError(name + ' not found')
        return obj

    def _property_to_json(self, name, py_name, typ, required, nullable):
        obj = getattr(self, '_' + py_name)
        if issubclass(typ, CrdObject) or issubclass(typ, CrdObjectList):
            if nullable and obj is None:
                return obj
            if not required and obj is _omit:
                return obj
            return obj.to_json()
        else:
            return obj

    def to_json(self):
        # type: () -> Dict
        res = {p[0]: self._property_to_json(*p) for p in self._properties}
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data, breadcrumb=''):
        try:
            sanitized = {
                p[1]: _property_from_json(data, breadcrumb, *p) for p in cls._properties
            }
            return cls(**sanitized)
        except (TypeError, AttributeError):
            logger.exception(breadcrumb)


class CrdObjectList(list):
    _items_type = None  # type: Any

    def to_json(self):
        # type: () -> List
        return [e.to_json() for e in self]

    @classmethod
    def from_json(cls, data, breadcrumb=''):
        return cls(cls._items_type.from_json(e, breadcrumb + '[]') for e in data)
