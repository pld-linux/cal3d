Summary:	3d character animation library
Summary(pl):	Biblioteka do trójwymiarowej animacji postaci
Name:		cal3d
Version:	0.9.1
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	55023cf5b4063990f355629c57a175af
Patch0:		%{name}-fixtag.patch
URL:		http://cal3d.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-utils
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cal3d is a 3d character animation library written in C++ in a
platform-/graphic API-independent way.

%description -l pl
Cal3d jest biblioteką do trójwymiarowej animacji postaci napisaną w
C++ w sposób niezależny od architektury.

%package devel
Summary:	Header files for cal3d library
Summary(pl):	Pliki nagłówkowe biblioteki cal3d
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for cal3d library.

%description devel -l pl
Pliki nagłówkowe biblioteki cal3d.

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

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO docs/guide
%attr(755,root,root) %{_libdir}/libcal3d-*.so

%files devel
%defattr(644,root,root,755)
%doc docs/api/html/*
%attr(755,root,root) %{_libdir}/libcal3d.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc
