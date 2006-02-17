Summary:	3d character animation library
Summary(pl):	Biblioteka do trójwymiarowej animacji postaci
Name:		cal3d
Version:	0.10.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/cal3d/%{name}-full-%{version}.tar.bz2
# Source0-md5:	47b3b72c6adcf5351f0884639d606d05
Patch0:		%{name}-fixtag.patch
URL:		http://cal3d.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-utils
BuildRequires:	doxygen
BuildRequires:	gnome-doc-tools
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cal3d is a 3d character animation library written in C++ in a
platform-/graphic API-independent way.

%description -l pl
Cal3d jest bibliotek± do trójwymiarowej animacji postaci napisan± w
C++ w sposób niezale¿ny od architektury.

%package devel
Summary:	Header files for cal3d library
Summary(pl):	Pliki nag³ówkowe biblioteki cal3d
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for cal3d library.

%description devel -l pl
Pliki nag³ówkowe biblioteki cal3d.

%prep
%setup -q
%patch0 -p1

%build
rm -f acinclude.m4
%{__aclocal}
%{__libtoolize}
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libcal3d.so.*

%files devel
%defattr(644,root,root,755)
%doc api docs/guide docs/modeling
%attr(755,root,root) %{_libdir}/libcal3d.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc
