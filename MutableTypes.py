import operator

# === Base class for shared logic ===

class MutableBase:
    TYPE = object  # to be overridden by subclasses

    def __init__(self, value):
        self._value = [self.TYPE(value)]

    def get(self):
        return self._value[0]

    def set(self, value):
        self._value[0] = self.TYPE(value)

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.get())})"

    def __str__(self):
        return str(self.get())

    def __format__(self, format_spec):
        return format(self.get(), format_spec)

    def __hash__(self):
        return hash(self.get())

    # Comparisons
    def __compare_op(opname):
        def op(self, other):
            return getattr(operator, opname)(self.get(), other)
        return op

    __eq__ = __compare_op('eq')
    __ne__ = __compare_op('ne')
    __lt__ = __compare_op('lt')
    __le__ = __compare_op('le')
    __gt__ = __compare_op('gt')
    __ge__ = __compare_op('ge')


# === MutableInt ===

class MutableInt(MutableBase):
    TYPE = int

    def __int__(self):
        return self.get()

    def __binary_op(opname):
        def op(self, other):
            return MutableInt(getattr(operator, opname)(self.get(), int(other)))
        return op

    def __inplace_op(opname):
        def op(self, other):
            self._value[0] = getattr(operator, opname)(self.get(), int(other))
            return self
        return op

    __add__ = __binary_op('add')
    __sub__ = __binary_op('sub')
    __mul__ = __binary_op('mul')
    __floordiv__ = __binary_op('floordiv')
    __truediv__ = __binary_op('truediv')
    __mod__ = __binary_op('mod')
    __pow__ = __binary_op('pow')

    __iadd__ = __inplace_op('add')
    __isub__ = __inplace_op('sub')
    __imul__ = __inplace_op('mul')
    __ifloordiv__ = __inplace_op('floordiv')
    __itruediv__ = __inplace_op('truediv')
    __imod__ = __inplace_op('mod')
    __ipow__ = __inplace_op('pow')

    def __neg__(self):
        return MutableInt(-self.get())

    def __abs__(self):
        return MutableInt(abs(self.get()))


# === MutableFloat ===

class MutableFloat(MutableBase):
    TYPE = float

    def __float__(self):
        return self.get()

    def __binary_op(opname):
        def op(self, other):
            return MutableFloat(getattr(operator, opname)(self.get(), float(other)))
        return op

    def __inplace_op(opname):
        def op(self, other):
            self._value[0] = getattr(operator, opname)(self.get(), float(other))
            return self
        return op

    __add__ = __binary_op('add')
    __sub__ = __binary_op('sub')
    __mul__ = __binary_op('mul')
    __floordiv__ = __binary_op('floordiv')
    __truediv__ = __binary_op('truediv')
    __mod__ = __binary_op('mod')
    __pow__ = __binary_op('pow')

    __iadd__ = __inplace_op('add')
    __isub__ = __inplace_op('sub')
    __imul__ = __inplace_op('mul')
    __ifloordiv__ = __inplace_op('floordiv')
    __itruediv__ = __inplace_op('truediv')
    __imod__ = __inplace_op('mod')
    __ipow__ = __inplace_op('pow')

    def __neg__(self):
        return MutableFloat(-self.get())

    def __abs__(self):
        return MutableFloat(abs(self.get()))


# === MutableStr ===

class MutableStr(MutableBase):
    TYPE = str

    def __len__(self):
        return len(self.get())

    def __getitem__(self, key):
        return self.get()[key]

    def __add__(self, other):
        return MutableStr(self.get() + str(other))

    def __iadd__(self, other):
        self._value[0] += str(other)
        return self

    def upper(self):
        return MutableStr(self.get().upper())

    def lower(self):
        return MutableStr(self.get().lower())

    def capitalize(self):
        return MutableStr(self.get().capitalize())

    def split(self, sep=None):
        return self.get().split(sep)

    def replace(self, old, new):
        return MutableStr(self.get().replace(old, new))


# === MutableBool ===

class MutableBool(MutableBase):
    TYPE = bool

    def __bool__(self):
        return self.get()

    def toggle(self):
        self._value[0] = not self._value[0]

    def __and__(self, other):
        return MutableBool(self.get() and bool(other))

    def __or__(self, other):
        return MutableBool(self.get() or bool(other))

    def __invert__(self):
        return MutableBool(not self.get())

    def __iand__(self, other):
        self._value[0] = self.get() and bool(other)
        return self

    def __ior__(self, other):
        self._value[0] = self.get() or bool(other)
        return self
