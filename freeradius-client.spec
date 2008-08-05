%define major 2
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	FreeRADIUS Client Software
Name:		freeradius-client
Version:	1.1.6
Release:	%mkrel 1
License:	BSD-like
Group:		System/Servers
URL:		http://www.freeradius.org/
Source0:	ftp://ftp.freeradius.org/pub/radius/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.freeradius.org/pub/radius/%{name}-%{version}.tar.gz.sig
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
FreeRADIUS Client is a framework and library for writing RADIUS Clients which
additionally includes radlogin, a flexible RADIUS aware login replacement, a
command line program to send RADIUS accounting records and a utility to query
the status of a (Merit) RADIUS server.

%package -n	%{libname}
Summary:	FreeRADIUS Client Software library
Group:          System/Libraries

%description -n	%{libname}
FreeRADIUS Client is a framework and library for writing RADIUS Clients which
additionally includes radlogin, a flexible RADIUS aware login replacement, a
command line program to send RADIUS accounting records and a utility to query
the status of a (Merit) RADIUS server.

This package contains the shared library of FreeRADIUS Client

%package -n	%{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name} = %{version}-%{release}

%description -n	%{develname}
FreeRADIUS Client is a framework and library for writing RADIUS Clients which
additionally includes radlogin, a flexible RADIUS aware login replacement, a
command line program to send RADIUS accounting records and a utility to query
the status of a (Merit) RADIUS server.

This package contains the header and static libraries files for
freeradius-client.

%prep

%setup -q

%build
rm missing
libtoolize --copy --force; aclocal; automake -ac; autoconf

%configure2_5x \
    --localstatedir=/var/lib \
    --enable-shadow \
    --with-secure-path

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc BUGS COPYRIGHT README README.radexample doc/ChangeLog doc/instop.html doc/login.example
%dir %{_sysconfdir}/radiusclient
%attr(0644,root,root) %{_sysconfdir}/radiusclient/dictionary
%attr(0644,root,root) %{_sysconfdir}/radiusclient/dictionary.*
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/radiusclient/radiusclient.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/radiusclient/issue
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/radiusclient/port-id-map
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/radiusclient/servers
%attr(0755,root,root) %{_sbindir}/login.radius
%attr(0755,root,root) %{_sbindir}/radacct
%attr(0755,root,root) %{_sbindir}/radembedded
%attr(0755,root,root) %{_sbindir}/radexample
%attr(0755,root,root) %{_sbindir}/radiusclient
%attr(0755,root,root) %{_sbindir}/radlogin
%attr(0755,root,root) %{_sbindir}/radstatus

%files -n %{libname}
%defattr(-,root,root)
%attr(0755,root,root) %{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%attr(0644,root,root) %{_includedir}/*.h
%attr(0644,root,root) %{_libdir}/*.*a
%attr(0755,root,root) %{_libdir}/*.so

