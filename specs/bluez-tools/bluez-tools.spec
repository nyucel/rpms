Summary:            A set of tools to manage bluetooth devices for linux
Name:               bluez-tools
Version:            0.1.38
Release:            662e%{?dist}
License:            GPLv2+
Group:              System Environment/Base
Source:             https://bluez-tools.googlecode.com/files/%{name}-%{version}-662e.tar.gz
URL:                https://code.google.com/p/bluez-tools/
BuildRequires:      dbus-glib-devel
BuildRequires:      dbus-devel >= 0.90
BuildRequires:      glib2-devel
BuildRequires:      readline-devel
Requires:           bluez >= 4.69
Requires:           obexd >= 0.30

%description
This is a GSoC'10 project to implement a new command line tools for bluez (bluetooth stack for linux).
The project implemented in C and uses the D-Bus interface of bluez. 

%prep
%autosetup -n %{name}-%{version}-662e

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon Jan 26 2015 Ali Erdinc Koroglu <aekoroglu@gmail.com> - 0.1.38-662e
- 1st release for Fedora
