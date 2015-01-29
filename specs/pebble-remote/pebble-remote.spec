Name:           pebble-remote
Version:        2.0
Release:        1
Summary:        Remote control for LibreOffice & Apache OpenOffice Impress with Pebble
Group:          System/Libraries/Python
URL:            http://www.pebbleremote.com/
Source:         https://github.com/COMU/pebble-remote/archive/master.zip
License:        GPL
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  pybluez >= 0.18
BUildRequires:  lightblue >= 0.4
Requires:       pybluez >= 0.18
Requires:       lightblue >= 0.4
Requires:       python-pexpect
Requires:       python-tk

%description
Pebble Remote is a free software that provides remote control for Libreoffice & Apache OpenOffice Impress with Pebble. 
It is simple to installation and usage. This application can be used in two ways; via console or desktop. 

%prep
%autosetup -n %{name}-master

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__python} setup.py install \
   --root=$RPM_BUILD_ROOT \
   -O1 --skip-build \
   --install-headers=%{_includedir}/python \
   --install-lib=%{python_sitearch} \
   --record=%{name}.filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.filelist
%defattr(-,root,root)
%doc CHANGELOG

%changelog
* Wed Jan 28 2015 Ali Erdinc Koroglu <aekoroglu@gmail.com> - 2.0
- 1st release for Fedora
