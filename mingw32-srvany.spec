%define __strip %{_mingw32_strip}
%define __objdump %{_mingw32_objdump}
%define _use_internal_dependency_generator 0
%define __find_requires %{_mingw32_findrequires}
%define __find_provides %{_mingw32_findprovides}

%global upstream_version 31b3bf3

Name:		mingw32-srvany
Version:	1.0
Release:	4%{?dist}.4
Summary:	Utility for creating services for Windows

Group:		Development/Libraries

License:	GPLv2+
URL:		http://github.com/beekhof/mingw32-srvany
Source0:	http://github.com/downloads/beekhof/mingw32-srvany/mingw32-srvany-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{upstream_release}-root-%(%{__id_u} -n)
BuildArch:	noarch

BuildRequires:	automake autoconf libtool
BuildRequires:	redhat-rpm-config
BuildRequires:	mingw32-filesystem >= 56
BuildRequires:	mingw32-gcc
BuildRequires:	mingw32-gcc-c++
BuildRequires:	mingw32-binutils

%description
Utility for creating a service from any MinGW Windows binary

%prep
%setup -q -n beekhof-mingw32-srvany-%{upstream_version}

%build
autoreconf -i
%{_mingw32_configure} 
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_mingw32_bindir}/srvany.exe
%doc COPYING
%doc AUTHORS

%changelog
* Mon Dec 27 2010 Andrew Beekhof <abeekhof@redhat.com> - 1.0-4.4
- Rebuild everything with gcc-4.4
  Related: rhbz#658833

* Fri Dec 24 2010 Andrew Beekhof <abeekhof@redhat.com> - 1.0-4.3
- The use of ExclusiveArch conflicts with noarch, using an alternate COLLECTION to limit builds
  Related: rhbz#658833

* Wed Dec 22 2010 Andrew Beekhof <abeekhof@redhat.com> - 1.0-4.2
- Only build mingw packages on x86_64
  Related: rhbz#658833

* Wed Dec 22 2010 Andrew Beekhof <abeekhof@redhat.com> - 1.0-4.1
- Bump the revision to avoid tag collision
  Related: rhbz#658833

* Fri Dec 3 2010 Andrew Beekhof <andrew@beekhof.net> - 1.0-4
- Fixed the license tag

* Mon Oct 25 2010 Andrew Beekhof <andrew@beekhof.net> - 1.0-3
- Incorporate feedback from Fedora review

* Mon Sep 13 2010 Andrew Beekhof <andrew@beekhof.net> - 1.0-1
- Initial build.
