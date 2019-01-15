%bcond_without python3
%bcond_without tests

%bcond_without python2
%global srcname docker

Name:           python-%{srcname}
Version:        3.5.0
Release:        2%{?dist}
Summary:        A Python library for the Docker Engine API
License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-requests >= 2.14.2
Requires:       python-six >= 1.4.0
Requires:       python-websocket-client >= 0.32.0
Requires:       python-docker-pycreds >= 0.2.1
Requires:       python-pyopenssl
Requires:       python-idna
Requires:       python-cryptography


# Upstream uses environment markers to conditionally apply some dependencies.
# Environment markers were first added in setuptools 20.6.8, so that doesn't
# work in RHEL.  This patch converts those environment markers into simple if
# statements.
Patch1:		remove-environment-markers.patch

BuildArch:      noarch

%description
It lets you do anything the docker command does, but from within Python apps –
run containers, manage containers, manage Swarms, etc.

%prep
%autosetup -n %{srcname}-%{version} -p 1
rm -fr docker.egg-info

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/*
