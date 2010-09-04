%define oname   Falcon

Name:           falcon
Version:        0.9.6.6
Release:        %mkrel 1
Summary:        The Falcon Programming Language
License:        GPLv2+
Group:          Development/Other
URL:            http://www.falconpl.org/
Source:         http://www.falconpl.org/project_dl/_official_rel/%{oname}-%{version}.tgz
BuildRoot:      %_tmppath/%name-%version-%release-root
BuildRequires:  bison 
BuildRequires:  cmake 
BuildRequires:  pcre-devel 
BuildRequires:  zlib-devel

%description
The Falcon Programming Language is an embeddable scripting language
aiming to empower even simple applications with a powerful,
flexible, extensible and highly configurable scripting engine.

Falcon is also a standalone multiplatform scripting language that
aims to be both simple and powerful.

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog copyright README RELNOTES LICENSE LICENSE_GPLv2
%{_bindir}/falcon
%{_bindir}/faldisass
%{_bindir}/fallc.fal
%{_bindir}/falrun
%{_bindir}/falpack
%{_libdir}/falcon
%{_libdir}/*.so.*
%{_datadir}/falcon
%{_mandir}/man1/falcon.1.*
%{_mandir}/man1/faldisass.1.*
%{_mandir}/man1/fallc.fal.1.*
%{_mandir}/man1/falrun.1.*
%{_mandir}/man1/falpack.1.*
%exclude %{_datadir}/falcon/cmake

#--------------------------------------------------------------------

%package   devel
Summary:   Development files for %{name}
Group:     Development/Other
Requires:  %{name} = %{version}-%{release}

%description devel
The Falcon Programming Language is an embeddable scripting language
aiming to empower even simple applications with a powerful,
flexible, extensible and highly configurable scripting engine.

Falcon is also a standalone multiplatform scripting language that
aims to be both simple and powerful.

This package contains development files for %{name}. This is not
necessary for using the %{name} interpreter.

%files devel
%defattr(-,root,root,-)
%{_bindir}/falcon-conf
%{_bindir}/falconeer.fal
%{_bindir}/faltest
%{_datadir}/falcon/cmake/*.cmake
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man1/falcon-conf*
%{_mandir}/man1/falconeer.fal*
%{_mandir}/man1/faltest*

#--------------------------------------------------------------------
%prep
%setup -q -n %oname-%{version}

%build
%cmake -DFALCON_LIB_DIR=%{_libdir} -DFALCON_SHARE_DIR=%{_datadir}/%{name}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT
