Name:           acmetool
Version:        0.0.61
Release:        1
Summary:        Automatic certificate acquisition tool for ACME (Let's Encrypt)
Group:          System/Servers
License:        MIT
URL:            https://github.com/hlandau/acme
Source0:	https://github.com/hlandau/acme/archive/v%{version}.tar.gz
# Needs to package some go libraries along with it...
Source100:	get-source.sh
BuildRequires:	go
BuildRequires:	pkgconfig(libcap)

%description
Automatic certificate acquisition tool for ACME (Let's Encrypt)

%prep
%setup -qn acme-%{version}

%build
export GOPATH=`pwd`
%make PREFIX=%{_prefix}

%install
mkdir -p %{buildroot}%{_bindir}
export GOPATH=`pwd`
%makeinstall PREFIX=%{buildroot}%{_prefix}

%files
%{_bindir}/acmetool
