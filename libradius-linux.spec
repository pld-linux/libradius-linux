Summary:	TACACS+ libradius for Linux
Summary(pl.UTF-8):	Biblioteka libradius dla Linuksa z projektu TACACS+
Name:		libradius-linux
Version:	20040827
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://portal-to-web.de/tacacs/%{name}-%{version}.tar.gz
# Source0-md5:	c7cc2f49acdd9955a052029326833fe1
Patch0:		%{name}-make.patch
URL:		http://portal-to-web.de/tacacs/libradius.php
BuildRequires:	libmd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a library to generate RADIUS authentication request.

%description -l pl.UTF-8
Biblioteka do generowania żądań uwierzytelniania RADIUS.

%package devel
Summary:	Header files for RADIUS library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki RADIUS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for RADIUS library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki RADIUS.

%package static
Summary:	Static RADIUS library
Summary(pl.UTF-8):	Statyczna biblioteka RADIUS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static RADIUS library.

%description static -l pl.UTF-8
Statyczna biblioteka RADIUS.

%prep
%setup -q -n libradius-linux
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_mandir}/man{3,5}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libradius.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libradius.so.1
%{_mandir}/man5/radius.conf.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libradius.so
%{_includedir}/radlib.h
%{_mandir}/man3/libradius.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libradius.a
