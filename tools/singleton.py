class LanguageSingleton(type):
    _instances = {}
    
    def __call__(self, *args, **kwargs):
        if lang := kwargs.get("language"):
            if (self, lang) not in self._instances:
                self._instances[self, lang] = super(
                    LanguageSingleton, self
                ).__call__(*args, **kwargs)

            return self._instances[self, lang]
        if self not in self._instances:
            self._instances[self] = super(LanguageSingleton, self).__call__(
                *args, **kwargs
            )

        return self._instances[self]
