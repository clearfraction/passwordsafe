%global 	abi_package %{nil}
%define 	appname PasswordSafe
%define 	appid org.gnome.PasswordSafe

Name:           gnome-passwordsafe
Version:        3.32.0
Release:        1%{?dist}
Summary:        A password manager for GNOME
License:        GPLv3+
URL:            https://gitlab.gnome.org/World/%{appname}
Source:         %{url}/-/archive/%{version}/%{appname}-%{version}.tar.bz2
BuildRequires:  meson
BuildRequires:  pkg-config
BuildRequires:  desktop-file-utils appstream-glib
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-0.0)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  python3-dev
BuildRequires:  python-dateutil-python3 
BuildRequires:  pycparser-python3
BuildRequires:  lxml-python3
BuildRequires:  argon2_cffi-python3
BuildRequires:  python-future-python3
BuildRequires:  pycryptodome-python3
BuildRequires:  pykeepass-python3
BuildRequires:  construct-python3

Requires:       pykeepass-python3
Requires:       construct-python3
Requires:       pycryptodome-python3
Requires:       lxml-python3
Requires:       libpwquality-python3
Requires:       argon2_cffi-python3
BuildArch:      noarch

%description
Password Safe is a password manager which makes use of the Keepass v.4 format.
It integrates with the GNOME desktop and provides an interface for the
management of password databases.

%prep
%setup -q -n %{appname}-%{version}

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1574700391
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install


%find_lang passwordsafe


%files -f passwordsafe.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
/usr/lib/python3*/*/passwordsafe/
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/passwordsafe/
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/%{appid}.svg
%{_datadir}/metainfo/%{appid}.appdata.xml


%changelog
# based on https://build.opensuse.org/package/view_file/openSUSE:Factory/gnome-passwordsafe/