Name: php-qconf-agent		
Version:    1.0.0
Release:	1%{?dist}
Summary:    php ext for QConf Agent

Group:		Development/Languages
License:	QConf
URL:		http://github.com/.../%{name}-%{version}.tgz
Source0:	%{name}-%{version}.tgz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	qconf-agent, qconf-agent-devel, php-devel
Requires:	    qconf-agent

%description
php ext for QConf Agent

%prep
%setup -q


%build
phpize
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}/etc/php.d/
cat <<EOF > %{buildroot}/etc/php.d/qconf.ini
extension=qconf.so
EOF


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/etc/php.d/qconf.ini
/usr/lib64/php/modules/

%changelog

