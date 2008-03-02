Summary:	LWP thread library
Summary(pl.UTF-8):	Biblioteka wątków LWP
Summary(pt_BR.UTF-8):	Biblioteca LWP thread
Name:		lwp
Version:	2.4
Release:	0.1
License:	LGPL v2
Group:		Libraries
Source0:	ftp://ftp.coda.cs.cmu.edu/pub/lwp/src/%{name}-%{version}.tar.gz
# Source0-md5:	5bd3221562de580d51f18c547f7606e3
Patch0:		%{name}-configure.patch
URL:		http://www.coda.cs.cmu.edu/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	liblwp2

%description
The LWP userspace threads library. The LWP threads library is used by
the Coda distributed filesystem, RVM (a persistent VM library), and
RPC2/SFTP (remote procedure call library).

%description -l pl.UTF-8
Biblioteka wątków w przestrzeni użytkownika LWP. Biblioteka ta jest
używana przez rozproszony system plików Coda, RVM (bibliotekę VM),
RPC2/SFTP (bibliotekę zdalnych wywołań procedur).

%description -l pt_BR.UTF-8
Biblioteca LWP para threads em userspace. Esta biblioteca é utilizada
pelo Coda (um sistema de arquivos distribuído) e pelas bibliotecas RVM
e RPC2/SFTP.

%package devel
Summary:	LWP thread library development files
Summary(pl.UTF-8):	Pliki dla programistów używających LWP
Summary(pt_BR.UTF-8):	Arquivos para desenvolvimento com a biblioteca LWP thread
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	liblwp2-devel

%description devel
Headers and libraries for developing programs using the LWP userspace
threads library.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia programów używających biblioteki wątków
w przestrzeni użytkownika LWP.

%description devel -l pt_BR.UTF-8
Arquivos para desenvolvimento com a biblioteca LWP threads em
userspace.

%package static
Summary:	LWP thread library static libraries
Summary(pl.UTF-8):	Statyczne biblioteki LWP
Summary(pt_BR.UTF-8):	Bibliteca estática LWP thread
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for developing programs using the LWP userspace
threads library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki wątków w przestrzeni użytkownika LWP.

%description static -l pt_BR.UTF-8
Biblioteca estática LWP para threads em userspace.

%prep
%setup -q
%patch0 -p1

%build
rm -f configure.ac
%{__libtoolize}
%{__autoheader}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/liblwp.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblwp.so
%{_libdir}/liblwp.la
%{_includedir}/lwp

%files static
%defattr(644,root,root,755)
%{_libdir}/liblwp.a
