# gperftools - Lua bindings for Google Performance Tools CPU Profiler
[![Build Status](https://travis-ci.org/tarantool/gperftools.png?branch=master)](https://travis-ci.org/tarantool/gperftools)

## Getting Started

### Prerequisites

 * Tarantool 1.5+ or LuaJIT 2.0+
 * libprofiler.so from gperftools package
   - apt-get install libgoogle-perftools4 # Debian/Ubuntu, main repository
   - yum install gperftools-libs # RHEL/CentOS/Fedora, EPEL repository

### Installation

Use package for your distribution from http://tarantool.org/ repository.
You can also use LuaRocks:

``` bash
luarocks install https://raw.githubusercontent.com/tarantool/gperftools/master/gperftools-scm-1.rockspec --local
```

See [tarantool/rocks][TarantoolRocks] for LuaRocks configuration details.

### Usage

Start profiler:

    tarantool> cpuprof = require(‘gperftools.cpu’)
    tarantool> cpuprof.start(‘/home/roman/tarantool-on-production.prof’)

Wait some time to get performance metricrs to be collected
(at least couple minutes).

Flush actual results to disk (you can do that multiple times):

    tarantool> cpuprof.flush()

Analize the output (see [documentation][gperftools]):

    pprof --text /usr/bin/tarantool /home/roman/tarantool-on-production.prof

Stop profiling when you don’t need it anymore:

    tarantool> cpuprof.stop()

## See Also

 * [CPU Profiler Documentation][gperftools]
 * [Tarantool][]
 * [Tarantool Rocks][TarantoolRocks]

[gperftools]: http://gperftools.googlecode.com/git/doc/cpuprofile.html
[Tarantool]: http://github.com/tarantool/tarantool
[TarantoolRocks]: https://github.com/tarantool/rocks
