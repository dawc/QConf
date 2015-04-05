Name:    qconf-agent	
Version: 1.0.0
Release: 1%{?dist}
Summary: Qihoo Distrubuted Configuration Management System	

Group:	 Productivity/Databases/Servers
License: QConf
URL:     http://github.com/.../%{name}-%{version}.tgz
Source0:	%{name}-%{version}.tgz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: automake >= 1.14, gdbm-devel, libcurl-devel, libzookeeper-devel
Requires:	libstdc++, libcurl, gdbm, libzookeeper

%description
Qihoo Distrubuted Configuration Management System

%prep
%setup -q


%build

mkdir build && cd build && cmake .. \
    -DCMAKE_INSTALL_PREFIX=%{buildroot}/usr/local/qconf -DQCONF_AGENT_DIR=/usr/local/qconf -DHAS_PREFIX=1
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
cd build && make install

mkdir -p %{buildroot}/usr/sbin/
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/etc/rc.d/init.d/
cp %{buildroot}/usr/local/qconf/bin/qconf_agent %{buildroot}/usr/sbin/qconf_agent
cp %{buildroot}/usr/local/qconf/bin/qconf       %{buildroot}/usr/bin/qconf
mv %{buildroot}/usr/local/qconf/bin/qconf-agent %{buildroot}/etc/rc.d/init.d/
ln -sf /usr/local/qconf/conf %{buildroot}/etc/qconf


%post
/sbin/chkconfig qconf-agent on

%preun
/etc/init.d/qconf-agent stop 2>/dev/null || /bin/true
/sbin/chkconfig qconf-agent off

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%config /usr/local/qconf/conf/
/usr/local/qconf/include/
/usr/local/qconf/lib/
/usr/local/qconf/lock/lockfile
/usr/local/qconf/version
/usr/local/qconf/cmd/
/usr/local/qconf/doc/
/usr/local/qconf/dumps/
/usr/local/qconf/logs/
/usr/local/qconf/monitor/
/usr/local/qconf/result/
/usr/local/qconf/script/
%attr(0755,-,-) /usr/local/qconf/bin/agent-cmd.sh
%attr(0755,-,-) /usr/local/qconf/bin/qconf
%attr(0755,-,-) /usr/local/qconf/bin/qconf_agent
%attr(0755,-,-) /usr/bin/qconf
%attr(0755,-,-) /usr/sbin/qconf_agent
%attr(0755,-,-) /etc/rc.d/init.d/qconf-agent
/etc/qconf/

%changelog

