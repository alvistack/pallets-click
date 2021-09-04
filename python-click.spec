%global debug_package %{nil}

Name: python-click
Epoch: 100
Version: 8.1.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Simple wrapper around optparse for powerful command line utilities
License: BSD-3-Clause
URL: https://github.com/pallets/click/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Click is a Python package for creating command line interfaces in a
composable way with as little code as necessary. It's the "Command Line
Interface Creation Kit". It is configurable, and comes with defaults out
of the box.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-click
Summary: Simple wrapper around optparse for powerful command line utilities
Requires: python3
Provides: python3-click = %{epoch}:%{version}-%{release}
Provides: python3dist(click) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-click = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(click) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-click = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(click) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-click
Click is a Python package for creating command line interfaces in a
composable way with as little code as necessary. It's the "Command Line
Interface Creation Kit". It is configurable, and comes with defaults out
of the box.

%files -n python%{python3_version_nodots}-click
%license LICENSE.rst
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-click
Summary: Simple wrapper around optparse for powerful command line utilities
Requires: python3
Provides: python3-click = %{epoch}:%{version}-%{release}
Provides: python3dist(click) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-click = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(click) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-click = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(click) = %{epoch}:%{version}-%{release}

%description -n python3-click
Click is a Python package for creating command line interfaces in a
composable way with as little code as necessary. It's the "Command Line
Interface Creation Kit". It is configurable, and comes with defaults out
of the box.

%files -n python3-click
%license LICENSE.rst
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-click
Summary: Simple wrapper around optparse for powerful command line utilities
Requires: python3
Provides: python3-click = %{epoch}:%{version}-%{release}
Provides: python3dist(click) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-click = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(click) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-click = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(click) = %{epoch}:%{version}-%{release}

%description -n python3-click
Click is a Python package for creating command line interfaces in a
composable way with as little code as necessary. It's the "Command Line
Interface Creation Kit". It is configurable, and comes with defaults out
of the box.

%files -n python3-click
%license LICENSE.rst
%{python3_sitelib}/*
%endif

%changelog
