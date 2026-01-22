%define api	0.0
%define major	0
%define oldlibname	%mklibname zmf %{api} %{major}
%define libname	%mklibname zmf
%define devname	%mklibname -d zmf

Summary:	Library for importing and converting Zoner Callisto/Draw 4 and 5 images
Name:		libzmf
Version:	0.0.2
Release:	13
Group:		Office
License:	LGPLv2+
Url:		https://wiki.documentfoundation.org/DLP/Libraries/libzmf
Source0:	http://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	doxygen
BuildRequires:	pkgconfig(librevenge-0.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(icu-uc) >= 60
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(cppunit)
BuildRequires:	boost-devel

%description
libzmf is a library for reading and converting Zoner Callisto/Draw images

%package tools
Summary:	Tools to convert ZMF images into other formats
Group:		Publishing

%description tools
Tools to convert ZMF images into other formats.
Currently supported: raw svg

%package -n %{libname}
Summary:	Library for importing and converting Zoner Callisto/Draw images
Group:		System/Libraries
%rename %{oldlibname}

%description -n %{libname}
libzmf is a library for reading and converting ZMF images

%package -n %{devname}
Summary:	Files for developing with libzmf
Group:		Development/C++
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Includes and definitions for developing with libzmf.

%prep
%setup -q

%build
CFLAGS="%{optflags} -Qunused-arguments" \
CXXFLAGS="%{optflags} -Qunused-arguments" \
%configure --disable-werror
%make 

%install
%makeinstall_std

%files tools
%doc ChangeLog README AUTHORS
%{_bindir}/zmf2*

%files -n %{libname}
%{_libdir}/libzmf-%{api}.so.%{major}*

%files -n %{devname}
%{_libdir}/libzmf*.so
%{_libdir}/pkgconfig/libzmf*.pc
%{_includedir}/*
%doc %{_docdir}/libzmf/*

