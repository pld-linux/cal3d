# TODO: what are the differences between cal3d and imvu-cal3d fork? (both included in tarball)
Summary:	3d character animation library
Summary(hu.UTF-8):	3D karakter animáció könyvtára
Summary(pl.UTF-8):	Biblioteka do trójwymiarowej animacji postaci
Name:		cal3d
Version:	0.120
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/mp3butcher/Cal3D/releases
Source0:	https://github.com/mp3butcher/Cal3D/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8d914c71119a0a988a582c4bc6a24b53
Patch0:		%{name}-fixtag.patch
Patch1:		%{name}-cpp.patch
URL:		https://mp3butcher.github.io/Cal3D/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd31-sgml
BuildRequires:	docbook-utils
BuildRequires:	doxygen
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	sed >= 4.0
BuildRequires:	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cal3d is a 3d character animation library written in C++ in a
platform-/graphic API-independent way.

%description -l hu.UTF-8
Cal3d egy C++-ban íródott 3d karakter-animációs könyvtár
platform/grafikus API-független módon.

%description -l pl.UTF-8
Cal3d jest biblioteką do trójwymiarowej animacji postaci napisaną w
C++ w sposób niezależny od architektury.

%package devel
Summary:	Header files for cal3d library
Summary(hu.UTF-8):	Fejléc fájlok a cal3d könyvtárhoz
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki cal3d
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for cal3d library.

%description devel -l hu.UTF-8
Fejléc fájlok a cal3d könyvtárhoz.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki cal3d.

%package apidocs
Summary:	API documentation and guide for cal3d library
Summary(pl.UTF-8):	Dokumentacja i wprowadzenie do biblioteki cal3d
Group:		Documentation

%description apidocs
API documentation and guide for cal3d library.

%description apidocs -l pl.UTF-8
Dokumentacja i wprowadzenie do biblioteki cal3d.

%prep
%setup -q -n Cal3D-%{version}
cd cal3d
#%patch0 -p1
%patch -P1 -p1

# obsolete macro, UnitTest++ 2 uses pkg-config instead
%{__sed} -i -e '/^AM_USE_UNITTESTCPP/d' configure.in

%build
cd cal3d
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

cd docs
%{__make} doc-api
%{__make} doc-guide
cd ..
cp -r docs/api/html api

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C cal3d install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcal3d.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc cal3d/{AUTHORS,ChangeLog,README,TODO}
%attr(755,root,root) %{_bindir}/cal3d_converter
%attr(755,root,root) %{_libdir}/libcal3d.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcal3d.so.12
%{_mandir}/man1/cal3d*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcal3d.so
%{_includedir}/cal3d
%{_pkgconfigdir}/cal3d.pc

%files apidocs
%defattr(644,root,root,755)
%doc cal3d/{api,docs/guide}
