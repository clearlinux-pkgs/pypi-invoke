#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-invoke
Version  : 2.2.0
Release  : 40
URL      : https://files.pythonhosted.org/packages/f9/42/127e6d792884ab860defc3f4d80a8f9812e48ace584ffc5a346de58cdc6c/invoke-2.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/f9/42/127e6d792884ab860defc3f4d80a8f9812e48ace584ffc5a346de58cdc6c/invoke-2.2.0.tar.gz
Summary  : Pythonic task execution
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-invoke-bin = %{version}-%{release}
Requires: pypi-invoke-license = %{version}-%{release}
Requires: pypi-invoke-python = %{version}-%{release}
Requires: pypi-invoke-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
|version| |python| |license| |ci| |coverage|
.. |version| image:: https://img.shields.io/pypi/v/invoke
:target: https://pypi.org/project/invoke/
:alt: PyPI - Package Version
.. |python| image:: https://img.shields.io/pypi/pyversions/invoke
:target: https://pypi.org/project/invoke/
:alt: PyPI - Python Version
.. |license| image:: https://img.shields.io/pypi/l/invoke
:target: https://github.com/pyinvoke/invoke/blob/main/LICENSE
:alt: PyPI - License
.. |ci| image:: https://img.shields.io/circleci/build/github/pyinvoke/invoke/main
:target: https://app.circleci.com/pipelines/github/pyinvoke/invoke
:alt: CircleCI
.. |coverage| image:: https://img.shields.io/codecov/c/gh/pyinvoke/invoke
:target: https://app.codecov.io/gh/pyinvoke/invoke
:alt: Codecov

%package bin
Summary: bin components for the pypi-invoke package.
Group: Binaries
Requires: pypi-invoke-license = %{version}-%{release}

%description bin
bin components for the pypi-invoke package.


%package license
Summary: license components for the pypi-invoke package.
Group: Default

%description license
license components for the pypi-invoke package.


%package python
Summary: python components for the pypi-invoke package.
Group: Default
Requires: pypi-invoke-python3 = %{version}-%{release}

%description python
python components for the pypi-invoke package.


%package python3
Summary: python3 components for the pypi-invoke package.
Group: Default
Requires: python3-core
Provides: pypi(invoke)

%description python3
python3 components for the pypi-invoke package.


%prep
%setup -q -n invoke-2.2.0
cd %{_builddir}/invoke-2.2.0
pushd ..
cp -a invoke-2.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689260544
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-invoke
cp %{_builddir}/invoke-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-invoke/eadf0675261da2116b63962716fbf09f4cb946ca || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/inv
/usr/bin/invoke

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-invoke/eadf0675261da2116b63962716fbf09f4cb946ca

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
