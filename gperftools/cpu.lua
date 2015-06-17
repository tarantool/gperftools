-- gperftools.cpu

local ffi = require('ffi')

local status, profiler = pcall(ffi.load, 'profiler')
if not status then
    error('Failed to load libprofiler. Please install gperftools!')
end

ffi.cdef[[
    int ProfilerStart(const char* fname);
    void ProfilerStop();
    void ProfilerFlush();
]]

local function start(filename)
    if filename == nil then
        error("Usage: cpu.start(filename)")
    end
    if profiler.ProfilerStart(filename) ~= 0 then
        return true
    else
        return nil
    end
end

local function stop()
    profiler.ProfilerStop()
end

local function flush()
    profiler.ProfilerFlush()
end

return {
    start = start;
    stop = stop;
    flush = flush;
}
