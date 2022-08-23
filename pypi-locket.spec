#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-locket
Version  : 1.0.0
Release  : 35
URL      : https://files.pythonhosted.org/packages/2f/83/97b29fe05cb6ae28d2dbd30b81e2e402a3eed5f460c26e9eaa5895ceacf5/locket-1.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/2f/83/97b29fe05cb6ae28d2dbd30b81e2e402a3eed5f460c26e9eaa5895ceacf5/locket-1.0.0.tar.gz
Summary  : File-based locks for Python on Linux and Windows
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-locket-license = %{version}-%{release}
Requires: pypi-locket-python = %{version}-%{release}
Requires: pypi-locket-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
locket.py: File-based locks for Python on Linux and Windows
===========================================================

%package license
Summary: license components for the pypi-locket package.
Group: Default

%description license
license components for the pypi-locket package.


%package python
Summary: python components for the pypi-locket package.
Group: Default
Requires: pypi-locket-python3 = %{version}-%{release}

%description python
python components for the pypi-locket package.


%package python3
Summary: python3 components for the pypi-locket package.
Group: Default
Requires: python3-core
Provides: pypi(locket)

%description python3
python3 components for the pypi-locket package.


%prep
%setup -q -n locket-1.0.0
cd %{_builddir}/locket-1.0.0
pushd ..
cp -a locket-1.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656395345
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-locket
cp %{_builddir}/locket-1.0.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-locket/ee8192d8344dd7db99e21d3f7b2303f4d3ccc143
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-locket/ee8192d8344dd7db99e21d3f7b2303f4d3ccc143

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
