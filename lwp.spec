Summary:	LWP thread library
Summary(pl):	Biblioteka w±tków LWP
Summary(pt_BR):	Biblioteca LWP thread
Name:		lwp
Version:	1.9
Release:	4
License:	GPL (?LGPL)
Group:		Libraries
Source0:	ftp://ftp.coda.cs.cmu.edu/pub/lwp/src/%{name}-%{version}.tar.gz
Patch0:		%{name}-configure.patch
URL:		http://www.coda.cs.cmu.edu/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	liblwp2

%description
The LWP userspace threads library. The LWP threads library is used by
the Coda distributed filesystem, RVM (a persistent VM library), and
RPC2/SFTP (remote procedure call library).

%description -l pl
Biblioteka w±tków w przestrzeni u¿ytkownika LWP. Biblioteka ta jest
u¿ywana przez rozproszony system plików Coda, RVM (biblioteka VM),
RPC2/SFTP (biblioteka zdalnych wywo³añ procedur).

%description -l pt_BR
Biblioteca LWP para threads em userspace. Esta biblioteca é utilizada
pelo Coda (um sistema de arquivos distribuído) e pelas bibliotecas RVM
e RPC2/SFTP.

%package devel
Summary:	LWP thread library development files
Summary(pl):	Pliki dla programistów u¿ywaj±cych LWP
Summary(pt_BR):	Arquivos para desenvolvimento com a biblioteca LWP thread
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	liblwp2-devel

%description devel
Headers and libraries for developing programs using the LWP userspace
threads library. The LWP threads library is used by the Coda
distributed filesystem, RVM (a persistent VM library), and RPC2/SFTP
(a remote procedure call library).

%description devel -l pl
Pliki nag³ówkowe do tworzenia programów u¿ywaj±cych biblioteki w±tków
w przestrzeni u¿ytkownika LWP. Biblioteka ta jest u¿ywana przez rozproszony 
system plików Coda, RVM (biblioteka VM), RPC2/SFTP (biblioteka zdalnych 
wywo³añ procedur).

%description devel -l pt_BR
Biblioteca LWP para threads em userspace. Esta biblioteca é utilizada
pelo Coda (um sistema de arquivos distribuído) e pelas bibliotecas RVM
e RPC2/SFTP.

%package static
Summary:	LWP thread library static libraries
Summary(pl):	Statyczne biblioteki LWP
Summary(pt_BR):	Bibliteca estática LWP thread
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries for developing programs using the LWP userspace
threads library. The LWP threads library is used by the Coda
distributed filesystem, RVM (a persistent VM library), and RPC2/SFTP
(a remote procedure call library).

%description static -l pl
Statyczna wersja biblioteki w±tków w przestrzeni u¿ytkownika LWP.
Biblioteka ta jest u¿ywana przez rozproszony system plików Coda, RVM 
(biblioteka VM), RPC2/SFTP (biblioteka zdalnych wywo³añ procedur).

%description static -l pt_BR
Biblioteca LWP para threads em userspace. Esta biblioteca é utilizada
pelo Coda (um sistema de arquivos distribuído) e pelas bibliotecas RVM
e RPC2/SFTP.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing configure.ac
%{__libtoolize}
autoheader
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblwp.so.*.*

%files devel
%defattr(644,root,root,755)
%doc PORTING README NEWS ChangeLog AUTHORS
%attr(755,root,root) %{_libdir}/liblwp.so
%attr(755,root,root) %{_libdir}/liblwp.la
%{_includedir}/lwp

%files static
%defattr(644,root,root,755)
%{_libdir}/liblwp.a
