Name:           lightblue
Version:        0.4
Release:        1
Summary:        LightBlue is a cross-platform Bluetooth API for Python which provides simple access to Bluetooth operations.
Group:          System/Libraries/Python
URL:            https://github.com/pebble/lightblue-0.4
Source:         https://github.com/pebble/lightblue-0.4/archive/master.zip
License:        GPL
BuildRequires:  bluez-libs-devel
BuildRequires:  openobex-devel >= 1.5
BuildRequires:  python-devel
BuildRequires:  pybluez >= 0.18
Requires:       python >= 2.7
Requires:       pybluez >= 0.18

%description
LightBlue is a cross-platform Bluetooth API for Python which provides simple access to Bluetooth operations. 
It is available for Mac OS X, GNU/Linux and Nokia's Python for Series 60 platform for mobile phones.

LightBlue provides simple access to:
    * Device and service discovery (with and without end-user GUIs)
    * Standard socket interface for RFCOMM and L2CAP sockets (currently L2CAP client sockets only, and not on PyS60)
    * Sending and receiving files over OBEX
    * Advertising of RFCOMM and OBEX services
    * Local device information

%prep
%autosetup -n %{name}-%{version}-master

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__python} setup.py install \
   --root=$RPM_BUILD_ROOT \
   -O1 --skip-build \
   --install-headers=%{_includedir}/python \
   --install-lib=%{python_sitearch} \
   --record=%{name}.filelist

mv doc html

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.filelist
%defattr(-,root,root)
%doc CHANGELOG README.txt html examples

%changelog
* Mon Jan 26 2015 Ali Erdinc Koroglu <aekoroglu@gmail.com> - 0.4
- 1st release for Fedora
