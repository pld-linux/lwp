Summary:	LWP thread library
Summary(pl):	Biblioteka w�tk�w LWP
Summary(pt_BR):	Biblioteca LWP thread
Name:		lwp
Version:	1.12
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	ftp://ftp.coda.cs.cmu.edu/pub/lwp/src/%{name}-%{version}.tar.gz
# Source0-md5:	5b4139c9b1ac393de433683ed355425b
# Source0-size:	365064
Patch0:		%{name}-configure.patch
Patch1:		%{name}-amd64.patch
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

%description -l pl
Biblioteka w�tk�w w przestrzeni u�ytkownika LWP. Biblioteka ta jest
u�ywana przez rozproszony system plik�w Coda, RVM (bibliotek� VM),
RPC2/SFTP (bibliotek� zdalnych wywo�a� procedur).

%description -l pt_BR
Biblioteca LWP para threads em userspace. Esta biblioteca � utilizada
pelo Coda (um sistema de arquivos distribu�do) e pelas bibliotecas RVM
e RPC2/SFTP.

%package devel
Summary:	LWP thread library development files
Summary(pl):	Pliki dla programist�w u�ywaj�cych LWP
Summary(pt_BR):	Arquivos para desenvolvimento com a biblioteca LWP thread
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	liblwp2-devel

%description devel
Headers and libraries for developing programs using the LWP userspace
threads library.

%description devel -l pl
Pliki nag��wkowe do tworzenia program�w u�ywaj�cych biblioteki w�tk�w
w przestrzeni u�ytkownika LWP.

%description devel -l pt_BR
Arquivos para desenvolvimento com a biblioteca LWP threads em
userspace.

%package static
Summary:	LWP thread library static libraries
Summary(pl):	Statyczne biblioteki LWP
Summary(pt_BR):	Bibliteca est�tica LWP thread
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for developing programs using the LWP userspace
threads library.

%description static -l pl
Statyczna wersja biblioteki w�tk�w w przestrzeni u�ytkownika LWP.

%description static -l pt_BR
Biblioteca est�tica LWP para threads em userspace.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
