Summary:	Library for reading and writing optical discs
Name:		libburn
Version:	1.2.4
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://files.libburnia-project.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	25b45b1ccf6921a5bce4e2d88f55a81f
URL:		http://libburnia-project.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libburn is an open-source library for reading, mastering and writing
optical discs.

%package devel
Summary:	Header files for libburn library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libburn library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTORS COPYRIGHT README
%attr(755,root,root) %{_bindir}/cdrskin
%attr(755,root,root) %ghost %{_libdir}/libburn.so.4
%attr(755,root,root) %{_libdir}/libburn.so.*.*.*
%{_mandir}/man1/cdrskin.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libburn.so
%{_libdir}/libburn.la
%{_includedir}/libburn
%{_pkgconfigdir}/libburn-1.pc

