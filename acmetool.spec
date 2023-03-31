Name:           acmetool
Version:	0.2.1
Release:	2
Summary:        Automatic certificate acquisition tool for ACME (Let's Encrypt)
Group:          System/Servers
License:        MIT
URL:            https://github.com/hlandau/acme
Source0:	https://github.com/hlandau/acme/archive/v%{version}.tar.gz
# Needs to package some go libraries along with it...
Source100:	get-source.sh
BuildRequires:	golang
BuildRequires:	pkgconfig(libcap)

%description
Automatic certificate acquisition tool for ACME (Let's Encrypt)

%prep
%autosetup -p1

%build
export GOPATH=`pwd`
%make_build PREFIX=%{_prefix}

%install
mkdir -p %{buildroot}%{_bindir}
export GOPATH=`pwd`
%makeinstall PREFIX=%{buildroot}%{_prefix}

%files
%{_bindir}/acmetool
