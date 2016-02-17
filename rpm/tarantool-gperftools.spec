Name: tarantool-gperftools
Version: 1.0.0
Release: 1%{?dist}
Summary: Lua bindings for gperftools CPU Profiler
Group: Applications/Databases
License: BSD
URL: https://github.com/tarantool/tarantool-gperftools
Source0: https://github.com/tarantool/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: tarantool >= 1.6.8.0
BuildRequires: gperftools-devel
BuildRequires: /usr/bin/prove
Requires: tarantool >= 1.6.8.0
Requires: gperftools-devel
%description
Lua bindings for Google Performance Tools CPU Profiler

%prep
%setup -q -n %{name}-%{version}

%check
prove -v ./test/gperftools.test.lua

%install
install -d %{buildroot}%{_datarootdir}/tarantool/gperftools
install -m 0644 gperftools/init.lua %{buildroot}%{_datarootdir}/tarantool/gperftools/
install -m 0644 gperftools/cpu.lua %{buildroot}%{_datarootdir}/tarantool/gperftools/

%files
%{_datarootdir}/tarantool/gperftools/init.lua
%{_datarootdir}/tarantool/gperftools/cpu.lua

%changelog
* Wed Jun 17 2015 Roman Tsisyk <roman@tarantool.org> 1.0.0-1
- Initial version of the RPM spec
