Summary:	LWP thread library
Summary(pl):	Biblioteka w�tk�w LWP
Name:		lwp
Version:	1.9
Release:	2
License:	GPL (?LGPL)
Group:		Libraries
Source0:	ftp://ftp.coda.cs.cmu.edu/pub/lwp/src/%{name}-%{version}.tar.gz
URL:		http://www.coda.cs.cmu.edu/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The LWP userspace threads library. The LWP threads library is used by
the Coda distributed filesystem, RVM (a persistent VM library), and
RPC2/SFTP (remote procedure call library).

%description -l pl
Biblioteka w�tk�w w przestrzeni u�ytkownika LWP. Biblioteka ta jest
u�ywana przez rozproszony system plik�w Coda, RVM (biblioteka VM),
RPC2/SFTP (biblioteka zdalnych wywo�a� procedur).

%package devel
Summary:	LWP thread library development files
Summary(pl):	Pliki dla programist�w u�ywaj�cych LWP
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Headers and libraries for developing programs using the LWP userspace
threads library. The LWP threads library is used by the Coda
distributed filesystem, RVM (a persistent VM library), and RPC2/SFTP
(a remote procedure call library).

%description devel -l pl
Pliki nag��wkowe do tworzenia program�w u�ywaj�cych biblioteki w�tk�w
w przestrzeni u�ytkownika LWP.

%package static
Summary:	LWP thread library static libraries
Summary(pl):	Statyczne biblioteki LWP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries for developing programs using the LWP userspace
threads library. The LWP threads library is used by the Coda
distributed filesystem, RVM (a persistent VM library), and RPC2/SFTP
(a remote procedure call library).

%description static -l pl
Statyczna wersja biblioteki w�tk�w w przestrzeni u�ytkownika LWP.

%prep
%setup -q
touch ChangeLog

%build
libtoolize --copy --force
autoheader
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf PORTING README NEWS ChangeLog AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblwp.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/liblwp.so
%attr(755,root,root) %{_libdir}/liblwp.la
%{_includedir}/lwp

%files static
%defattr(644,root,root,755)
%{_libdir}/liblwp.a
