%global 	abi_package %{nil}
%define 	appname PasswordSafe
%define 	appid org.gnome.PasswordSafe

Name:           passwordsafe
Version:        5.0
Release:        1%{?dist}
Summary:        A password manager for GNOME
License:        GPLv3+
URL:            https://gitlab.gnome.org/World/PasswordSafe
Source:         %{url}/-/archive/%{version}/%{appname}-%{version}.tar.bz2
BuildRequires:  meson
BuildRequires:  pkg-config
BuildRequires:  desktop-file-utils appstream-glib
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  python3-dev
BuildRequires:  python-dateutil-python3 
BuildRequires:  pycparser-python3
BuildRequires:  lxml-python3
BuildRequires:  argon2-cffi-python3
BuildRequires:  python-future-python3
BuildRequires:  pycryptodomex-python3
BuildRequires:  pykeepass-python3
BuildRequires:  construct-python3

Requires:       pykeepass-python3
Requires:       construct-python3
Requires:       pycryptodomex-python3
Requires:       lxml-python3
Requires:       libpwquality-python3
Requires:       argon2-cffi-python3
BuildArch:      noarch

%description
Password Safe is a password manager which makes use of the Keepass v.4 format.
It integrates with the GNOME desktop and provides an interface for the
management of password databases.

%prep
%setup -q -n %{appname}-%{version}

%build
export LANG=C.UTF-8
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
mv %{buildroot}/usr/share/mime/application %{buildroot}/usr/share/mime/packages
%find_lang passwordsafe

%post
glib-compile-schemas /usr/share/glib-2.0/schemas


%files -f passwordsafe.lang
%license LICENSE
%doc README.md
%{_bindir}/gnome-%{name}
/usr/lib/python3*/*/passwordsafe/
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/passwordsafe/
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/%{appid}.svg
%{_datadir}/metainfo/%{appid}.appdata.xml
%{_datadir}/mime-packages/org.gnome.PasswordSafe.xml

%changelog
# based on https://build.opensuse.org/package/view_file/openSUSE:Factory/gnome-passwordsafe/
