Summary:	LWP thread library
Summary(pl):	Biblioteka w±tkÛw LWP
Name:		lwp
Version:	1.9
Release:	2
License:	GPL (?LGPL)
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
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
Biblioteka w±tkÛw w przestrzeni uøytkownika LWP. Biblioteka ta jest
uøywana przez rozproszony system plikÛw Coda, RVM (biblioteka VM),
RPC2/SFTP (biblioteka zdalnych wywo≥aÒ procedur).

%package devel
Summary:	LWP thread library development files
Summary(pl):	Pliki dla programistÛw uøywaj±cych LWP
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Headers and libraries for developing programs using the LWP userspace
threads library. The LWP threads library is used by the Coda
distributed filesystem, RVM (a persistent VM library), and RPC2/SFTP
(a remote procedure call library).

%description devel -l pl
Pliki nag≥Ûwkowe do tworzenia programÛw uøywaj±cych biblioteki w±tkÛw
w przestrzeni uøytkownika LWP.

%package static
Summary:	LWP thread library static libraries
Summary(pl):	Statyczne biblioteki LWP
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Static libraries for developing programs using the LWP userspace
threads library. The LWP threads library is used by the Coda
distributed filesystem, RVM (a persistent VM library), and RPC2/SFTP
(a remote procedure call library).

%description static -l pl
Statyczna wersja biblioteki w±tkÛw w przestrzeni uøytkownika LWP.

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
