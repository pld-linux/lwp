Summary:	LWP thread library
Name:		lwp
Version:	cvs20001115
Release:	1
License:	GPL (?LGPL)
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Source0:	%{name}-%{version}.tgz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The LWP userspace threads library. The LWP threads library is used by
the Coda distributed filesystem, RVM (a persistent VM library), and
RPC2/SFTP (remote procedure call library).

%package devel
Summary:	LWP thread library development files
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Headers and libraries for developing programs using the LWP userspace
threads library. The LWP threads library is used by the Coda
distributed filesystem, RVM (a persistent VM library), and RPC2/SFTP
(a remote procedure call library).

%package static
Summary:	LWP thread library static libraries
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libraries for developing programs using the LWP userspace
threads library. The LWP threads library is used by the Coda
distributed filesystem, RVM (a persistent VM library), and RPC2/SFTP
(a remote procedure call library).

%prep
%setup -q -n lwp

%build
touch ChangeLog
autoheader
aclocal
libtoolize
automake --copy --add-missing
autoconf
%configure
%{__make} OPTFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc PORTING README NEWS INSTALL ChangeLog AUTHORS COPYING
%attr(755,root,root) %{_libdir}/liblwp.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblwp.so
%attr(755,root,root) %{_libdir}/liblwp.la
%{_includedir}/lwp

%files static
%defattr(644,root,root,755)
%{_libdir}/liblwp.a
