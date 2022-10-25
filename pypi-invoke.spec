#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9C29BC560041E930 (jeff@bitprophet.org)
#
Name     : pypi-invoke
Version  : 1.7.3
Release  : 30
URL      : https://files.pythonhosted.org/packages/2b/8d/9aec496bbd200589397b4cd6d546576c296465c1bdeb28c1ea1019e75a1f/invoke-1.7.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/2b/8d/9aec496bbd200589397b4cd6d546576c296465c1bdeb28c1ea1019e75a1f/invoke-1.7.3.tar.gz
Source1  : https://files.pythonhosted.org/packages/2b/8d/9aec496bbd200589397b4cd6d546576c296465c1bdeb28c1ea1019e75a1f/invoke-1.7.3.tar.gz.asc
Summary  : Pythonic task execution
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-invoke-bin = %{version}-%{release}
Requires: pypi-invoke-license = %{version}-%{release}
Requires: pypi-invoke-python = %{version}-%{release}
Requires: pypi-invoke-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
|version| |python| |license| |ci| |coverage|

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
%setup -q -n invoke-1.7.3
cd %{_builddir}/invoke-1.7.3
pushd ..
cp -a invoke-1.7.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664807145
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-invoke
cp %{_builddir}/invoke-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-invoke/eadf0675261da2116b63962716fbf09f4cb946ca || :
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
