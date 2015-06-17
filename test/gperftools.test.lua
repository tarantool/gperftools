#!/usr/bin/env tarantool

package.path = "../?/init.lua;../?.lua;./?/init.lua;./?.lua"

local cpuprof = require('gperftools.cpu')
local fio = require('fio')
local filename = os.tmpname()

require('tap').test('gperftools', function(t)
    t:plan(4)

    t:ok(cpuprof.start(filename), "start")
    t:ok(fio.stat(filename) ~= nil, "file exists")

    cpuprof.flush()
    local st = fio.stat(filename)
    t:ok(st and st.size > 0, "flush")

    cpuprof.stop()
    t:ok(true, "stop")

    fio.unlink(filename)
end)
