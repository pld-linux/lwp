Summary:	LWP thread library
Name:		lwp
Version:	1.4
Release:	1
License:	GPL
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Source:		ftp://ftp.coda.cs.cmu.edu/pub/coda/src/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The LWP userspace threads library. The LWP threads library is used by the Coda
distributed filesystem, RVM (a persistent VM library), and RPC2/SFTP (remote
procedure call library)

%package devel
Summary: 	LWP thread library development files
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Headers and libraries for developing programs using the LWP userspace threads
library. The LWP threads library is used by the Coda distributed filesystem,
RVM (a persistent VM library), and RPC2/SFTP (a remote procedure call library)

%package static
Summary: 	LWP thread library static libraries
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libraries for developing programs using the LWP userspace threads
library. The LWP threads library is used by the Coda distributed filesystem,
RVM (a persistent VM library), and RPC2/SFTP (a remote procedure call library)

%prep
%setup -q

%build
%configure --prefix=/usr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%files
%attr(755,root,root) /usr/lib/liblwp.so.1.0.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblwp.so
%{_libdir}/liblwp.la
%{_includedir}/lwp/lock.h
%{_includedir}/lwp/lwp.h
%{_includedir}/lwp/preempt.h
%{_includedir}/lwp/timer.h

%files static
%defattr(644,root,root,755)
%{_libdir}/liblwp.a
