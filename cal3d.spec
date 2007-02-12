Summary:	3d character animation library
Summary(pl.UTF-8):	Biblioteka do trójwymiarowej animacji postaci
Name:		cal3d
Version:	0.11.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://download.gna.org/cal3d/sources/%{name}-%{version}.tar.gz
# Source0-md5:	82ad09c1c28e73bc9596aec47237bfba
Patch0:		%{name}-fixtag.patch
URL:		https://gna.org/projects/cal3d/
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

%description -l pl.UTF-8
Cal3d jest biblioteką do trójwymiarowej animacji postaci napisaną w
C++ w sposób niezależny od architektury.

%package devel
Summary:	Header files for cal3d library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki cal3d
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for cal3d library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki cal3d.

%prep
%setup -q
#%patch0 -p1

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
%attr(755,root,root) %{_bindir}/cal3d*
%attr(755,root,root) %{_libdir}/libcal3d.so.*
%{_mandir}/man1/cal3d*

%files devel
%defattr(644,root,root,755)
%doc api docs/guide
%attr(755,root,root) %{_libdir}/libcal3d.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc
