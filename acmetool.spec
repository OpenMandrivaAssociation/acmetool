Name:           acmetool
Version:        0.0.58
Release:        1
Summary:        Automatic certificate acquisition tool for ACME (Let's Encrypt)
Group:          System/Servers
License:        MIT
URL:            https://github.com/hlandau/acme
Source0:	acmetool-20160918.tar.xz
# Needs to package some go libraries along with it...
Source100:	get-source.sh
BuildRequires:	go
BuildRequires:	pkgconfig(libcap)

%description
Automatic certificate acquisition tool for ACME (Let's Encrypt)

%prep
%setup -qn acmetool

%build
export GOPATH=`pwd`
mv src/github.com/hlandau/acme/Makefile .
%make PREFIX=%{_prefix}

%install
mkdir -p %{buildroot}%{_bindir}
export GOPATH=`pwd`
%makeinstall PREFIX=%{buildroot}%{_prefix}

%files
%{_bindir}/acmetool
