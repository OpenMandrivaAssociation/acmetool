Name:           acmetool
Version:        0.0.67
Release:        4
Summary:        Automatic certificate acquisition tool for ACME (Let's Encrypt)
Group:          System/Servers
License:        MIT
URL:            https://github.com/hlandau/acme
Source0:	https://github.com/hlandau/acme/archive/v%{version}.tar.gz
# Needs to package some go libraries along with it...
Source100:	get-source.sh
# Generated with "git diff" from acmev2 branch of https://github.com/hlandau/acme
Patch0:		acmetool-acmev2.patch
BuildRequires:	go
BuildRequires:	pkgconfig(libcap)

%description
Automatic certificate acquisition tool for ACME (Let's Encrypt)

%prep
%autosetup -p1 -n acme-%{version}

%build
export GOPATH=`pwd`
%make PREFIX=%{_prefix}

%install
mkdir -p %{buildroot}%{_bindir}
export GOPATH=`pwd`
%makeinstall PREFIX=%{buildroot}%{_prefix}

%files
%{_bindir}/acmetool
