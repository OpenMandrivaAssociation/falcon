%define oname   Falcon
%define major	1
%define libname	%mklibname %{name}_engine %{major}
%define devname	%mklibname %{name}_engine -d

Summary:	The Falcon Programming Language
Name:		falcon
Version:	0.9.6.6
Release:	5
License:	GPLv2+
Group:		Development/Other
Url:		http://www.falconpl.org/
Source0:	http://www.falconpl.org/project_dl/_official_rel/%{oname}-%{version}.tgz

BuildRequires:  bison 
BuildRequires:  cmake 
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(zlib)

%description
The Falcon Programming Language is an embeddable scripting language
aiming to empower even simple applications with a powerful,
flexible, extensible and highly configurable scripting engine.

Falcon is also a standalone multiplatform scripting language that
aims to be both simple and powerful.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Conflicts:	falcon < 0.9.6.6-5

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	falcon-devel < 0.9.6.6-5

%description -n %{devname}
This package contains development files for %{name}. This is not
necessary for using the %{name} interpreter.
%prep
%setup -qn %{oname}-%{version}

%build
%cmake \
	-DFALCON_LIB_DIR=%{_libdir} \
	-DFALCON_SHARE_DIR=%{_datadir}/%{name}
%make

%install
%makeinstall_std -C build

%files
%doc AUTHORS ChangeLog copyright README RELNOTES LICENSE LICENSE_GPLv2
%{_bindir}/falcon
%{_bindir}/faldisass
%{_bindir}/fallc.fal
%{_bindir}/falrun
%{_bindir}/falpack
%{_libdir}/falcon
%{_datadir}/falcon
%{_mandir}/man1/falcon.1*
%{_mandir}/man1/faldisass.1*
%{_mandir}/man1/fallc.fal.1*
%{_mandir}/man1/falrun.1*
%{_mandir}/man1/falpack.1*
%exclude %{_datadir}/falcon/cmake

%files -n %{libname}
%{_libdir}/libfalcon_engine.so.%{major}*

%files -n %{devname}
%{_bindir}/falcon-conf
%{_bindir}/falconeer.fal
%{_bindir}/faltest
%{_datadir}/falcon/cmake/*.cmake
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man1/falcon-conf*
%{_mandir}/man1/falconeer.fal*
%{_mandir}/man1/faltest*

