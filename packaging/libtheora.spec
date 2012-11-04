Name:           libtheora
Version:        1.1.1
Release:        14
License:        BSD-3-Clause
Summary:        Free Video Codec
Url:            http://www.theora.org/
Group:          Productivity/Multimedia/Other
%define pkg_version %{version}
Source:         %{name}-%{version}.tar.bz2
Source2:        baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  libogg-devel
BuildRequires:  libtool
BuildRequires:  libvorbis-devel
BuildRequires:  pkg-config
BuildRequires:  python

%description
Theora is a free video codec based on VP3. The package contains the
library that can decode and encode Theora streams. Theora is also able
to playback VP3 streams.

%package devel
License:        BSD-3-Clause
Summary:        Free Video Codec
Group:          Development/Libraries/C and C++
Requires:       libogg-devel
Requires:       libtheora = %{version}

%description devel
Theora is a free video codec based on VP3. The package contains the
library that can decode and encode Theora streams. Theora is also able
to playback VP3 streams.

%prep
%setup -q -n %{name}-%{pkg_version}

%build
ACLOCAL="aclocal -I m4" autoreconf -f -i
%configure --disable-examples \
    --disable-static \
    --with-pic
make %{?_smp_mflags} docdir=%{_docdir}/%{name}

%check
make check

%install
%make_install
install -d %{buildroot}%{_bindir}

rm -rf %{buildroot}/%{_datadir}/doc/%{name}-%{version}/*

%post  -p /sbin/ldconfig

%postun  -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/libtheora.so.0*
%{_libdir}/libtheoradec.so.1*
%{_libdir}/libtheoraenc.so.1*

%files devel
%defattr(-,root,root)
%doc COPYING LICENSE
%{_includedir}/theora
%{_libdir}/*.so
%{_libdir}/pkgconfig/theoradec.pc
%{_libdir}/pkgconfig/theoraenc.pc
%{_libdir}/pkgconfig/theora.pc
